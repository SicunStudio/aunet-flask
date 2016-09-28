# -*-coding:utf-8 -*-
import os
basedir=os.path.abspath(os.path.dirname(__file__))
# flask-wtf配置
CSRF_ENABLED = True
SECRET_KEY = 'May AU forever'

#sqlalchemy配置
SQLALCHEMY_DATABASE_URI='mysql+pymysql://root:abc201314@localhost/aunet_flask'#mysql的配置
SQLALCHEMY_POOL_RECYCLE=15
SQLALCHEMY_POOL_SIZE=15
SQLALCHEMY_TRACK_MODIFICATIONS=True