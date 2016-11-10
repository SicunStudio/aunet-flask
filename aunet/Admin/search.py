from flask_restful import reqparse, abort,Resource,fields,marshal_with
from datetime import datetime

from aunet.Home.models import News
from aunet import db
from .news import News_fields


News_parser=reqparse.RequestParser()
News_parser.add_argument("category",type=str,required=True,help="category is needed")#若请求中无此参数，默认为None
News_parser.add_argument('sort',type=str,required=True,help="sort is needed")
News_parser.add_argument('start',type=int,required=True,help="start is needed")
News_parser.add_argument('end',type=int,required=True,help="end is needed")
News_parser.add_argument('tags',type=str,required=True,action="append",help="tags is needed")

class SearchNews(Resource):
	@marshal_with(News_fields)
	def get(self):
		data=list()
		# data1=dict()
		args=News_parser.parse_args()
		category=args['category']
		sort=args['sort']
		start=args['start']
		end=args['end']
		tags=args['tags']
		start=float(start)
		end=float(end)
		start=datetime.fromtimestamp(start)
		end=datetime.fromtimestamp(end)
		# data1['year']=sort
		# return data1
		# if sort=="latest":
		# 	news=News.query.filter(News.cate==category,News.post_time<end,News.post_time>=start).order_by(News.id.desc()).all()
		# if sort=="first":
		# 	news=News.query.filter(News.cate==category,News.post_time<end,News.post_time>=start).order_by(News.id).all()
		# data1['aa']=len(news)
		news=News.query.filter(News.post_time<end,News.post_time>=start).all()
		# return data1
		for new in news:
			new_tags=list()
			for tag in new.tags:
				new_tags.append(tag.name)
			cate=new.category[0].name
			if set(tags).issubset(set(new_tags)) is True and cate==category:
				data.append(new)
		return data

		
