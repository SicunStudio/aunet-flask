from flask_restful import reqparse, abort,Resource,fields,marshal_with
from aunet import db

from aunet.Home.models import News,Notice, AdvanceNotice, StarAssociation, CharmAssociation, AssociationTag,SilderShow


# User_parser=reqparse.RequestParser()            # User zhong method post de parser
# User_parser.add_argument('userName',type=str,required =True,location="json",help="userName")
# User_parser.add_argument('passWord',type=str,required =True,location="json",help="passWord")
# User_parser.add_argument('email',type=str,location="json",help="email")
# User_parser.add_argument('roleName',type=str,required =True,location="json",help="roleName")
parser=reqparse.RequestParser()
parser.add_argument('page',type=int,help="page")#若请求中无此参数，默认为None
parser.add_argument('per_page',type=int,help="per_page")

SilderShow_parser=reqparse.RequestParser()
SilderShow_parser.add_argument('title',type=str,required=True,location="json",help="title")
SilderShow_parser.add_argument('imgUrl',type=str,required=True,location="json",help="imgUrl")
SilderShow_parser.add_argument("outline",type=str,required=True,location="json",help="outline")


SilderShowSpec_parser=reqparse.RequestParser()
SilderShowSpec_parser.add_argument('title',type=str,location="json",help="title")
SilderShowSpec_parser.add_argument('imgUrl',type=str,location="json",help="imgUrl")
SilderShowSpec_parser.add_argument("outline",type=str,location="json",help="outline")
SilderShowSpec_parser.add_argument("status",type=int,location='json',help="status")

CharmAssociation_parser=reqparse.RequestParser()
CharmAssociation_parser.add_argument('name',type=str,location="json",required=True,help="name"),
CharmAssociation_parser.add_argument('imgUrl',type=str,location="json",required=True,help="imgUrl"),
CharmAssociation_parser.add_argument("intro",type=str,location="json",required=True,help="intro"),
CharmAssociation_parser.add_argument("tags",type=str,location="json",required=True,help="tags",action='append')

CharmAssociationSpec_parser=reqparse.RequestParser()
CharmAssociationSpec_parser.add_argument('name',type=str,location="json",help="name"),
CharmAssociationSpec_parser.add_argument('imgUrl',type=str,location="json",help="imgUrl"),
CharmAssociationSpec_parser.add_argument("intro",type=str,location="json",help="intro"),
CharmAssociationSpec_parser.add_argument("tags",type=str,location="json",help="tags",action='append')

News_parser=reqparse.RequestParser()
News_parser.add_argument("category",type=str,location="json",required=True,help="category")
News_parser.add_argument("detail",type=str,location="json",required=True,help="detail")
News_parser.add_argument("title",type=str,location="json",required=True,help="title")
News_parser.add_argument("outline",type=str,location="json",required=True,help="outline")
News_parser.add_argument('imgUrl',type=str,location="json",required=True,help="imgUrl",action='append')
News_parser.add_argument("imgUrlFirst",type=str,location="json",required=True,help="imgUrlFirst")

NewsSpec_parser=reqparse.RequestParser()
NewsSpec_parser.add_argument("category",type=str,location="json",help="category")
NewsSpec_parser.add_argument("detail",type=str,location="json",help="detail")
NewsSpec_parser.add_argument("title",type=str,location="json",help="title")
NewsSpec_parser.add_argument("outline",type=str,location="json",help="outline")
NewsSpec_parser.add_argument('imgUrl',type=str,location="json",help="imgUrl",action='append')
NewsSpec_parser.add_argument("imgUrlFirst",type=str,location="json",help="imgUrlFirst")
NewsSpec_parser.add_argument("edit",type=int,location="json",help="edit status")


Notice_parser=reqparse.RequestParser()
Notice_parser.add_argument("detail",type=str,location="json",required=True,help="detail")
Notice_parser.add_argument("title",type=str,location="json",required=True,help="title")
Notice_parser.add_argument("outline",type=str,location="json",required=True,help="outline")
Notice_parser.add_argument('imgUrl',type=str,location="json",required=True,help="imgUrl",action='append')
Notice_parser.add_argument("imgUrlFirst",type=str,location="json",required=True,help="imgUrlFirst")

News_fields={
    "id":fields.Integer(attribute="news_Id"),
    "category":fields.String(attribute="news_Category"),
    "postTime":fields.DateTime(dt_format='iso8601',attribute="news_Post_Time"),#rfc822/iso8601
    "title":fields.String(attribute="news_Title"),
    "outline":fields.String(attribute="news_Outline"),
    "edit":fields.Integer(attribute="news_Edit")
}
Notice_fields={
    "id":fields.Integer(attribute="notice_Id"),
    "postTime":fields.DateTime(dt_format='iso8601',attribute="notice_Post_Time"),#rfc822/iso8601
    "title":fields.String(attribute="notice_Title"),
    "outline":fields.String(attribute="notice_Outline"),
    "edit":fields.Integer(attribute="notice_Edit")
}

AdvanceNotice_fields={
    "id":fields.Integer(attribute="an_Id"),
    "postTime":fields.DateTime(dt_format='iso8601',attribute="an_Post_Time"),#rfc822/iso8601
    "title":fields.String(attribute="an_Title"),
    "outline":fields.String(attribute="an_Outline"),
    "edit":fields.Integer(attribute="an_Edit")
}
SilderShow_fields={
    "id":fields.Integer,
    "postTime":fields.DateTime(dt_format='iso8601',attribute="news_Post_Time"),#rfc822/iso8601
    "title":fields.String,
    'imgUrl':fields.String(attribute="img_Url"),
    "outline":fields.String,
    "status":fields.Integer
}

class TagItem(fields.Raw):
    def format(self,charm_Tag):
        tags=[]
        for tag in charm_Tag:
            tags.append(tag.tag)
        return tags
CharmAssociation_fields={
    "id":fields.Integer,
    "name":fields.String(attribute="charm_Name"),
    "imgUrl":fields.String(attribute="charm_Img_Url"),
    "intro":fields.String(attribute="charm_Intro"),                                     
    "tags":TagItem(attribute="charm_Tag")
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
        silder_show=SilderShow(title,imgUrl,outline)
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
        if title!=None:
            silder_show.title=title
        if imgUrl!=None:
            silder_show.img_Url=imgUrl
        if outline!=None:
            silder_show.outline=outline
        if status!=None:
            silder_show.status=status
        db.session.add(silder_show)
        db.session.commit()

    def delete(self,id):
        id=int(id)
        silder_show=SilderShow.query.filter(SilderShow.id==id).first()
        abort_if_not_exist(silder_show,"silder_show")
        db.session.delete(silder_show)
        db.session.commit()

class CharmAssociation1(Resource):
    @marshal_with(CharmAssociation_fields)
    def get(self):
        args=parser.parse_args()
        page=args['page']
        per_page=args['per_page']
        if page!=None and per_page!=None:
            charm_associations=CharmAssociation.query.filter(CharmAssociation.id>=(page-1)*per_page,CharmAssociation.id<page*per_page).all()
        else:
            charm_associations=CharmAssociation.query.all()
        return charm_associations

    def post(self):
        args=CharmAssociation_parser.parse_args()
        name=args['name']
        imgUrl=args['imgUrl']
        intro=args['intro']
        tags=args['tags']
        ca=CharmAssociation(name,imgUrl,intro)
        db.session.add(ca)
        db.session.commit()
        for tag in tags:
            t= AssociationTag(tag,ca)
            db.session.add(t)
            db.session.commit()

class  CharmAssociationSpec(Resource):
    @marshal_with(CharmAssociation_fields)
    def get(self,id):
        id=int(id)
        ca=CharmAssociation.query.filter(CharmAssociation.id==id).first()
        abort_if_not_exist(ca,"CharmAssociation")
        return ca
    def put(self,id):
        ca=CharmAssociation.query.filter(CharmAssociation.id==id).first()
        abort_if_not_exist(ca,"CharmAssociation")
        args=CharmAssociationSpec_parser.parse_args()
        name=args['name']
        imgUrl=args['imgUrl']
        intro=args['intro']
        tags=args['tags']
        if name!=None:
            ca.charm_Name=name
        if imgUrl!=None:
            ca.charm_Img_Url=imgUrl
        if intro!=None:
            ca.charm_Intro=intro
        db.session.add(ca)
        db.session.commit()
        if tags!=None:
            for tag in ca.charm_Tag:
                db.session.delete(tag)
                db.session.commit()
            for tag in tags:
                t= AssociationTag(tag,ca)
                db.session.add(t)
                db.session.commit()

    def delete(self,id):
        ca=CharmAssociation.query.filter(CharmAssociation.id==id).first()
        abort_if_not_exist(ca,"CharmAssociation")
        db.session.delete(ca)
        db.session.commit()


class News1(Resource):
    @marshal_with(News_fields)
    def get(self):
        args=parser.parse_args()
        page=args['page']
        per_page=args['per_page']
        if page!=None and per_page!=None:
            news=News.query.filter(News.news_Id>=(page-1)*per_page,News.news_Id<page*per_page).all()
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
        news=News(category,detail,title,outline,imgUrlFirst)
        db.session.add(news)
        db.session.commit()


class NewsSpec(Resource):
    @marshal_with(News_fields)
    def get(self,id):
        id=int(id)
        news=News.query.filter(News.news_Id==id).first()
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
        if category!=None:
            news.news_Category=category
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

        db.session.add(news)
        db.session.commit()

    def delete(self,id):
        id=int(id)
        news=News.query.filter(News.news_Id==id).first()
        abort_if_not_exist(news,"news")
        db.session.delete(news)
        db.session.commit()
class NewsSpecDetail(Resource):
    def get(self,id):
        id=int(id)
        news=News.query.filter(News.news_Id==id).first()
        abort_if_not_exist(news,"news")
        data=dict()
        data['detail']=news.news_Detail
        return data


class Notice1(Resource):
    @marshal_with(Notice_fields)
    def get(self):
        args=parser.parse_args()
        page=args['page']
        per_page=args['per_page']
        if page!=None and per_page!=None:
            notice=Notice.query.filter(Notice.notice_Id>=(page-1)*per_page,Notice.notice_Id<page*per_page).all()
        else:
            notice=Notice.query.all()
        return notice
    def post(self):
        args=Notice_parser.parse_args()    
        detail=args['detail']
        title=args['title']
        outline=args['outline']
        imgUrl=args['imgUrl']######################################################
        imgUrlFirst=args['imgUrlFirst']
        notice=Notice(detail,title,outline,imgUrlFirst)
        db.session.add(notice)
        db.session.commit()


class NoticeSpec(Resource):
    @marshal_with(Notice_fields)
    def get(self,id):
        id=int(id)
        notice=Notice.query.filter(Notice.notice_Id==id).first()
        abort_if_not_exist(notice,"notice")
        return notice

    def put(self,id):
        id=int(id)
        notice=Notice.query.filter(Notice.notice_Id==id).first()
        abort_if_not_exist(notice,"notice")
        args=NewsSpec_parser.parse_args()#ye ke yi yong NewsSpec_parser
        detail=args['detail']
        title=args['title']
        outline=args['outline']
        imgUrl=args['imgUrl']######################################################
        imgUrlFirst=args['imgUrlFirst']
        edit=args['edit']
        if detail!=None:
            notice.notice_Detail=detail
        if title!=None:
            notice.notice_Title=title
        if outline!=None:
            notice.notice_Outline=outline
        if imgUrlFirst!=None:
            notice.notice_Img_Url=imgUrlFirst
        if edit!=None:
            notice.notice_Edit=edit

        db.session.add(notice)
        db.session.commit()

    def delete(self,id):
        id=int(id)
        notice=Notice.query.filter(Notice.notice_Id==id).first()
        abort_if_not_exist(notice,"notice")
        db.session.delete(notice)
        db.session.commit()

class NoticeSpecDetail(Resource):
    def get(self,id):
        id=int(id)
        notice=Notice.query.filter(Notice.notice_Id==id).first()
        abort_if_not_exist(notice,"notice")
        data=dict()
        data['detail']=notice.notice_Detail
        return data



class AdvanceNotice1(Resource):
    @marshal_with(AdvanceNotice_fields)
    def get(self):
        args=parser.parse_args()
        page=args['page']
        per_page=args['per_page']
        if page!=None and per_page!=None:
            an=AdvanceNotice.query.filter(AdvanceNotice.an_Id>=(page-1)*per_page,AdvanceNotice.an_Id<page*per_page).all()
        else:
            an=AdvanceNotice.query.all()
        return an
    def post(self):
        args=Notice_parser.parse_args()
        detail=args['detail']
        title=args['title']
        outline=args['outline']
        imgUrl=args['imgUrl']######################################################
        imgUrlFirst=args['imgUrlFirst']
        an=AdvanceNotice(detail,title,outline,imgUrlFirst)
        db.session.add(an)
        db.session.commit()


class AdvanceNoticeSpec(Resource):
    @marshal_with(AdvanceNotice_fields)
    def get(self,id):
        id=int(id)
        an=AdvanceNotice.query.filter(AdvanceNotice.an_Id==id).first()
        abort_if_not_exist(an,"advance notice")
        return an

    def put(self,id):
        id=int(id)
        an=AdvanceNotice.query.filter(AdvanceNotice.an_Id==id).first()
        abort_if_not_exist(an,"advance notice")
        args=NewsSpec_parser.parse_args()#ye ke yi yong NewsSpec_parser
        detail=args['detail']
        title=args['title']
        outline=args['outline']
        imgUrl=args['imgUrl']######################################################
        imgUrlFirst=args['imgUrlFirst']
        edit=args['edit']
        if detail!=None:
            an.an_Detail=detail
        if title!=None:
            an.an_Title=title
        if outline!=None:
            an.an_Outline=outline
        if imgUrlFirst!=None:
            an.an_Img_Url=imgUrlFirst
        if edit!=None:
            an.an_Edit=edit

        db.session.add(an)
        db.session.commit()

    def delete(self,id):
        id=int(id)
        an=AdvanceNotice.query.filter(AdvanceNotice.an_Id==id).first()
        abort_if_not_exist(an,"advance notice")
        db.session.delete(an)
        db.session.commit()

class AdvanceNoticeSpecDetail(Resource):
    def get(self,id):
        id=int(id)
        an=AdvanceNotice.query.filter(AdvanceNotice.an_Id==id).first()
        abort_if_not_exist(an,"advance notice")
        data=dict()
        data['detail']=an.an_Detail
        return data
