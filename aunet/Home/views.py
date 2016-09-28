from flask import render_template,flash,redirect,url_for,g,session,request,current_app
from flask_login import current_app,login_required,login_user,logout_user
from datetime import datetime, timedelta
from flask import jsonify
import json

from . import home
from .models import News,Notice,AdvanceNotice,StarAssociation,CharmAssociation,AssociationTag

@home.route('/news/1',methods=["POST","GET"])
def getData():
	# data1=session['DataType']
	# data1=session['Data2']
	data1="1"
	data2=session['Data1']
	#data3=g.Data
	data3="3"
	return render_template("Home/ceshi.html",data1=data1,data2=data2,data3=data3)



@home.route('/',methods=["POST","GET"])
@home.route('/index',methods=["POST","GET"])
def index():
	LatestFiveNews=getLatestNews()
	charm_association=getCharmAssociation()
	StarAssociation1=getStarAssociation("StarAssociationer")
	StarAssociation2=getStarAssociation("StarAUer")
	StarAssociation3=getStarAssociation("StarTeacher")
	LatestNotice=getLatestNotice(5)
	LatestAdvanceNotice=getLatestAdvanceNotice(5)
	NewsPinPai=getOneSpecialNews("PinPai")
	NewsCharmHust=getOneSpecialNews("CharmHust")
	NewsYuLan=getSpecialNumberNews(2)
	return render_template("Home/index/index.html",LatestFiveNews=LatestFiveNews,CharmAssociation=charm_association   \
					,StarAssociation1=StarAssociation1,StarAssociation2=StarAssociation2,StarAssociation3=StarAssociation3,LatestNotice=LatestNotice \
					,LatestAdvanceNotice=LatestAdvanceNotice,NewsPinPai=NewsPinPai,\
					NewsCharmHust=NewsCharmHust,NewsYuLan=NewsYuLan)

@home.route('/news/<int:year>/<int:month>/<int:day>',methods=["POST","GET"])
def show_News(year,month,day):
	return render_template("Home/news/news.html")

@home.route('/news',methods=["POST","GET"])
def indexNews():
	# LatestNews=getSpecialNumberNews(10)
	return render_template("Home/news/news.html")

def getLatestNews():
	LatestFiveNews=News.query.order_by(News.news_Post_Time.desc()).limit(5).all()
	return LatestFiveNews

def getCharmAssociation():
	charm_association=CharmAssociation.query.order_by(CharmAssociation.id.desc()).first()
	return charm_association

def getStarAssociation(star_Role):
	star_association=StarAssociation.query.filter(StarAssociation.star_Role==star_Role).first()
	return star_association

def getLatestNotice(number):
	LatestNotice=Notice.query.order_by(Notice.notice_id.desc()).limit(number).all()
	return LatestNotice
def getLatestAdvanceNotice(number):
	LatestAdvanceNotice=AdvanceNotice.query.order_by(AdvanceNotice.an_Id).limit(number).all()
	return LatestAdvanceNotice
def getOneSpecialNews(news_Category):
	SpecialNews=News.query.filter(News.news_Category==news_Category).first()
	return SpecialNews
def getSpecialNumberNews(number):
	news=News.query.filter(News.news_Category=="news").order_by(News.news_Post_Time.desc()).limit(number).all()
	return news

def news2Json(news,length,page):
	newsJson=dict()
	newsJson['news_Title']=list()
	newsJson['news_Outline']=list()
	newsJson['news_Img_Url']=list()
	newsJson['news_Post_Time']=list()
	newsJson['news_Length']=length
	newsJson['news_Current_Page']=page
	i=0
	for new in news:
		newsJson['news_Title'].append(dict({i:new.news_Title}))
		newsJson['news_Outline'].append(dict({i:new.news_Outline}))
		newsJson['news_Img_Url'].append(dict({i:new.news_Img_Url}))
		newsJson['news_Post_Time'].append(dict({i:new.news_Post_Time.strftime('%Y-%m-%d %H:%M:%S')}))
		i=i+1
	return json.dumps(newsJson)   		
	
@home.route('/news/news2Json',methods=["POST","GET"])
def newJson():
	if request.method == 'POST':
		g.Data=request.get_data()
		g.Data1=request.data
		session['Data1']=str(request.data)#request.data
		session['Data']=request.get_data()
		session['DataType']=type(request.get_data())
		# session['Data2']=request.get_json()
		
		#return request.get_data()
		 #getJson=request.get_json()
		
		return str(request.get_data())
		# return getJson.gotoPage
		getDict=json.loads(getJson)
		now = datetime.now()
		Category=getDict['Category']
		Time=getDict['Time']
		Sort=getDict['Sort']
		gotoPage=getDict['gotoPage']
		# Category=request.values.get['Category']
		# Time=request.values.get['Time']
		# Sort=request.values.get['Sort']
		# gotoPage=request.values.get['gotoPage']
		if Time=="all":
			Time=now-timedelta(days=365*10)
		elif Time=="week":
			Time=now -timedelta(days=7)
		elif Time=="month":
			Time=now -timedelta(days=90)
		elif Time=="year":
			Time=now-timedelta(days=365)

		if (Category=="all" or Category=="news") and (Sort=="all" or Sort=="hot"):
			news=News.query.filter(News.news_Post_Time>Time,News.news_Id>=(gotoPage-1)*10,News.news_Id<=gotoPage*10).order_by(News.news_CommentsNum).all()
		elif (Category=="notice") and (Sort=="all" or Sort=="hot"):
			news=Notice.query.filter(Notice.notice_Post_Time>Time,Notice.notice_Id>=(gotoPage-1)*10,Notice.notice_Id<=gotoPage*10).order_by(Notice.notice_CommentsNum).all()
		elif (Category=="preview") and (Sort=="all" or Sort=="hot"):
			news=AdvanceNotice.query.filter(AdvanceNotice.an_Post_Time>Time,AdvanceNotice.an_Id>=(gotoPage-1)*10,AdvanceNotice.an_Id<=gotoPage*10).order_by(AdvanceNotice.an_CommentsNum).all()
		elif (Category=="all" or Category=="news") and (Sort=="latest"):
			news=News.query.filter(News.news_Post_Time>Time,News.news_Id>=(gotoPage-1)*10,News.news_Id<=gotoPage*10).order_by(News.news_Id.desc()).all()
		elif (Category=="notice")and (Sort=="latest"):
			news=Notice.query.filter(Notice.notice_Post_Time>Time,Notice.notice_Id>=(gotoPage-1)*10,Notice.notice_Id<=gotoPage*10).order_by(Notice.notice_Id.desc()).all()
		elif (Category=="preview")and (Sort=="latest"):
			news=AdvanceNotice.query.filter(AdvanceNotice.an_Post_Time>Time,AdvanceNotice.an_Id>=(gotoPage-1)*10,AdvanceNotice.an_Id<=gotoPage*10).order_by(AdvanceNotice.an_Id.desc()).all()
		elif (Category=="all" or Category=="news") and (Sort=="oldest"):
			news=News.query.filter(News.news_Post_Time>Time,News.news_Id>=(gotoPage-1)*10,News.news_Id<=gotoPage*10).order_by(News.news_Id).all()
		elif (Category=="preview")and (Sort=="oldest"):
		 	news=AdvanceNotice.query.filter(AdvanceNotice.an_Post_Time>Time,AdvanceNotice.an_Id>=(gotoPage-1)*10,AdvanceNotice.an_Id<=gotoPage*10).order_by(AdvanceNotice.an_Id).all()
		elif (Category=="notice")and (Sort=="oldest"):
			news=Notice.query.filter(Notice.notice_Post_Time>Time,Notice.notice_Id>=(gotoPage-1)*10,Notice.notice_Id<=gotoPage*10).order_by(Notice.notice_Id).all()
		else:
			news=None
		if news!=None:
			NewsJson=news2Json(news,len(news),gotoPage)
			return NewsJson
		else:
			return None
	return None



