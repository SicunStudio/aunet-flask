# -*-coding:utf-8 -*-
from flask import render_template, flash, redirect, url_for, g, session, request, current_app
from flask_login import login_required, login_user, logout_user

from datetime import datetime, timedelta
from flask import jsonify
import json


from . import home
from .models import News, Category, Tag, SilderShow, news_category
from aunet import app


# used in template to format time
# usage : '|time'
@app.template_filter('time')
def time_filter(s):
    if isinstance(s, datetime) is True:
        now = datetime.now()
        utc_now = datetime.utcnow()
        return (s-(utc_now-now)).strftime('%Y %b %d %H:%M')
    elif (isinstance(s, str)):
        now = datetime.now()
        utc_now = datetime.utcnow()
        s = datetime.strptime(s, "%Y-%m-%d %H:%M:%S")
        s = s-(utc_now-now)
        return s.strftime("%Y %b %d %H:%M")


@home.route('/', methods=["POST", "GET"])
@home.route('/index', methods=["POST", "GET"])
def index():
    silder_show = SilderShow.query.order_by(
        SilderShow.post_time.desc()).limit(5).all()
    CharmAssociation = getNews(1, "魅力社团")  # charm_association
    LatestNotice = getNews(1, "通知")
    LatestAdvanceNotice = getNews(1, "预告")
    NewsPinPai = getNews(1, "品牌活动")
    NewsCharmHust = getNews(1, "魅力华科")
    NewsYuLan = getNews(2, "新闻")
    return render_template("Home/index/index.html", SilderShow=silder_show, CharmAssociation=CharmAssociation, LatestNotice=LatestNotice, LatestAdvanceNotice=LatestAdvanceNotice, NewsPinPai=NewsPinPai,
                           NewsCharmHust=NewsCharmHust, NewsYuLan=NewsYuLan)


@home.route('/news/<int:id>', methods=["POST", "GET"])
def show_News(id):
    news = News.query.filter(News.id == id).first()
    return render_template("Home/news/detail.html", news=news)


@home.route('/news', methods=["POST", "GET"])
def indexNews():
    return render_template("Home/news/index.html")


@home.route('/au_card', methods=['GET'])
def au_card():
    return render_template('Home/PartnerInfo/PartnerInfo.html')


def getNews(number, category):
    news = News.query.join(news_category).join(Category).filter(
        Category.name == category).order_by(News.post_time).limit(number).all()
    return news


# change news objects into json
def news2Json(news, length, page, news_number):
    newsJson = dict()
    newsJson['title'] = list()
    newsJson['outline'] = list()
    newsJson['img_url'] = list()
    newsJson['post_time'] = list()
    newsJson['length'] = length
    newsJson['news_number'] = news_number
    newsJson['current_page'] = str(page)
    newsJson['id'] = list()
    i = 0
    for new in news:
        now = datetime.now()
        utc_now = datetime.utcnow()
        newsJson['title'].append(dict({i: new.title}))
        newsJson['outline'].append(dict({i: new.outline}))
        newsJson['img_url'].append(dict({i: new.img_url}))
        newsJson['post_time'].append(
            dict({i: (new.post_time-(utc_now-now)).strftime('%Y %b %d %H:%M')}))
        newsJson['id'].append(dict({i: new.id}))
        i = i+1
    return newsJson


#/news page to load news by ajax
@home.route('/news/news2Json', methods=["POST", "GET"])
def newJson():
    if request.method == 'POST':
        get_dict = request.get_json()
        now = datetime.now()
        category = get_dict['Category']
        time = get_dict['Time']
        sort = get_dict['Sort']
        goto_page = get_dict['gotoPage']
        goto_page = int(goto_page)
        if time == "all":
            time = now-timedelta(days=365*10)
        elif time == "week":
            time = now - timedelta(days=7)
        elif time == "month":
            time = now - timedelta(days=90)
        elif time == "year":
            time = now-timedelta(days=365)

        if(category == "all" and (sort == "all" or sort == "hot" or sort == "latest")):
            news = News.query.filter(News.post_time > time).order_by(
                News.post_time.desc()).all()
            news_number = len(news)
            news = news[(goto_page-1)*10:goto_page*10]
        elif(category == "all" and sort == "oldest"):
            news = News.query.filter(
                News.post_time > time).order_by(News.post_time).all()
            news_number = len(news)
            news = news[(goto_page-1)*10:goto_page*10]
        elif(category != "all" and (sort == "all" or sort == "hot" or sort == "latest")):
            news = News.query.join(news_category).join(Category).filter(News.post_time > time).filter(
                Category.name == category).order_by(News.post_time.desc()).all()
            news_number = len(news)
            news = news[(goto_page-1)*10:goto_page*10]
        elif(category != "all" and sort == "oldest"):
            news = News.query.join(news_category).join(Category).filter(
                News.post_time > time, Category.name == category).order_by(News.post_time).all()
            news_number = len(news)
            news = news[(goto_page-1)*10:goto_page*10]
        else:
            news = None
        if news != None:
            NewsJson = news2Json(news, len(news), goto_page, news_number)
            return jsonify(NewsJson)
        else:
            return "<html><body>bad</body></html>"
    return "bad method"
