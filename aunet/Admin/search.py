from flask_restful import reqparse, abort,Resource,fields,marshal_with
from datetime import datetime

from aunet.Home.models import News
from aunet import db
from .news import News_fields


News_parser=reqparse.RequestParser()
News_parser.add_argument("category",type=str,required=True,help="category is needed")#若请求中无此参数，默认为None
News_parser.add_argument('sort',type=str,required=True,help="sort is needed")
News_parser.add_argument('time1',type=str,required=True,help="time1 is needed")
News_parser.add_argument('time2',type=str,required=True,help="time2 is needed")
News_parser.add_argument('tags',type=str,required=True,help="tags is needed")

class SearchNews(Resource):
	@marshal_with(News_fields)
	def get(self):
		data=list()
		args=News_parser.parse_args()
		category=args['category']
		sort=args['sort']
		time1=args['time1']
		time2=args['time2']
		tags=args['tags']
		time1=float(time1)
		time2=float(time2)
		time1=datetime.fromtimestamp(time1)
		time2=datetime.fromtimestamp(time2)
		if sort=="latest":
			news=News.query.filter(News.cate==category,News.post_time<time2,News.post_time>=time1).order_by(News.news_Id.desc()).all()
		if sort=="first":
			news=News.query.filter(News.cate==category,News.post_time<time2,News.post_time>=time1).order_by(News.news_Id).all()
		for new in news:
			new_tags=list()
			for tag in new.tags:
				new_tags.append(tag.name)

			if set(tags).issubset(set(new_tags)) is True:
				data.aptpend(new)
		return data

		
