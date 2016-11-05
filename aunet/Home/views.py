from flask import render_template,flash,redirect,url_for,g,session,request,current_app
from flask_login import login_required,login_user,logout_user
from datetime import datetime, timedelta
from flask import jsonify
import json


from . import home
from .models import News,Category, Tag, SilderShow

@home.route('/',methods=["POST","GET"])
@home.route('/index',methods=["POST","GET"])
def index():
	silder_show=SilderShow.query.order_by(SilderShow.post_time.desc()).limit(5).all()
	CharmAssociation=getNews(1,"charm_association")
	# StarAssociation1=getStarAssociation("StarAssociationer")
	# StarAssociation2=getStarAssociation("StarAUer")
	# StarAssociation3=getStarAssociation("StarTeacher")
	LatestNotice=getNews(5,"notice")
	LatestAdvanceNotice=getNews(5,"advance_notice")
	NewsPinPai=getNews(1,"pin_pai")
	NewsCharmHust=getNews(1,"charm_hust")
	NewsYuLan=getNews(2,"news")
	return render_template("Home/index/index.html",SilderShow=silder_show,CharmAssociation=CharmAssociation   \
					,LatestNotice=LatestNotice \
					,LatestAdvanceNotice=LatestAdvanceNotice,NewsPinPai=NewsPinPai,\
					NewsCharmHust=NewsCharmHust,NewsYuLan=NewsYuLan)

@home.route('/news/<int:year>/<int:month>/<int:day>',methods=["POST","GET"])
def show_News(year,month,day):
	return render_template("Home/news/news.html")

@home.route('/news',methods=["POST","GET"])
def indexNews():
	# LatestNews=getSpecialNumberNews(10)
	return render_template("Home/news/index.html")


# def getStarAssociation(star_Role):
# 	# star_association=
# 	star_association=StarAssociation.query.filter(StarAssociation.star_Role==star_Role).first()
# 	return star_association


def getNews(number,category):
	news=News.query.filter(News.cate==category).order_by(News.post_time.desc()).limit(number).all()
	return news

def news2Json(news,length,page):
	newsJson=dict()
	newsJson['news_Title']=list()
	newsJson['news_Outline']=list()
	newsJson['news_Img_Url']=list()
	newsJson['news_Post_Time']=list()
	newsJson['news_Length']=length
	newsJson['news_Current_Page']=str(page)
	i=0
	for new in news:
		newsJson['news_Title'].append(dict({i:new.news_Title}))
		newsJson['news_Outline'].append(dict({i:new.news_Outline}))
		newsJson['news_Img_Url'].append(dict({i:new.news_Img_Url}))
		newsJson['news_Post_Time'].append(dict({i:new.news_Post_Time.strftime('%Y-%m-%d %H:%M:%S')}))
		i=i+1
	return newsJson   		
	
@home.route('/news/news2Json',methods=["POST","GET"])
def newJson():
	if request.method == 'POST':
		getDict=request.get_json()				
		now = datetime.now()
		Category=getDict['Category']
		Time=getDict['Time']
		Sort=getDict['Sort']
		gotoPage=getDict['gotoPage']
		gotoPage=int(gotoPage)
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

		if(Category=="all" and (Sort=="all" or Sort=="hot" or Sort=="latest")):
			news=News.query.filter(News.post_time>Time).order_by(News.post_time.desc()).all()
			news=news[(gotoPage-1)*10:gotoPage*10]
		elif(Category=="all" and Sort=="oldest"):
			news=News.query.filter(News.post_time>Time).order_by(News.post_time).all()
			news=news[(gotoPage-1)*10:gotoPage*10]
		elif(Category!="all" and (Sort=="all" or Sort=="hot" or Sort=="latest")):
			news=News.query.filter(News.post_time>Time,News.cate==category).order_by(News.post_time.desc()).all()
			news=news[(gotoPage-1)*10:gotoPage*10]
		elif(Category!="all" and Sort=="oldest"):
			news=News.query.filter(News.post_time>Time,News.cate==category).order_by(News.post_time).all()
			news=news[(gotoPage-1)*10:gotoPage*10]
		else:
			news=None
		if news!=None:
			NewsJson=news2Json(news,len(news),gotoPage)
			return jsonify(NewsJson)
		else:
			return "<html><body>bad</body></html>"
	return None



