# -*-coding:utf-8 -*-
from .. import db
from datetime import datetime
from flask_login import current_user


news_category = db.Table("news_category",
                         db.Column(
                             'news_id', db.Integer, db.ForeignKey("news.id")),
                         db.Column(
                             'category_id', db.Integer, db.ForeignKey("category.id")),
                         db.Column(
                             "created_at", db.DateTime, default=datetime.now)
                         )

news_tag = db.Table("news_tag",
                    db.Column("news_id", db.Integer, db.ForeignKey("news.id")),
                    db.Column("tag_id", db.Integer, db.ForeignKey("tag.id")),
                    db.Column("created_at", db.DateTime, default=datetime.now),
                    )


class News(db.Model):
    __tablename__ = "news"
    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer)
    month = db.Column(db.Integer)
    day = db.Column(db.Integer)
    post_time = db.Column(db.DateTime)
    detail = db.Column(db.Text)
    title = db.Column(db.String(80))
    outline = db.Column(db.Text)
    img_url = db.Column(db.String(50))
    editable = db.Column(db.Boolean)
    author = db.Column(db.String(40))
    category = db.relationship(
        "Category", secondary=news_category, backref=db.backref('news', lazy="dynamic"))
    tags = db.relationship(
        "Tag", secondary=news_tag, backref=db.backref('news', lazy="dynamic"))

    def addCategory(self, categoryName):
        category = Category.query.filter(Category.name == categoryName).first()
        self.category.append(category)

    def addTag(self, tagName):
        tag = Tag.query.filter(Tag.name == tagName).first()
        self.tags.append(tag)

    @property
    def cate(self):
        return self.category[0].name

    def __init__(self, news_Detail, news_Title, news_Outline, news_Img_Url):
        time = datetime.utcnow()
        self.post_time = time
        self.year = time.year
        self.month = time.month
        self.day = time.day
        self.detail = news_Detail
        self.title = news_Title
        self.outline = news_Outline
        # self.img_url=news_Img_Url
        self.img_url = news_Img_Url
        self.editable = True
        if current_user == None:
            self.author = "匿名"
        else:
            self.author = current_user.userName

    def __str__(self):
        return "Title:%s" % self.title
    __repr__ = __str__


class Category(db.Model):
    __tablename__ = "category"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True)
    remark = db.Column(db.String(30))

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "category_name:%s" % self.name
    __repr__ = __str__


class Tag(db.Model):
    __tablename__ = "tag"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True)

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "tag_name:%s" % self.name

    __repr__ = __str__


class SilderShow(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    img_url = db.Column(db.String(80))
    outline = db.Column(db.Text)
    post_time = db.Column(db.DateTime)
    link = db.Column(db.String(80))
    editable = db.Column(db.Boolean)

    def __init__(self, title, img_Url, outline, link):
        self.title = title
        self.img_url = img_Url
        self.outline = outline
        self.link = link
        self.editable = 1
        self.post_time = datetime.utcnow()

    def __str__(self):
        return self.title
    __repr__ = __str__
