#-*-coding:utf-8-*-
# 导入各扩展
from flask import Flask,session
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_restful import Api,Resource
from flask_login import LoginManager
from flask_principal import Principal
import pymysql
from datetime import timedelta


# from .Api.common.common import errors



app=Flask(__name__)#创建应用
app.config.from_object('config')#导入配置
try:
	app.config.from_object('secret_config')#导入secret配置
except:
	pass
# 实例化各扩展
db=SQLAlchemy(app)
# api=Api(app,errors=errors)
api=Api(app)

principals=Principal(app)

lm=LoginManager()
lm.init_app(app)
lm.login_view='getApp'

#设置flask的session和cookit的过期时间
app.permanent_session_lifetime = timedelta(hours=6)
lm.remember_cookie_duration=timedelta(hours=6)


mail=Mail(app)

#注册蓝图
from .Admin import admin
app.register_blueprint(admin,url_prefix='/admin')

from .Home import home
app.register_blueprint(home)

from .Material import material
app.register_blueprint(material)


from . import models,views

