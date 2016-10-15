from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from .. import lm,db

from datetime import datetime



role_node = db.Table('role_node',  # 角色权限关联表  
    db.Column('node_id', db.Integer, db.ForeignKey('node.id')),
    db.Column('role_id', db.Integer, db.ForeignKey('role.id')),
    db.Column('created_at', db.DateTime, default=datetime.now)
    )

user_role=	db.Table('user_role',	#用户角色关联表
	db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('role_id', db.Integer, db.ForeignKey('role.id')),
    db.Column('created_at', db.DateTime, default=datetime.now)
	)



class User(db.Model,UserMixin):
	__tablename__="user"
	id = db.Column(db.Integer, primary_key=True)
	userName = db.Column(db.String(64), unique=True, index=True)
	passWord =db.Column(db.String(128))
	email=db.Column(db.String(40))
	status=db.Column(db.Boolean)
	remark=db.Column(db.String(20))
	role=db.relationship("Role",secondary=user_role,backref=db.backref('users',lazy="dynamic"))


	def verify_password(self, passWord):
		return check_password_hash(self.passWord,passWord)

	def get_id(self):
		return self.id
  	
    # def get_id(self):
    #     return str(self.id)  # python 3

	@property
	def nodes(self):
		node=[]
		for r in self.role:
			node=node+r.nodes
		return node



    
	def __init__(self,userName,passWord,email,roleName):
		self.userName = userName
		self.passWord = generate_password_hash(passWord)
		self.email=email
		r=Role.query.filter(Role.roleName==roleName).first()
		self.role.append(r)
		self.remark=r.remark
		self.status=1

    	#self.role=Role.query.filter(Role.roleName==roleName).first()

	def __str__(self):
   		return self.userName

	__repr__ = __str__




class LoginLog(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	userName= db.Column(db.String(64))
	loginTime=db.Column(db.String(25))
	loginIp=db.Column(db.String(20))

	def __init__(self,userName,loginTime,loginIp):
		self.userName=userName
		self.loginTime=loginTime
		self.loginIP=loginIp
	def __str__(self):
		return self.userName
	__repr__ = __str__

class Role(db.Model):
	__tablename__="role"
	id = db.Column(db.Integer, primary_key=True)
	roleName=db.Column(db.String(20),unique=True)
	status=db.Column(db.Boolean)
	remark=db.Column(db.String(20))
	nodes=db.relationship("Node",secondary=role_node,backref=db.backref('roles',lazy="dynamic"))

	def addNode(self,nodeId):
		n=Node.query.filter(Node.id==nodeId).first()
		self.nodes.append(n)
		

	def __init__(self,roleName,remark):
		self.roleName=roleName
		self.remark=remark
		self.status=1

	def __str__(self):
		return self.roleName

	__repr__ = __str__


class Node(db.Model):
	__tablename__="node"
	id = db.Column(db.Integer, primary_key=True)
	nodeName=db.Column(db.String(20),unique=True)
	remark=db.Column(db.String(20))	
	status=db.Column(db.Boolean)
	level=db.Column(db.Integer)


	def __init__(self,nodeName,remark,level):
		self.nodeName=nodeName
		self.remark=remark
		self.status=1
		self.level=level

	def __str__(self):
		return self.nodeName

	__repr__ = __str__

