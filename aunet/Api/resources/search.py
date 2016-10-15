from flask_restful import reqparse, abort,Resource,fields,marshal_with
from datetime import datetime

from aunet.Home.models import News,Notice,AdvanceNotice
from aunet import db
from .news import News_fields,Notice_fields,AdvanceNotice_fields


News_parser=reqparse.RequestParser()
News_parser.add_argument("category",type=str,required=True,help="category is needed")#若请求中无此参数，默认为None
News_parser.add_argument('sort',type=str,required=True,help="sort is needed")
News_parser.add_argument('time1',type=str,required=True,help="time1 is needed")
News_parser.add_argument('time2',type=str,required=True,help="time2 is needed")


Notice_parser=reqparse.RequestParser()
Notice_parser.add_argument('sort',type=str,required=True,help="sort is needed")
Notice_parser.add_argument('time1',type=str,required=True,help="time1 is needed")
Notice_parser.add_argument('time2',type=str,required=True,help="time2 is needed")


class SearchNews(Resource):
	@marshal_with(News_fields)
	def get(self):
		args=News_parser.parse_args()
		category=args['category']
		sort=args['sort']
		time1=args['time1']
		time2=args['time2']
		time1=float(time1)
		time2=float(time2)
		time1=datetime.fromtimestamp(time1)
		time2=datetime.fromtimestamp(time2)
		if sort=="latest":
			news=News.query.filter(News.news_Category==category,News.news_Post_Time<time2,News.news_Post_Time>=time1).order_by(News.news_Id.desc()).all()
		if sort=="first":
			news=News.query.filter(News.news_Category==category,News.news_Post_Time<time2,News.news_Post_Time>=time1).order_by(News.news_Id).all()
		return news

class SearchNotice(Resource):
	@marshal_with(Notice_fields)
	def get(self):
		args=Notice_parser.parse_args()
		sort=args['sort']
		time1=args['time1']
		time2=args['time2']
		time1=float(time1)
		time2=float(time2)
		time1=datetime.fromtimestamp(time1)
		time2=datetime.fromtimestamp(time2)
		if sort=="latest":
			notice=Notice.query.filter(Notice.notice_Post_Time<time2,Notice.notice_Post_Time>time1).order_by(Notice.notice_Id.desc()).all()
		if sort=="first":
			notice=Notice.query.filter(Notice.notice_Post_Time<time2,Notice.notice_Post_Time>time1).order_by(Notice.notice_Id).all()
		return notice

class SearchAdvanceNotice(Resource):
	@marshal_with(AdvanceNotice_fields)
	def get(self):
		args=Notice_parser.parse_args()
		sort=args['sort']
		time1=args['time1']
		time2=args['time2']
		time1=float(time1)
		time2=float(time2)
		time1=datetime.fromtimestamp(time1)
		time2=datetime.fromtimestamp(time2)
		if sort=="latest":
			an=AdvanceNotice.query.filter(AdvanceNotice.an_Post_Time<time2,AdvanceNotice.an_Post_Time>time1).order_by(AdvanceNotice.an_Id.desc()).all()
		if sort=="first":
			an=AdvanceNotice.query.filter(AdvanceNotice.an_Post_Time<time2,AdvanceNotice.an_Post_Time>time1).order_by(AdvanceNotice.an_Id).all()
		return an



		