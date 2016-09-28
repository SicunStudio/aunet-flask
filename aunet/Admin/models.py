from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from .. import lm,db

from datetime import datetime


class User(db.Model,UserMixin):
	id = db.Column(db.Integer, primary_key=True)
	userName = db.Column(db.String(64), unique=True, index=True)
	passWord =db.Column(db.String(128))
	email=db.Column(db.String(40))
	lock=db.Column(db.Boolean)
	remark=db.Column(db.String(20))
	

	def verify_password(self, passWord):
        return check_password_hash(self.passWord, passWord)	
    def get_id(self):
    	return self.id
    def __init__(self,uerName,passWord,email,remark):
    	self.uerName=userName
    	self.passWord=generate_password_hash(passWord)
    	self.email=email
    	self.remark=remark

    def __str__(self):
    	return self.userName


class LoginLog(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	userName= db.Column(db.String(64))
	loginTime=db.Column(db.DateTime)
	loginIp=db.Column(db.String(20))

	def __init__(self,userName,loginTime,loginIp):
		self.userName=userName
		self.loginTime=loginTime
		self.loginIP=loginIp
	def __str__(self):
		return self.userName

class Role(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	roleName=db.Column(db.String(20),unique=True)
	status=db.Column(db.Boolean)
	remark=db.Column(db.String(20))



class Node(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	nodeName=db.Column(db.String(20),unique=True)
	remark=db.Column(db.String(20))	
	status=db.Column(db.Boolean)
	level=db.Column(db.Integer)
