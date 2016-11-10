# -*- coding: utf-8 -*-
from flask_restful import reqparse, abort,Resource,fields,marshal_with
from werkzeug.security import generate_password_hash
from datetime import datetime

from aunet.Admin.models import User,Node,Role,LoginLog
from aunet import db
from .models import EditUserPermission,EditUserNeed

from flask_login import current_user

from flask_principal import RoleNeed,UserNeed,ActionNeed
from flask_principal import Identity, AnonymousIdentity, \
     identity_changed,Permission


Node_fields={
	"nodeName":fields.String,
	"status":fields.Boolean,
	"level":fields.Integer
}

User_parser=reqparse.RequestParser()			# User zhong method post de parser
User_parser.add_argument('userName',type=str,required =True,location="json",help="userName is needed")
User_parser.add_argument('passWord',type=str,required =True,location="json",help="passWord is needed")
User_parser.add_argument('email',type=str,location="json",help="email is needed",required=True)
User_parser.add_argument('roleName',type=str,required =True,location="json",action="append",help="roleName is needed")

User1_parser=reqparse.RequestParser()			#User1 zhong method post de parser
User1_parser.add_argument('email',type=str,location="json")
User1_parser.add_argument('passWord',type=str,location="json")
User1_parser.add_argument('roleName',type=str,location="json",action="append")
User1_parser.add_argument('userName',type=str,location="json")
User1_parser.add_argument('status',type=bool,location="json")


NodeSpec_parser=reqparse.RequestParser()
NodeSpec_parser.add_argument('status',type=int,help="status type is int")

Role_parser=reqparse.RequestParser()
Role_parser.add_argument('roleName',type=str,location="json",required=True,help="roleName is needed")
Role_parser.add_argument("nodeName",type=str,location="json",required=True,action="append",help="remark is needed")

RoleSpec_parser=reqparse.RequestParser()
RoleSpec_parser.add_argument('roleName',type=str,location="json")
RoleSpec_parser.add_argument('nodeName',type=str,action="append",location="json")
RoleSpec_parser.add_argument('status',type=bool,location="json")


def abort_if_not_exist(data,message):
	if data==None:
		abort(404,message="{}  Found".format(message))

def abort_if_exist(data,message):
	if data!=None:
		abort(400,message="{} has existed ,please try another".format(message))

def abort_if_unauthorized(message):
	abort(401,message="{} permission Unauthorized".format(message))



class Users(Resource):
	def get(self):
		datas=list()
		data=dict()
		users=User.query.all()
		for user in users:
			log=LoginLog.query.filter(LoginLog.userName==user.userName).order_by(LoginLog.id.desc()).first()
			if log !=None:
				data['loginIp']=log.loginIp
				data['loginTime']=log.loginTime.timestamp()
			else:
				data['loginIp']=None
				data['loginTime']=None
			data['userName']=user.userName
			data['status']=user.status
			data['email']=user.email
			data['roles']=list()
			data['nodes']=list()
			for role in user.roles:
				for node in role.nodes:
					n=dict()
					n['nodeName']=node.nodeName
					n['status']=node.status
					n['level']=node.level
					data['nodes'].append(n)
				r=dict()
				r['roleName']=role.roleName
				r['status']=role.status
				data['roles'].append(r)
			datas.append(data)
		return datas
	def post(self):
		permission=Permission(ActionNeed('添加用户'))
		if permission.can()is not True:
			abort_if_unauthorized("添加用户")
		args=User_parser.parse_args()
		userName=args['userName']
		passWord=args['passWord']
		email=args['email']
		roleName=args['roleName']
		user1=User.query.filter(User.userName==userName).first()
		abort_if_exist(user1,"userName")
		user=User(userName,passWord,email)
		for name in roleName:
			role=Role.query.filter(Role.roleName==name).first()
			abort_if_not_exist(role,"role")
			user.roles.append(role)
		db.session.add(user)
		db.session.commit()

class CurrentUser(Resource):
	def get(self):
		user=current_user
		abort_if_not_exist(user,"user")
		log=LoginLog.query.filter(LoginLog.userName==user.userName).order_by(LoginLog.id.desc()).first()
		data=dict()
		if log !=None:
			data['loginIp']=log.loginIp
			data['loginTime']=log.loginTime.timestamp()
		else:
			data['loginIp']=None
			data['loginTime']=None
		data['userName']=user.userName
		data['status']=user.status
		data['email']=user.email
		data['roles']=list()
		data['nodes']=list()
		for role in user.roles:
			for node in role.nodes:
				n=dict()
				n['nodeName']=node.nodeName
				n['status']=node.status
				n['level']=node.level
				data['nodes'].append(n)
			r=dict()
			r['roleName']=role.roleName
			r['status']=role.status
			data['roles'].append(r)
		return data

class UserSpec(Resource):			
	def get(self,id):

		user=User.query.filter(User.id==id).first()
		abort_if_not_exist(user,"user")
		log=LoginLog.query.filter(LoginLog.userName==user.userName).order_by(LoginLog.id.desc()).first()
		data=dict()
		if log !=None:
			data['loginIp']=log.loginIp
			data['loginTime']=log.loginTime.timestamp()
		else:
			data['loginIp']=None
			data['loginTime']=None
		data['userName']=user.userName
		data['status']=user.status
		data['email']=user.email
		data['roles']=list()
		data['nodes']=list()
		for role in user.roles:
			for node in role.nodes:
				n=dict()
				n['nodeName']=node.nodeName
				n['status']=node.status
				n['level']=node.level
				data['nodes'].append(n)
			r=dict()
			r['roleName']=role.roleName
			r['status']=role.status
			data['roles'].append(r)
		return data


	def put(self,id):
		if current_user.is_anonymous==True:
			abort_if_unauthorized("修改用户")
		permission=Permission(ActionNeed("修改用户"))
		
		if (permission.can()is not True) and (permission1.can()is not True):
			abort_if_unauthorized("修改用户")

		user=User.query.filter(User.id==id).first()
		abort_if_not_exist(user,"user")
		args=User1_parser.parse_args()
		# userId=args['userId']
		status=args['status']
		email=args['email']
		passWord=args['passWord']
		roleName=args['roleName']
		userName=args['userName']
		user1=User.query.filter(User.userName==userName).first()
		abort_if_exist(user1,"userName")
		if status!=None and permission.can():
			user.status=status
		if email!=None:
			user.email=email
		if passWord!=None:
			user.passWord=generate_password_hash(passWord)
		if roleName!=None and permission.can():
			r=list()
			for name in roleName:
				role=Role.query.filter(Role.roleName==name).first()
				abort_if_not_exist(role,"role")
				r.append(role)
			user.role=r
		if userName!=None:
			user.userName=userName
		db.session.add(user)
		db.session.commit()



	def delete(self,id):
		permission=Permission(ActionNeed("删除用户"))
		if permission.can()is not True:
			abort_if_unauthorized("删除用户")
		user=User.query.filter(User.id==id).first()
		abort_if_not_exist(user,"user")
		db.session.delete(user)
		db.session.commit()



class Nodes(Resource):	
	@marshal_with(Node_fields)
	def get(self):						
		nodes=Node.query.all()
		return nodes


class NodeSpec(Resource):
	@marshal_with(Node_fields)
	def get(self,id):

		node=Node.query.filter(Node.id==id).first()
		abort_if_not_exist(node,"node")
		return node

	def put(self,id):
		permission=Permission(ActionNeed("修改节点"))
		if permission.can()is not True:
			abort_if_unauthorized("修改节点")

		node=Node.query.filter(Node.id==id).first()
		abort_if_not_exist(node,"node")
		args=NodeSpec_parser.parse_args()
		status=args['status']
		if status !=None:
			node.status=status
		db.session.add(node)
		db.session.commit()

class Roles(Resource):
	def get(self):
		roles=Role.query.all()
		datas=list()
		for role in roles:
			data=dict()
			data['roleName']=role.roleName
			data['status']=role.status
			data['nodes']=list()
			for node in role.nodes:
				n=dict()
				n['nodeName']=node.nodeName
				n['status']=node.status
				n['level']=node.level
				data['nodes'].append(n)
			datas.append(data)
		return datas

	def post(self):
		permission=Permission(ActionNeed('添加角色'))
		if permission.can()is not True:
			abort_if_unauthorized("添加角色")
		args=Role_parser.parse_args()
		roleName=args['roleName']
		nodeName=args['nodeName']
		role1=Role.query.filter(Role.roleName==roleName).first()
		abort_if_exist(role1,"roleName")
		role=Role(roleName)
		db.session.add(role)
		db.session.commit()
		for name in nodeName:
			node=Node.query.filter(Node.nodeName==name).first()
			abort_if_not_exist(node,"node")
			role.nodes.append(node)
		db.session.add(role)
		db.session.commit()

class RoleSpec(Resource):
	def get(self,id):

		role=Role.query.filter(Role.id==id).first()
		abort_if_not_exist(role,"role")
		data=dict()
		data['roleName']=role.roleName
		data['status']=role.status
		data['nodes']=list()
		for node in role.nodes:
			n=dict()
			n['nodeName']=node.nodeName
			n['status']=node.status
			n['level']=node.level
			data['nodes'].append(n)
		return data

	def put(self,id):
		permission=Permission(ActionNeed('修改角色'))
		if permission.can()is not True:
			abort_if_unauthorized("修改角色")
	
		role=Role.query.filter(Role.id==id).first()
		abort_if_not_exist(role,"role")
		args=RoleSpec_parser.parse_args()
		roleName=args['roleName']
		nodeName=args['nodeName']
		status=args['status']
		if roleName!=None:
			r=Role.query.filter_by(roleName=roleName).first()
			abort_if_exist(r,"rolename")
			role.roleName=roleName
		if status!=None:
			role.status=status
		if nodeName!=None:
			n=list()
			for name in nodeName:
				node=Node.query.filter(Node.nodeName==name).first()
				abort_if_not_exist(node,"node")
				n.append(node)
			role.nodes=n

		db.session.add(role)
		db.session.commit()

	def delete(self,id):
		permission=Permission(ActionNeed('删除角色'))
		if permission.can()is not True:
			abort_if_unauthorized("删除角色")

		role=Role.query.filter(Role.id==id).first()
		abort_if_not_exist(role,"role")
		db.session.delete(role)
		db.session.commit()

