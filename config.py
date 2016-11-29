# -*-coding:utf-8 -*-
import os
BASEDIR=os.path.abspath(os.path.dirname(__file__))
# flask-wtf配置
CSRF_ENABLED = True
SECRET_KEY = 'May AU forever'

#sqlalchemy配置
SQLALCHEMY_DATABASE_URI='mysql+pymysql://root:abc201314@localhost/aunet_flask'#mysql的配置
SQLALCHEMY_MIGRATE_REPO = os.path.join(BASEDIR, 'db_repository')

SQLALCHEMY_POOL_RECYCLE=15
SQLALCHEMY_POOL_SIZE=15
SQLALCHEMY_TRACK_MODIFICATIONS=True

DEBUG=True


MAIL_SERVER='smtp.qq.com'#邮箱服务器
MAIL_PORT=465
MAIL_USE_SSL=True
MAIL_USERNAME=''#如果是qq邮箱则为qq号，136邮箱同理
MAIL_PASSWORD=''#客户端密码
MAIL_USE_TLS = False
MAIL=('sicun','1412511544@qq.com')