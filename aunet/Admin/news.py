# -*-coding:utf-8 -*-
# import extensions and python library
from flask_restful import reqparse, abort, Resource, fields, marshal_with
from flask_principal import Permission, ActionNeed

from datetime import datetime
import time
from bs4 import BeautifulSoup
from io import BytesIO
from urllib import request
import random
import os
import base64
import json
from PIL import Image

# import models needed
from aunet import db, app
from aunet.Home.models import News, SilderShow, Category, Tag

# parser for SilderShow
SilderShow_parser = reqparse.RequestParser()
SilderShow_parser.add_argument(
    'title', type=str, required=True, location="json", help="title is needed")
SilderShow_parser.add_argument(
    'imgUrl', type=str, required=True, location="json", help="imgUrl is needed")
SilderShow_parser.add_argument(
    "outline", type=str, required=True, location="json", help="outline is needed")
SilderShow_parser.add_argument(
    "link", type=str, required=True, location="json", help="the link that jump")


# parser for SilderShowSpec
SilderShowSpec_parser = reqparse.RequestParser()
SilderShowSpec_parser.add_argument(
    'title', type=str, location="json", help="title")
SilderShowSpec_parser.add_argument(
    'imgUrl', type=str, location="json", help="imgUrl")
SilderShowSpec_parser.add_argument(
    "outline", type=str, location="json", help="outline")
SilderShowSpec_parser.add_argument(
    "editable", type=int, location='json', help="status")
SilderShowSpec_parser.add_argument(
    "link", type=str, location="json", help="the link that jump")

News_parser = reqparse.RequestParser()
News_parser.add_argument(
    "category", type=str, location="json", required=True, help="category  is needed")
News_parser.add_argument(
    "detail", type=str, location="json", required=True, help="detail is needed")
News_parser.add_argument(
    "title", type=str, location="json", required=True, help="title is needed")
News_parser.add_argument("tags", type=str, location="json",
                         required=True, action='append', help="tags  is needed")


NewsSpec_parser = reqparse.RequestParser()
NewsSpec_parser.add_argument(
    "category", type=str, location="json", help="category")
NewsSpec_parser.add_argument(
    "detail", type=str, location="json", help="detail")
NewsSpec_parser.add_argument("title", type=str, location="json", help="title")
NewsSpec_parser.add_argument(
    "editable", type=int, location="json", help="edit status")
NewsSpec_parser.add_argument(
    "tags", type=str, location="json", action='append', help="tags id is needed")
NewsSpec_parser.add_argument('detail', type=str, location="json")


parser = reqparse.RequestParser()
parser.add_argument(
    'name', type=str, location='json', help="name is needed", required=True)

parser_spec = reqparse.RequestParser()
parser_spec.add_argument('name', type=str, location='json')

# parser to judge DELETE or POST or PUT http method
RequestMethod_parser = reqparse.RequestParser()
RequestMethod_parser.add_argument('requestMethod', type=str, location='json')


# defined as a new field
class CategoryItem(fields.Raw):

    def format(self, category):
        if len(category) == 0:
            return None
        else:
            return category[0].name


class TagItem(fields.Raw):

    def format(self, news_tag):
        tags = list()
        for tag in news_tag:
            tags.append(tag.name)
        return tags


class PostTimeItem(fields.Raw):

    def format(self, postTime):
        # t=datetime.fromtimestamp(postTime)
        a = postTime.strftime('%Y-%m-%d %H:%M:%S')
        return time.mktime(time.strptime(a, '%Y-%m-%d %H:%M:%S'))


class ImgToDataurl(fields.Raw):

    def format(self, imgUrl):
        try:
            path = os.path.join(app.config['BASEDIR'], 'aunet', imgUrl)
            with open(path, "rb") as f:
                data = f.read()
            data = base64.b64encode(data)  #
            data = str(data)
            data = data[2:-1]
            data = "data:image/jpg;base64,"+data
            return data
        except:
            return imgUrl


# work with marshal_with() to change a class into json
News_fields = {
    "id": fields.Integer(attribute="id"),
    "category": CategoryItem,
    "tags": TagItem,
    "postTime": PostTimeItem(attribute="post_time"),
    "title": fields.String(attribute="title"),
    "outline": fields.String(attribute="outline"),
    "editable": fields.Integer(attribute="editable"),
    "author": fields.String
}
NewsSpec_fields = {
    "id": fields.Integer(attribute="id"),
    "category": CategoryItem,
    "tags": TagItem,
    "postTime": PostTimeItem(attribute="post_time"),
    "title": fields.String(attribute="title"),
    "outline": fields.String(attribute="outline"),
    "editable": fields.Integer(attribute="editable"),
    "author": fields.String,
    "detail": fields.String
}
SilderShow_fields = {
    "id": fields.Integer,
    "postTime": PostTimeItem(attribute="post_time"),
    "imgUrl": ImgToDataurl(attribute="img_url"),
    "outline": fields.String,
    "editable": fields.Integer,
    "link": fields.String,
    "title": fields.String
}


# manage error message
def abort_if_not_exist(data, message):
    if data == None:
        abort(404, message="{} Not Found".format(message))


def abort_if_exist(data, message):
    if data != None:
        abort(
            400, message="{} has existed ,please try another".format(message))


def abort_if_unauthorized(message):
    abort(401, message="{} permission Unauthorized".format(message))


# change the img url into dataurl ,and return the first image
def handle_html(html):
    soup = BeautifulSoup(html, "html.parser")
    image_num = 0  # judge if  these
    for img in soup.find_all('img'):
        imgurl = img.get('src')
        data = request.urlopen(imgurl).read()
        imgBuf = BytesIO(data)  # change image in ram to batesIo
        i = Image.open(imgBuf)
        filename = str(int(random.uniform(1, 1000)+time.time()))+".png"
        path = os.path.join(
            app.config['BASEDIR'], 'aunet/static/Uploads/News', filename)
        i.save(path, quality="96")
        with open(path, "rb") as f:
            data = f.read()
        data = base64.b64encode(data)  #
        data = str(data)
        data = data[2:-1]
        data = "data:image/jpg;base64,"+data
        img['src'] = data
        # return img
        image_num = image_num+1
        if image_num > 1:
            # remove extra images, only save the first image
            os.remove(path)
        else:
            imgUrlFirst = "static/Uploads/News/"+filename
    if image_num == 0:
        # the default image file
        imgUrlFirst = "static/Uploads/News/default.jpg"
    return soup, imgUrlFirst

# change imgurl into img and save it ,and save the path to the mysql


def dataurl_to_img(img_url):
    data = request.urlopen(img_url).read()
    img_buf = BytesIO(data)
    img = Image.open(img_buf)
    filename = str(int(random.uniform(1, 1000)+time.time()))+".png"
    path = os.path.join(
        app.config['BASEDIR'], 'aunet/static/Uploads/News', filename)
    img.save(path, quality="192")
    return 'static/Uploads/News/'+filename


class SilderShowClass(Resource):

    @marshal_with(SilderShow_fields)
    def get(self):
        permission = Permission(ActionNeed(('查看新闻')))
        if permission.can() is not True:
            abort_if_unauthorized("查看新闻")
        silder_shows = SilderShow.query.all()
        return silder_shows

    def post(self):
        request_arg = RequestMethod_parser.parse_args()
        requestMethod = request_arg['requestMethod']
        if requestMethod == "POST":
            permission = Permission(ActionNeed('添加新闻'))
            if permission.can() is not True:
                abort_if_unauthorized("添加新闻")
            args = SilderShow_parser.parse_args()
            title = args['title']
            imgUrl = args['imgUrl']
            imgUrl = dataurl_to_img(imgUrl)
            outline = args['outline']
            link = args['link']
            silder_show = SilderShow(title, imgUrl, outline, link)
            db.session.add(silder_show)
            db.session.commit()
        else:
            abort(404, message="api not found")


class SliderShowSpec(Resource):

    @marshal_with(SilderShow_fields)
    def get(self, id):
        permission = Permission(ActionNeed(('查看新闻')))
        if permission.can() is not True:
            abort_if_unauthorized("查看新闻")
        silder_show = SilderShow.query.filter(SilderShow.id == id).first()
        abort_if_not_exist(silder_show, "silder_show")
        return silder_show

    def post(self, id):
        request_arg = RequestMethod_parser.parse_args()
        requestMethod = request_arg['requestMethod']
        if requestMethod == "PUT":
            permission = Permission(ActionNeed('修改新闻'))
            if permission.can()is not True:
                abort_if_unauthorized("修改新闻")
            silder_show = SilderShow.query.filter(SilderShow.id == id).first()
            abort_if_not_exist(silder_show, "silder_show")
            args = SilderShowSpec_parser.parse_args()
            title = args['title']
            imgUrl = args['imgUrl']
            try:
                imgUrl = dataurl_to_img(imgUrl)
            except:
                imgUrl = args['imgUrl']
            outline = args['outline']
            editable = args['editable']
            link = args['link']
            if title != None:
                silder_show.title = title
            if imgUrl != None:
                silder_show.img_url = imgUrl
            if outline != None:
                silder_show.outline = outline
            if editable != None:
                silder_show.editable = editable
            if link != None:
                silder_show.link = link
            db.session.add(silder_show)
            db.session.commit()
        elif requestMethod == "DELETE":
            permission = Permission(ActionNeed('删除新闻'))
            if permission.can()is not True:
                abort_if_unauthorized("删除新闻")
            silder_show = SilderShow.query.filter(SilderShow.id == id).first()
            abort_if_not_exist(silder_show, "silder_show")
            db.session.delete(silder_show)
            db.session.commit()
        else:
            abort(404, message="api not found")


class NewsClass(Resource):

    @marshal_with(News_fields)
    def get(self):
        permission = Permission(ActionNeed(('查看新闻')))
        if permission.can() is not True:
            abort_if_unauthorized("查看新闻")
        news = News.query.all()
        return news

    def post(self):
        request_arg = RequestMethod_parser.parse_args()
        requestMethod = request_arg['requestMethod']
        if requestMethod == "POST":
            permission = Permission(ActionNeed('添加新闻'))
            if permission.can()is not True:
                abort_if_unauthorized("添加新闻")
            args = News_parser.parse_args()
            category = args['category']
            detail = args['detail']
            title = args['title']
            tags = args['tags']
            try:
                tags = list(eval(tags[0]))
            except:
                pass
            soup, imgUrlFirst = handle_html(detail)
            outline = soup.get_text()[:80]
            news = News(soup.prettify(), title, outline, imgUrlFirst)
            db.session.add(news)
            db.session.commit()
            news.addCategory(category)
            for tag in tags:
                t = Tag.query.filter_by(name=tag).first()
                abort_if_not_exist(t, "tag")
                news.tags.append(t)
            db.session.add(news)
            db.session.commit()
        else:
            abort(404, message="api not found")


class NewsSpec(Resource):

    @marshal_with(NewsSpec_fields)
    def get(self, id):
        permission = Permission(ActionNeed(('查看新闻')))
        if permission.can() is not True:
            abort_if_unauthorized("查看新闻")
        news = News.query.filter(News.id == id).first()
        abort_if_not_exist(news, "news")
        return news

    def post(self, id):
        request_arg = RequestMethod_parser.parse_args()
        requestMethod = request_arg['requestMethod']
        if requestMethod == "PUT":
            permission = Permission(ActionNeed('修改新闻'))
            if permission.can()is not True:
                abort_if_unauthorized("修改新闻")
            news = News.query.filter(News.id == id).first()
            abort_if_not_exist(news, "news")
            args = NewsSpec_parser.parse_args()
            category = args['category']
            detail = args['detail']
            title = args['title']
            editable = args['editable']
            tags = args['tags']
            try:
                tags = list(eval(tags[0]))
            except:
                pass
            if category != None:
                news.category = []
                news.addCategory(category)
            if detail != None:
                news.detail = detail
                soup, imgUrlFirst = handle_html(detail)
                news.img_url = imgUrlFirst
                outline = soup.get_text()[:80]
                news.outline = outline

            if title != None:
                news.title = title

            if editable != None:
                news.editable = editable
            if tags != None:
                news.tags = []
                for tag in tags:
                    news.addTag(tag)
            db.session.add(news)
            db.session.commit()
        elif requestMethod == "DELETE":
            permission = Permission(ActionNeed('删除新闻'))
            if permission.can()is not True:
                abort_if_unauthorized("删除新闻")

            news = News.query.filter(News.id == id).first()
            abort_if_not_exist(news, "news")
            db.session.delete(news)
            db.session.commit()
        else:
            abort(404, message="api not found")


class NewsSpecDetail(Resource):

    def get(self, id):
        # id=int(id)
        news = News.query.filter(News.id == id).first()
        abort_if_not_exist(news, "news")
        data = dict()
        data['detail'] = news.detail
        return data


class Categorys(Resource):

    def get(self):
        permission = Permission(ActionNeed(('查看新闻栏目')))
        if permission.can() is not True:
            abort_if_unauthorized("查看新闻栏目")
        categorys = Category.query.all()
        datas = list()
        for category in categorys:
            data = dict()
            data['name'] = category.name
            data['id'] = category.id
            datas.append(data)
        return datas

    def post(self):
        request_arg = RequestMethod_parser.parse_args()
        requestMethod = request_arg['requestMethod']
        if requestMethod == "POST":
            permission = Permission(ActionNeed("添加新闻属性"))
            if permission.can()is not True:
                abort_if_unauthorized("添加新闻属性")
            args = parser.parse_args()
            name = args['name']
            c = Category.query.filter(Category.name == name).first()
            abort_if_exist(c, "category")
            category = Category(name)
            db.session.add(category)
            db.session.commit()
        else:
            abort(404, message="api not found")


class CategoryClass(Resource):

    def get(self, id):
        permission = Permission(ActionNeed(('查看新闻栏目')))
        if permission.can() is not True:
            abort_if_unauthorized("查看新闻栏目")
        category = Category.query.filter_by(id=id).first()
        abort_if_not_exist(category, "category")
        data = dict()
        data['name'] = category.name
        data['id'] = category.id
        return data

    def post(self, id):
        request_arg = RequestMethod_parser.parse_args()
        requestMethod = request_arg['requestMethod']
        if requestMethod == "PUT":
            permission = Permission(ActionNeed('修改新闻属性'))
            if permission.can()is not True:
                abort_if_unauthorized("修改新闻属性")

            category = Category.query.filter(Category.id == id).first()
            abort_if_not_exist(category, "category")
            args = parser_spec.parse_args()
            name = args['name']
            if name != None and name != category.name:
                c = Category.query.filter(Category.name == name).first()
                abort_if_exist(c, "category")
                category.name = name
            db.session.add(category)
            db.session.commit()
        elif requestMethod == "DELETE":
            permission = Permission(ActionNeed('删除新闻属性'))
            if permission.can()is not True:
                abort_if_unauthorized("删除新闻属性")
            id = int(id)
            category = Category.query.filter(Category.id == id).first()
            abort_if_not_exist(category, "category")
            db.session.delete(category)
            db.session.commit()
        else:
            abort(404, message="api not found")


class Tags(Resource):

    def get(self):
        permission = Permission(ActionNeed(('查看新闻标签')))
        if permission.can() is not True:
            abort_if_unauthorized("查看新闻标签")
        tags = Tag.query.all()
        datas = list()
        for tag in tags:
            data = dict()
            data['name'] = tag.name
            data['id'] = tag.id
            datas.append(data)
        return datas

    def post(self):
        request_arg = RequestMethod_parser.parse_args()
        requestMethod = request_arg['requestMethod']
        if requestMethod == "POST":
            permission = Permission(ActionNeed('修改新闻标签'))
            if permission.can()is not True:
                abort_if_unauthorized("修改新闻标签")
            args = parser.parse_args()
            name = args['name']
            t = Tag.query.filter(Tag.name == name).first()
            abort_if_exist(t, "tag")
            tag = Tag(name)
            db.session.add(tag)
            db.session.commit()
        else:
            abort(404, message="api not found")


class TagClass(Resource):

    def get(self, id):
        permission = Permission(ActionNeed(('查看新闻标签')))
        if permission.can() is not True:
            abort_if_unauthorized("查看新闻标签")
        tag = Tag.query.filter_by(id=id).first()
        abort_if_not_exist(tag, "tag")
        data = dict()
        data['name'] = tag.name
        data['id'] = tag.id
        return data

    def post(self, id):
        request_arg = RequestMethod_parser.parse_args()
        requestMethod = request_arg['requestMethod']
        if requestMethod == "PUT":
            permission = Permission(ActionNeed('修改新闻标签'))
            if permission.can()is not True:
                abort_if_unauthorized("修改新闻标签")
            tag = Tag.query.filter(Tag.id == id).first()
            abort_if_not_exist(tag, "tag")
            args = parser_spec.parse_args()
            name = args['name']
            if name != None and name != tag.name:
                t = Tag.query.filter(Tag.name == name).first()
                abort_if_exist(t, "tag")
                tag.name = name
            db.session.add(tag)
            db.session.commit()
        elif requestMethod == "DELETE":
            permission = Permission(ActionNeed('删除新闻标签'))
            if permission.can()is not True:
                abort_if_unauthorized("删除新闻标签")
            tag = Tag.query.filter(Tag.id == id).first()
            abort_if_not_exist(tag, "tag")
            db.session.delete(tag)
            db.session.commit()
        else:
            abort(404, message="api not found")
