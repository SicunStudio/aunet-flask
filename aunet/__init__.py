#-*-coding:utf-8-*-
# 导入各扩展
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_restful import Api,Resource
from flask_login import LoginManager
import pymysql

# from .Api.common.common import errors



app=Flask(__name__)#创建应用
app.config.from_object('config')#导入配置

# 实例化各扩展
db=SQLAlchemy(app)
# api=Api(app,errors=errors)
api=Api(app)



lm=LoginManager()
lm.init_app(app)
lm.login_view='admin.login'

mail=Mail(app)

#注册蓝图
from .Admin import admin
app.register_blueprint(admin,url_prefix='/admin')

from .Home import home
app.register_blueprint(home)

from .Api import dashboard
app.register_blueprint(dashboard,url_prefix='/dashboard')



from . import models,views

