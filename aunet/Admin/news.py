from flask_restful import reqparse, abort,Resource,fields,marshal_with
from aunet import db

from aunet.Home.models import News ,SilderShow


# User_parser=reqparse.RequestParser()            # User zhong method post de parser
# User_parser.add_argument('userName',type=str,required =True,location="json",help="userName")
# User_parser.add_argument('passWord',type=str,required =True,location="json",help="passWord")
# User_parser.add_argument('email',type=str,location="json",help="email")
# User_parser.add_argument('roleName',type=str,required =True,location="json",help="roleName")
parser=reqparse.RequestParser()
parser.add_argument('page',type=int,help="page")#若请求中无此参数，默认为None
parser.add_argument('per_page',type=int,help="per_page")

SilderShow_parser=reqparse.RequestParser()
SilderShow_parser.add_argument('title',type=str,required=True,location="json",help="title is needed")
SilderShow_parser.add_argument('imgUrl',type=str,required=True,location="json",help="imgUrl is needed")
SilderShow_parser.add_argument("outline",type=str,required=True,location="json",help="outline is needed")
SilderShow_parser.add_argument("link",type=str,required=True,location="json",help="the link that jump")


SilderShowSpec_parser=reqparse.RequestParser()
SilderShowSpec_parser.add_argument('title',type=str,location="json",help="title")
SilderShowSpec_parser.add_argument('imgUrl',type=str,location="json",help="imgUrl")
SilderShowSpec_parser.add_argument("outline",type=str,location="json",help="outline")
SilderShowSpec_parser.add_argument("status",type=int,location='json',help="status")
SilderShowSpec_parser.add_argument("link",type=str,location="json",help="the link that jump")

News_parser=reqparse.RequestParser()
News_parser.add_argument("category",type=int,location="json",required=True,help="category id is needed")
News_parser.add_argument("detail",type=str,location="json",required=True,help="detail is needed")
News_parser.add_argument("title",type=str,location="json",required=True,help="title is needed")
News_parser.add_argument("outline",type=str,location="json",required=True,help="outline is needed")
News_parser.add_argument('imgUrl',type=str,location="json",required=True,help="imgUrl is needed",action='append')
News_parser.add_argument("imgUrlFirst",type=str,location="json",required=True,help="imgUrlFirst is needed")
News_parser.add_argument("tags",type=int ,location="json",required=True,action='append',help="tags id is needed")

NewsSpec_parser=reqparse.RequestParser()
NewsSpec_parser.add_argument("category",type=str,location="json",help="category")
NewsSpec_parser.add_argument("detail",type=str,location="json",help="detail")
NewsSpec_parser.add_argument("title",type=str,location="json",help="title")
NewsSpec_parser.add_argument("outline",type=str,location="json",help="outline")
NewsSpec_parser.add_argument('imgUrl',type=str,location="json",help="imgUrl",action='append')
NewsSpec_parser.add_argument("imgUrlFirst",type=str,location="json",help="imgUrlFirst")
NewsSpec_parser.add_argument("edit",type=int,location="json",help="edit status")
News_parser.add_argument("tags",type=int ,location="json",action='append',help="tags id is needed")

class CategoryItem(fields.Raw):
    def format(self,category):
        return category[0].name
class TagItem(fields.Raw):
    def format(self,news_tag):
        tags=list()
        for tag in news_tag:
            tags.append(tag.name)
        return tags

News_fields={
    "id":fields.Integer(attribute="id"),
    "category":CategoryItem,
    "tags":TagItem,
    "postTime":fields.DateTime(dt_format='iso8601',attribute="post_time"),#rfc822/iso8601
    "title":fields.String(attribute="title"),
    "outline":fields.String(attribute="outline"),
    "edit":fields.Integer(attribute="edit")
}
  
SilderShow_fields={
    "id":fields.Integer,
    "postTime":fields.DateTime(dt_format='iso8601',attribute="post_time"),#rfc822/iso8601
    "title":fields.String,
    'imgUrl':fields.String(attribute="img_url"),
    "outline":fields.String,
    "status":fields.Integer,
    "link":fields.Url
}


def abort_if_not_exist(data,message):
    if data==None:
        abort(404,message="{} Not Found".format(message))                                                                               

 
class SilderShow1(Resource):
    @marshal_with(SilderShow_fields)
    def get(self):
        args=parser.parse_args()
        page=args['page']
        per_page=args['per_page']
        if page!=None and per_page!=None:
            silder_shows=SilderShow.query.filter(SilderShow.id>=(page-1)*per_page,SilderShow.id<page*per_page).all()
        else:
            silder_shows=SilderShow.query.all()
        return silder_shows
    def post(self):
        args=SilderShow_parser.parse_args()
        title=args['title']
        imgUrl=args['imgUrl']
        outline=args['outline']
        link=args['link']
        silder_show=SilderShow(title,imgUrl,outline,link)
        db.session.add(silder_show)
        db.session.commit()

class SliderShowSpec(Resource):
    @marshal_with(SilderShow_fields)
    def get(self,id):
        id=int(id)
        silder_show=SilderShow.query.filter(SilderShow.id==id).first()
        abort_if_not_exist(silder_show,"silder_show")
        return silder_show

    def put(self,id):
        id=int(id)
        silder_show=SilderShow.query.filter(SilderShow.id==id).first()
        abort_if_not_exist(silder_show,"silder_show")
        args=SilderShowSpec_parser.parse_args()
        title=args['title']
        imgUrl=args['imgUrl']
        outline=args['outline']
        status=args['status'] 
        link=args['link']
        if title!=None:
            silder_show.title=title
        if imgUrl!=None:
            silder_show.img_Url=imgUrl
        if outline!=None:
            silder_show.outline=outline
        if status!=None:
            silder_show.status=status
        if link!=None:
            silder_show.link=link
        db.session.add(silder_show)
        db.session.commit()

    def delete(self,id):
        id=int(id)
        silder_show=SilderShow.query.filter(SilderShow.id==id).first()
        abort_if_not_exist(silder_show,"silder_show")
        db.session.delete(silder_show)
        db.session.commit()

class News1(Resource):
    @marshal_with(News_fields)
    def get(self):
        args=parser.parse_args()
        page=args['page']
        per_page=args['per_page']
        if page!=None and per_page!=None:
            news=News.query.filter(News.id>=(page-1)*per_page,News.id<page*per_page).all()
        else:
            news=News.query.all()
        return news
    def post(self):
        args=News_parser.parse_args()
        category=args['category']
        detail=args['detail']
        title=args['title']
        outline=args['outline']
        imgUrl=args['imgUrl']######################################################
        imgUrlFirst=args['imgUrlFirst']
        tags=args['tags']
        news=News(detail,title,outline,imgUrlFirst)
        db.session.add(news)
        db.session.commit()
        news.addCategory(category)
        for tag in tags:
            news.addTag(tag)
        db.session.add(news)
        db.session.commit()


class NewsSpec(Resource):
    @marshal_with(News_fields)
    def get(self,id):
        id=int(id)
        news=News.query.filter(News.id==id).first()
        abort_if_not_exist(news,"news")
        return news

    def put(self,id):
        id=int(id)
        news=News.query.filter(News.news_Id==id).first()
        abort_if_not_exist(news,"news")
        args=NewsSpec_parser.parse_args()
        category=args['category']
        detail=args['detail']
        title=args['title']
        outline=args['outline']
        imgUrl=args['imgUrl']   ######################################################
        imgUrlFirst=args['imgUrlFirst']
        edit=args['edit']
        tags=args['tags']
        if category!=None:
            news.category=[]
            news.addCategory(category)
        if detail!=None:
            news.news_Detail=detail
        if title!=None:
            news.news_Title=title
        if outline!=None:
            news.news_Outline=outline
        if imgUrlFirst!=None:
            news.news_Img_Url=imgUrlFirst
        if edit!=None:
            news.news_Edit=edit
        if tags!=None:
            news.tags=[]
            for tag in tags:
                news.addTag(tag)
        db.session.add(news)
        db.session.commit()

    def delete(self,id):
        id=int(id)
        news=News.query.filter(News.id==id).first()
        abort_if_not_exist(news,"news")
        db.session.delete(news)
        db.session.commit()
class NewsSpecDetail(Resource):
    def get(self,id):
        id=int(id)
        news=News.query.filter(News.id==id).first()
        abort_if_not_exist(news,"news")
        data=dict()
        data['detail']=news.news_Detail
        return data





