from flask_restful import reqparse, abort,Resource,fields,marshal_with

from aunet.Home.models import News,Notice,AdvanceNotice
from aunet import db
from ./news import News_fields,Notice_fields,AdvanceNotice_fields


News_parser=reqparse.RequestParser()
News_parser.add_argument("category",type=str,required=True,help="category")#若请求中无此参数，默认为None
News_parser.add_argument('sort',type=str,required=True,help="sort")
News_parser.add_argument('time1',type=str,required=True,help="time1")
News_parser.add_argument('time2',type=str,required=True,help="time2")


Notice_parser=reqparse.RequestParser()
Notice_parser.add_argument('sort',type=str,required=True,help="sort")
Notice_parser.add_argument('time1',type=str,required=True,help="time1")
Notice_parser.add_argument('time2',type=str,required=True,help="time2")


class News1(Resource):
	def get(self):
		args=News_parser.parse_args()
		category=args['category']
		sort=args['sort']
		time1=args['time1']
		time2=args['time2']
		