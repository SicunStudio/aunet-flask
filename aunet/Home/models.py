from .. import db
from datetime import datetime


class News(db.Model):
	__tablename__="news"
	news_Id=db.Column(db.Integer,primary_key=True)
	news_Category=db.Column(db.String(30))
	news_Year=db.Column(db.Integer)
	news_Month=db.Column(db.Integer)
	news_Day=db.Column(db.Integer)
	news_Post_Time=db.Column(db.DateTime)
	#news_Comments=db.Column(db.Text)
	news_Detail=db.Column(db.Text)
	news_Title=db.Column(db.String(60))
	news_Outline=db.Column(db.Text)
	news_Img_Url=db.Column(db.String(20))
	news_Edit=db.Column(db.Boolean)
	news_CommentsNum=db.Column(db.Integer)

	def __init__(self,news_Category,news_Detail,news_Title,news_Outline,news_Img_Url):
		time=datetime.now()
		self.news_Category=news_Category
		self.news_Post_Time=time
		self.news_Year=time.year
		self.news_Month=time.month
		self.news_Day=time.day
		self.news_Detail=news_Detail
		self.news_Title=news_Title
		self.news_Outline=news_Outline
		self.news_Img_Url=news_Img_Url
		self.news_Edit=True

	def __str__(self):
		return "Title:%s"%self.news_Title
class Comments(db.Model):
	__tablename__="comments"
	com_Id=db.Column(db.Integer,primary_key=True)
	
class Notice(db.Model):
	__tablename__="notice"
	notice_id=db.Column(db.Integer,primary_key=True)
	notice_Year=db.Column(db.Integer)
	notice_Month=db.Column(db.Integer)
	notice_Day=db.Column(db.Integer)
	notice_Post_Time=db.Column(db.DateTime)
	#news_Comments=db.Column(db.Text)
	notice_Detail=db.Column(db.Text)
	notice_Title=db.Column(db.String(60))
	notice_Outline=db.Column(db.Text)
	notice_Img_Url=db.Column(db.String(20))
	notice_Edit=db.Column(db.Boolean)
	notice_CommentsNum=db.Column(db.Integer)

	def __init__(self,notice_Detail,notice_Title,notice_Outline,notice_Img_Url):
		time=datetime.now()
		self.notice_Year=time.year
		self.notice_Month=time.month
		self.notice_Day=time.day
		self.notice_Detail=notice_Detail
		self.notice_Title=notice_Title
		self.notice_Outline=notice_Outline
		self.notice_Img_Url=notice_Img_Url
		self.notice_Edit=True
	def __str__(self):
		return self.notice_Outline

class AdvanceNotice(db.Model):
	__tablename__="advance_notice"
	an_Id=db.Column(db.Integer,primary_key=True)
	an_Year=db.Column(db.Integer)
	an_Month=db.Column(db.Integer)
	an_Day=db.Column(db.Integer)
	an_Post_Time=db.Column(db.DateTime)
	#news_Comments=db.Column(db.Text)
	an_Detail=db.Column(db.Text)
	an_Title=db.Column(db.String(60))
	an_Outline=db.Column(db.Text)
	an_Img_Url=db.Column(db.String(20))
	an_Edit=db.Column(db.Boolean)
	an_CommentsNum=db.Column(db.Integer)

	def __init__(self,an_Detail,an_Title,an_Outline,an_Img_Url):
		time=datetime.now()
		self.an_Year=time.year
		self.an_Month=time.month
		self.an_Day=time.day
		self.an_Detail=an_Detail
		self.an_Title=an_Title
		self.an_Outline=an_Outline
		self.an_Img_Url=an_Img_Url
		self.an_Edit=True
	def __str__(self):
		return self.an_Outline




class StarAssociation(db.Model):
	__tablename__="star_association"
	star_Id=db.Column(db.Integer,primary_key=True)
	star_Role=db.Column(db.String(20))#StarAssociationer,StarAUer,StarTeature
	star_Name=db.Column(db.String(25))
	star_Img_Url=db.Column(db.String(30))
	star_Intro=db.Column(db.Text)

	def __init__(self,star_Role,star_Name,star_Img_Url,star_Intro):
		self.star_Role=star_Role
		self.star_Name=star_Name
		self.star_Img_Url=star_Img_Url
		self.star_Intro=star_Intro

	def __str__(self):
	   	return 'StarAssociation (Role:%s,name: %s)' % (self.star_Role,self.star_Name)
#魅力社团
class CharmAssociation(db.Model):
	__tablename__="charm_association"
	id=db.Column(db.Integer,primary_key=True)
	charm_Name=db.Column(db.String(20))
	charm_Img_Url=db.Column(db.String(20))
	charm_Intro=db.Column(db.Text) 
	

	def __init__(self,charm_Name,charm_Img_Url):
		self.charm_Name=charm_Name
		self.charm_Img_Url=charm_Img_Url
		

class AssociationTag(db.Model):
	__tablename__="association_tag"
	id=db.Column(db.Integer,primary_key=True)
	tag=db.Column(db.String(20))
	tag_Id=db.Column(db.Integer,db.ForeignKey("charm_association.id"))
	charmAssociation=db.relationship("CharmAssociation",backref=db.backref('charm_Tag', lazy='dynamic'))

	def __init__(self,tag,charmAssociation):
		self.tag=tag
		self.charmAssociation=charmAssociation
# class Comments(db.Model):
# 	comment_Time=db.Column(db.Datetime)
# 	comment_Content=db.Column(db.Text)




