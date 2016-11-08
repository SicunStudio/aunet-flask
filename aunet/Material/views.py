# -- coding: UTF-8 --
from urllib.request import quote
from docxtpl import DocxTemplate,RichText
from time import time,mktime,strftime,strptime,localtime
from flask import render_template,redirect,url_for,flash,\
     Blueprint,make_response,request,abort,send_file
# from flask_mail import Message
from flask_login import login_required,current_user
from flask_principal import RoleNeed,Permission
from .models import *
import os

from .. import db
from . import material

Upload_path = os.getcwd()+'/aunet/static/Uploads/Material/'
Docx_path = os.getcwd()+'/aunet/static/Material/docx/'
types = {
    'east4':(East4,'东四三楼'),
    'colorprint':(Colorprint,'彩喷悬挂'),
    'material':(Materials,'物资借用'),
    'outdoor':(Outdoor,'路演场地'),
    'sacenter':(Sacenter,'大活教室'),
    'special':(Special,'特殊场地'),
    'sports':(Sports,'体育场馆'),
    'teachingbuilding':(Teachingbuilding,'教学楼教室')
    }

level1 = Permission(RoleNeed('association_admin'))
level2 = level1.union(Permission(RoleNeed('association')))

def make_context(data,type):
    context = {}
    if type in ['east4','outdoor','special','sacenter']:
        context['is_sponsor'] = '是' if data.sponsor\
        else '否'
    if type == 'sacenter':
        context['site'+data.site_type] = data.site
    elif type == 'teachingbuilding':
        days = ['一','二','三','四','五','六','日']
        context['day'] = days[strptime(str(data.date),'%Y-%m-%d').tm_wday]
        for x in ['content','host','unit','title']:
            context[x+data.activity_type] = getattr(data,x)
    #不需要进行渲染的字段
    except_fields = [
        'metadata','query','query_class',
        'id','apply_time','approve_time',
        'advice','result','applicant',
        'year1','month1','date1'
        ]
    #生成context
    for x in dir(data):
        if x in except_fields or x[0]=='_':
            continue
        field = str(getattr(data,x))
        if field == 'None' or field == '0':
            field = ''
        context[x] = field

    return context

def query_data(type,id):
    if type not in types.keys():abort(404)
    data = types[type][0].query.filter_by(id=int(id)).first_or_404()
    if str(current_user.id) != data.applicant:abort(403)
    return data

@material.route('/download/<file_type>',methods=['POST'])
@login_required
@level2.require(403)
def download(file_type):
    '''下载接口'''

    if file_type not in ['form','scheme']:abort(404)
    id = request.form.get('id')
    type = request.form.get('type')
    data = query_data(type,id)
    #下载策划
    if file_type == 'scheme':
        if data.filename == '':abort(404)
        content = send_file(Upload_path+data.filename)
        filename = quote(data.filename[:-10])
    #if data.applicant!=current_user.name :abort(404)
    else :
        #生成context并进行渲染
        context=make_context(data,type)
        for key,value in context.items() :
            context[key] = RichText(value)     
        doc = DocxTemplate(Docx_path+type+'.docx')
        doc.render(context)
        temp_file = str(current_user.id) +'result.docx'
        doc.save(temp_file)
        #读取渲染后的文件并将之删除
        with open(temp_file,'rb') as f:
            content = f.read()           
        if os.path.exists(temp_file):
            os.remove(temp_file)
        filename = quote(data.association+'-'+types[type][1]+'.docx')     
 
    response = make_response(content)
    response.headers['Content-Disposition'] = \
    "attachment;filename*=UTF-8''" + filename
    response.headers['Content-Type'] = 'application/octet-stream'
    return response


@material.route('/delete/',methods=['POST'])
@login_required
@level2.require(403)
def delete():
    '''删除申请'''
    
    id = request.form.get('id')
    type = request.form.get('type')
    data = query_data(type,id)

    if data.filename is not None and \
    os.path.exists(Upload_path+data.filename):
        os.remove(Upload_path+data.filename)
    db.session.delete(data)
    db.session.commit()
    flash('删除成功！')
    return redirect(url_for('material.status'))


@material.route('/submit/',methods=['POST'])
@login_required
@level2.require(403)
def submit():
    '''申请提交接口'''
    
    form = request.form
    type = form['type']
    id = form['uid']
    if type not in types: abort(404)
    time = localtime()
    if id != "":
        data = query_data(type,id)
    else:
        data = types[type][0]()
        upload_file = request.files['file']
        if upload_file.filename != '':    
            rand_filename = upload_file.filename+str(int(mktime(time)))
            data.filename = rand_filename
            upload_file.save(Upload_path+rand_filename)
        else :
            data.filename = 'Nothing'

    data.applicant = current_user.id
    data.date=form['year1']+'-'+form['month1']+'-'+form['date1']
    data.apply_time = strftime('%Y-%m-%d %H:%M:%S',time)
    
 
    if type == 'material':
        if form['material_type'] == '2':
            data.chair_date = form['year2']+'-'\
            +form['month2']+'-'+form['date2']
        if form['material_type'] == '4':
            data.projector_date = form['year3']+'-'\
            +form['month3']+'-'+form['date3']
    date_items = [a+b for a in ['year','month','date'] 
    for b in ['1','2','3']]
    
    for key,value in form.items():
        if key in date_items or key in ['uid','file']:continue
        if key[-3:] =='num' or key == 'number':
            value = 0 if value =='' else int(value)
        setattr(data,key,value)
    try:
        db.session.add(data)
        db.session.commit()
    except:
        db.session.rollback()
        flash("表单数据有误，未能成功提交！")
        return redirect(url_for('material.status'))     
    
    flash("申请提交成功，等待审批！")
    return redirect(url_for('material.status'))


@material.route('/<option>/<type>/',methods=['POST','GET'])
@login_required
@level2.require(403)
def main(option,type):
    '''apply'''
    if type not in types.keys() or \
    option not in ['apply','modify']:abort(404)
    data={}
    if option == 'modify':
        id = request.form.get('id')
        data = types[type][0].query.filter_by(id=id,
            applicant=current_user.id).first_or_404()
    apply_type = types[type][1]
    return render_template('/pages/'+type+'.html',data=data,\
        apply_type = apply_type)

@material.route('/procedure')
@login_required
@level2.require(403)
def procedure():
    data = {'association':'procedure'}
    return render_template('/pages/'+'procedure.html',\
        data = data)


@material.route('/admin/')
@login_required
@level1.require(403)
def admin():
    datas=[]
    for db_type in types.values():
        data = db_type[0].query.all()
        if data is None: 
            continue
        datas.extend(data)
    datas.sort(key=lambda x:x.apply_time,reverse=True)
    return render_template('admin.html',datas=datas,types=types)


@material.route('/status/')
@login_required
@level2.require(403)
def status():
    results ={ '0':'审批中','1':'已通过','2':'未通过'}
    datas=[]
    for db_type in types.values():
        data = db_type[0].query.all()
        if data is None: continue
        datas.extend(data)
    return render_template('/pages/status.html',\
        datas=datas,types=types,results=results)



@material.route('/approve/',methods=['POST'])
@login_required
@level1.require(403)
def approve():

    type = request.form.get('type')
    if type not in types.keys() : abort(404)

    id = request.form.get('id')
    data = types[type][0].query.filter_by(id = int(id)).first_or_404()
    data.advice = request.form.get('advice')
    data.result = request.form.get('result')
    is_print = request.form.get('is_print')
    data.is_print = '否' if is_print is None else '是'
    data.pre_verify = request.form.get('pre_verify')
    data.approve_time = strftime('%Y-%m-%d %H:%M:%S',localtime())
    db.session.add(data)
    db.session.commit()
    flash('审批操作成功！')

    return redirect(url_for('material.admin'))



@material.route('/modal/',methods=['POST'])
@login_required
@level2.require(403)
def modal():
    id = request.form.get('id')
    type = request.form.get('type')
    modal_type = request.form.get('modal_type')
    data = types[type][0].query.filter_by(id = int(id)).first_or_404()
    context = make_context(data,type)
    template = '/modal/'+'modal-' + type + '.html'
    return render_template(template,data=data,context=context,\
        type=types[type][1],modal_type=modal_type)
