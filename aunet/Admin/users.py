
from flask_restful import reqparse, abort,Resource,fields,marshal_with
from werkzeug.security import generate_password_hash
from datetime import datetime
from flask import request
from aunet.Admin.models import User,Node,Role,LoginLog
from aunet import db
from .models import EditUserPermission,EditUserNeed,LoginLog

from flask_login import current_user

from flask_principal import RoleNeed,UserNeed,ActionNeed
from flask_principal import Identity, AnonymousIdentity, \
     identity_changed,Permission
import json

Node_fields={
	"id":fields.Integer,
	"nodeName":fields.String,
	"status":fields.Boolean,
	"level":fields.Integer
}

User_parser=reqparse.RequestParser()			# User zhong method post de parser
User_parser.add_argument('userName',type=str,required =True,location="json",help="userName is needed")
User_parser.add_argument('passWord',type=str,required =True,location="json",help="passWord is needed")
User_parser.add_argument('email',type=str,location="json",help="email is needed",required=True)
User_parser.add_argument('phone',type=str,location="json",help="phone is needed",required=True)
User_parser.add_argument('roleName',type=str,required =True,location="json",action="append",help="roleName is needed")

User1_parser=reqparse.RequestParser()		#User1 zhong method post de parser
User1_parser.add_argument('email',type=str,location="json")
User1_parser.add_argument('phone',type=str,location="json")
User1_parser.add_argument('passWord',type=str,location="json")
User1_parser.add_argument('roleName',type=str,location="json",action="append")
User1_parser.add_argument('userName',type=str,location="json")
User1_parser.add_argument('status',type=bool,location="json")



NodeSpec_parser=reqparse.RequestParser()
NodeSpec_parser.add_argument('status',type=int,help="status type is int")
NodeSpec_parser.add_argument('level',type=int,help="permission level")


Role_parser=reqparse.RequestParser()
Role_parser.add_argument('roleName',type=str,location="json",required=True,help="roleName is needed")
Role_parser.add_argument("nodeName",type=str,location="json",action="append",required=True,help="remark is needed")

RoleSpec_parser=reqparse.RequestParser()
RoleSpec_parser.add_argument('roleName',type=str,location="json")
RoleSpec_parser.add_argument('nodeName',action="append",type=str,location="json")
RoleSpec_parser.add_argument('status',type=bool,location="json")

RequestMethod_parser=reqparse.RequestParser()
RequestMethod_parser.add_argument('requestMethod',type=str,location='json')


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
		permission=Permission(ActionNeed(('查看用户')))
		if permission.can() is not True:
			abort_if_unauthorized("查看用户")
		datas=list()
		users=User.query.all()
		for user in users:
			data=dict()
			log=LoginLog.query.filter(LoginLog.userName==user.userName).order_by(LoginLog.id.desc()).first()
			if log !=None:
				data['loginIp']=log.loginIp
				data['loginTime']=log.loginTime.timestamp()
			else:
				data['loginIp']=None
				data['loginTime']=None
			data['userName']=user.userName
			data['phone']=user.phone
			data['status']=user.status
			data['email']=user.email
			data['id']=user.id
			data['roles']=list()
			data['nodes']=list()
			for role in user.roles:
				for node in role.nodes:
					n=dict()
					n['nodeName']=node.nodeName
					n['status']=node.status
					n['level']=node.level
					n['id']=node.id
					data['nodes'].append(n)
				r=dict()
				r['id']=role.id
				r['roleName']=role.roleName
				r['status']=role.status
				data['roles'].append(r)
			datas.append(data)
		return datas
	def post(self):
		request_arg=RequestMethod_parser.parse_args()
		requestMethod=request_arg['requestMethod']
		if requestMethod=="POST":
			permission=Permission(ActionNeed('添加用户'))
			if permission.can()is not True:
				abort_if_unauthorized("添加用户")
			args=User_parser.parse_args()
			try:
				args['roleName']=list(eval(args['roleName'][0]))
			except:
				pass
			userName=args['userName']
			passWord=args['passWord']
			email=args['email']
			roleName=args['roleName']
			phone=args['phone']
			user1=User.query.filter(User.userName==userName).first()
			abort_if_exist(user1,"userName")
			user=User(userName,passWord,email,phone)
			for name in roleName:
				role=Role.query.filter(Role.roleName==name).first()
				abort_if_not_exist(role,"role")
				user.roles.append(role)
			db.session.add(user)
			db.session.commit()
		else:
			abort(404,message="api not found")


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
		data['id']=user.id
		data['userName']=user.userName
		data['status']=user.status
		data['email']=user.email
		data['phone']=user.phone
		data['roles']=list()
		data['nodes']=list()
		for role in user.roles:
			for node in role.nodes:
				n=dict()
				n['id']=node.id
				n['nodeName']=node.nodeName
				n['status']=node.status
				n['level']=node.level
				data['nodes'].append(n)
			r=dict()
			r['id']=role.id
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
		data['id']=user.id
		data['userName']=user.userName
		data['status']=user.status
		data['email']=user.email
		data['phone']=user.phone
		data['roles']=list()
		data['nodes']=list()
		for role in user.roles:
			for node in role.nodes:
				n=dict()
				n['id']=node.id
				n['nodeName']=node.nodeName
				n['status']=node.status
				n['level']=node.level
				data['nodes'].append(n)
			r=dict()
			r['id']=role.id
			r['roleName']=role.roleName
			r['status']=role.status
			data['roles'].append(r)
		return data


	def post(self,id):
		request_arg=RequestMethod_parser.parse_args()
		requestMethod=request_arg['requestMethod']
		if requestMethod=="PUT":
			if current_user.is_anonymous==True:
				abort_if_unauthorized("修改用户")
			permission=Permission(ActionNeed("修改用户"))
			permission1=EditUserPermission(EditUserNeed(current_user.id))
			if (permission.can()is not True)and (permission1.can()is not True):
				abort_if_unauthorized("修改用户")

			user=User.query.filter(User.id==id).first()
			abort_if_not_exist(user,"user")
			args=User1_parser.parse_args()
			# userId=args['userId']
			status=args['status']
			email=args['email']
			phone=args['phone']
			passWord=args['passWord']
			roleName=args['roleName']
			userName=args['userName']
			if userName!=None and userName!=user.userName:
				user1=User.query.filter(User.userName==userName).first()
				abort_if_exist(user1,"userName")
				user.userName=userName
			
			if status!=None and permission.can():
				user.status=status
			if email!=None:
				user.email=email
			if phone!=None:
				user.phone=phone
			if passWord!=None:
				user.passWord=generate_password_hash(passWord)
			if roleName!=None and permission.can():
				try:
					roleName=list(eval(roleName[0]))
				except:
					pass
				r=list()
				for name in roleName:
					role=Role.query.filter(Role.roleName==name).first()
					abort_if_not_exist(role,"role")
					r.append(role)
				user.roles=r
			if userName!=None:
				user.userName=userName
			db.session.add(user)
			db.session.commit()
		elif requestMethod=="DELETE":
			permission=Permission(ActionNeed("删除用户"))
			if permission.can()is not True:
				abort_if_unauthorized("删除用户")
			user=User.query.filter(User.id==id).first()
			abort_if_not_exist(user,"user")
			db.session.delete(user)
			db.session.commit()
		else:
			abort(404,message="api not found")


class Nodes(Resource):	
	@marshal_with(Node_fields)
	def get(self):
		permission=Permission(ActionNeed(('查看权限节点')))
		if permission.can() is not True:
			abort_if_unauthorized("查看权限节点")						
		nodes=Node.query.all()
		return nodes


class NodeSpec(Resource):
	@marshal_with(Node_fields)
	def get(self,id):
		permission=Permission(ActionNeed(('查看权限节点')))
		if permission.can() is not True:
			abort_if_unauthorized("查看权限节点")	
		node=Node.query.filter(Node.id==id).first()
		abort_if_not_exist(node,"node")
		return node

	def post(self,id):
		request_arg=RequestMethod_parser.parse_args()
		requestMethod=request_arg['requestMethod']
		if requestMethod=="PUT":
			permission=Permission(ActionNeed("修改节点"))
			if permission.can()is not True:
				abort_if_unauthorized("修改节点")

			node=Node.query.filter(Node.id==id).first()
			abort_if_not_exist(node,"node")
			args=NodeSpec_parser.parse_args()
			status=args['status']
			level=args['level']
			print (level)
			if status !=None:
				node.status=status
			if level!=None:
				node.level=level
			db.session.add(node)
			db.session.commit()
		else:
			abort(404,message="api not found")

class Roles(Resource):
	def get(self):
		permission=Permission(ActionNeed(('查看角色')))
		if permission.can() is not True:
			abort_if_unauthorized("查看角色")
		roles=Role.query.all()
		datas=list()
		for role in roles:
			data=dict()
			data['id']=role.id
			data['roleName']=role.roleName
			data['status']=role.status
			data['nodes']=list()
			for node in role.nodes:
				n=dict()
				n['id']=node.id
				n['nodeName']=node.nodeName
				n['status']=node.status
				n['level']=node.level
				data['nodes'].append(n)
			datas.append(data)
		return datas

	def post(self):
		request_arg=RequestMethod_parser.parse_args()
		requestMethod=request_arg['requestMethod']
		print(requestMethod)
		if requestMethod=="POST":
			permission=Permission(ActionNeed('添加角色'))
			if permission.can()is not True:
				abort_if_unauthorized("添加角色")
			args=Role_parser.parse_args()
			roleName=args['roleName']
			try:
				nodeName=list(eval(args['nodeName'][0]))
			except:
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
		else:
			abort(404,message="api not found")

class RoleSpec(Resource):
	def get(self,id):
		permission=Permission(ActionNeed(('查看角色')))
		if permission.can() is not True:
			abort_if_unauthorized("查看角色")
		role=Role.query.filter(Role.id==id).first()
		abort_if_not_exist(role,"role")
		data=dict()
		data['roleName']=role.roleName
		data['status']=role.status
		data['id']=role.id
		data['nodes']=list()
		for node in role.nodes:
			n=dict()
			n['id']=node.id
			n['nodeName']=node.nodeName
			n['status']=node.status
			n['level']=node.level
			data['nodes'].append(n)
		return data

	def post(self,id):
		request_arg=RequestMethod_parser.parse_args()
		requestMethod=request_arg['requestMethod']
		if requestMethod=="PUT":
			permission=Permission(ActionNeed('修改角色'))
			if permission.can()is not True:
				abort_if_unauthorized("修改角色")
			
			role=Role.query.filter(Role.id==id).first()
			abort_if_not_exist(role,"role")
			args=RoleSpec_parser.parse_args()
			roleName=args['roleName']
			nodeName=args['nodeName']
			status=args['status']
			if roleName!=None and roleName!=role.roleName:
				r=Role.query.filter_by(roleName=roleName).first()
				abort_if_exist(r,"rolename")
				role.roleName=roleName
			if status!=None:
				role.status=status
			if nodeName!=None:
				try:
					nodeName=list(eval(nodeName[0]))
				except:
					pass
				n=list()
				for name in nodeName:
					node=Node.query.filter(Node.nodeName==name).first()
					abort_if_not_exist(node,"node")
					n.append(node)
				role.nodes=n

			db.session.add(role)
			db.session.commit()
		elif requestMethod=="DELETE":
			permission=Permission(ActionNeed('删除角色'))
			if permission.can()is not True:
				abort_if_unauthorized("删除角色")

			role=Role.query.filter(Role.id==id).first()
			abort_if_not_exist(role,"role")
			db.session.delete(role)
			db.session.commit()
		else:
			abort(404,message="api not found")
