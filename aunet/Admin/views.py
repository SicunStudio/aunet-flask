# -*-coding:utf-8 -*-
from flask import render_template,current_app,redirect,request,make_response,session
from flask_login import current_user,login_user,logout_user,login_required
from flask_principal import identity_loaded,RoleNeed,UserNeed,ActionNeed
from flask_principal import Identity, AnonymousIdentity, \
     identity_changed,Permission
# from flask_restful import abort
import json,os,random
from werkzeug.security import generate_password_hash
from flask import abort
from .news import SilderShow1,SliderShowSpec,News1,NewsSpec,NewsSpecDetail,Tags,Tag1,Categorys,Category1
from .users import Users,UserSpec,Roles,RoleSpec,Nodes,NodeSpec,CurrentUser
from .search import SearchNews
from .login import Login


from aunet import lm,app,api,db
from .models import User,LoginLog
from .models import EditUserPermission,EditUserNeed
from .email import send_email
from . import admin
from . import ts
from collections import namedtuple
from functools import partial


#user has the permission of edit himself
EditUserNeed=partial(namedtuple("user",['method','value']),'edit')

class EditUserPermission(Permission):
    def __init__(self,user_id):
        need=EditUserNeed(int(user_id))
        super(EditUserPermission,self).__init__(need)


@lm.user_loader
def load_user(id):
    return User.query.get(int(id))

# @lm.unauthorized_handler
# def unauthorized_handle():
#     return "good"

@identity_loaded.connect_via(app)
def on_identity_loaded(sender, identity):
    # Set the identity user object
    identity.user = current_user
    #user has the permission of edit himself

    identity.provides.add(EditUserPermission(current_user.id))

    # Add the UserNeed to the identity
    if hasattr(current_user, 'id'):
        identity.provides.add(UserNeed(current_user.id))
        for role in current_user.roles:
            identity.provides.add(RoleNeed(role.roleName))
        
    # Assuming the User model has a list of nodes, update the
    # identity with the nodes that the user provides
    if hasattr(current_user,"roles"):
        for role in current_user.roles:
            for node in role.nodes:
                if (node.status==1) and (current_user.status==1) and (role.status==1):
                    identity.provides.add(ActionNeed(node.nodeName))
    	
    
    		
@admin.route('/index')
@admin.route('/')
def index():    
    return render_template("Admin/index.html")


@admin.route('/login',methods=["POST","GET"])
def login():
    if request.method=="POST":
        confirmCode=request.form['confirmCode']
        user=User.query.filter(User.userName==request.form['userName']).first()
        if user==None:
            confirmCode=random.randint(100, 999)
            session['confirmCode']=confirmCode
            error="用户不存在"
            return render_template("Admin/login.html",confirmCode=confirmCode,error=error)
        elif user.verify_password(request.form['password']) is not True:
            confirmCode=random.randint(100, 999)
            session['confirmCode']=confirmCode
            error="密码错误"
            return render_template("Admin/login.html",confirmCode=confirmCode,error=error)
        elif int(confirmCode)!=session['confirmCode']:
            confirmCode=random.randint(100, 999)
            session['confirmCode']=confirmCode
            error="验证码错误"
            return render_template("Admin/login.html",confirmCode=confirmCode,error=error)
        else:          
            login_user(user)
            ip=request.remote_addr
            log=LoginLog(current_user.userName,ip)
            db.session.add(log)
            db.session.commit()
            identity_changed.send(current_app._get_current_object(),identity=Identity(user.id))
            if user.userName=="association" or user.userName=="association_admin":
                return redirect("/Material")
            else:
                return redirect(request.args.get('next') or '/')
    confirmCode=random.randint(100, 999)
    session['confirmCode']=confirmCode
    error=None 
    return render_template("Admin/login.html",confirmCode=confirmCode,error=error)

# @lm.unauthorized_handler
# def unauthorized_handle():
#     return "good"

@app.route('/logout')
# @login_required
def logout():
    # Remove the user information from the session
    logout_user()

    # Remove session keys set by Flask-Principal
    for key in ('identity.name', 'identity.auth_type'):
        session.pop(key, None)
    # identity=AnonymousIdentity()
    # Tell Flask-Principal the user is anonymous
    # identity_changed.send(current_app._get_current_object(),
    #                       identity=AnonymousIdentity())

    return redirect(request.args.get('next') or '/')

@app.route("/templates/Admin/<string:path>",methods=['GET',"POST"])
def getHtml(path):
    # path=request.args.get("path","templates/Home/index/index.html")
    #return "dg"
    path=os.path.join('/home/lyjdwh/Documents/aunet-flask','aunet/templates/Admin/',path)
    path=str(path)
    try:
        f=open(path)
        # text=f.read()
        # res = make_response(text)
        # return res
        return f.read()
    except:
        return "not found" ,404


@app.route("/dashboard", methods=["GET"])
@app.route("/dashboard/<string:path>", methods=["GET"])
def app():
    with open("aunet/templates/Admin/app.html") as f:
        return f.read()



    

@admin.route('/upload',methods=['GET',"POST"])
def upload():
    pass

@admin.route('/forget',methods=["GET","POST"])
def forget():
    if request.method=="POST":
        userName=request.form['userName']
        email=request.form['email']
        user=User.query.filter(User.userName==userName).first()
        subject="验证邮箱"
        token=ts.dumps(user.userName,salt="you will never guess")
        confirm_url=url_for("admin.confirm",token=token,_external=True)
        html=render_template(
            'Admin/conform.html',
            confirm_url=confirm_url)
        if email==user.email:
            send_email(subject,user.email,html)
        return redirect(url_for("index"))
    return render_template("")

@admin.route('/confirm/<token>')
def confirm_email(token):
    try:
        userName=ts.loads(token,salt="you will never guess", max_age=86400)
    except:
        abort(404)
    user=User.query.filter(User.userName==userName).first_or_404()
    user.passWord=generate_password_hash("123456")
    db.session.add(user)
    db.session.commit()
    return "good"

#User 模块
api.add_resource(CurrentUser,"/api/User/CurrentUser")
api.add_resource(Users, '/api/User/Users')
api.add_resource(UserSpec,"/api/User/Users/<string:id>")
api.add_resource(Nodes,"/api/User/Nodes")
api.add_resource(NodeSpec,"/api/User/Nodes/<string:id>")
api.add_resource(Roles,"/api/User/Roles")
api.add_resource(RoleSpec,"/api/User/Roles/<string:id>")


#News 模块

api.add_resource(SilderShow1,"/api/News/SliderShow")
api.add_resource(SliderShowSpec,"/api/News/SliderShow/<string:id>")
api.add_resource(News1,"/api/News/News")
api.add_resource(NewsSpec,"/api/News/News/<string:id>")                 #gai
api.add_resource(NewsSpecDetail,"/api/News/News/<string:id>/Detail")
api.add_resource(Tags,"/api/News/Tags")
api.add_resource(Tag1,"/api/News/Tags/<string:id>")
api.add_resource(Categorys,"/api/News/Categorys")
api.add_resource(Category1,"/api/News/Categorys/<string:id>")

#Search 模块

api.add_resource(SearchNews,"/api/Search/News")

api.add_resource(Login,"/api/Login")