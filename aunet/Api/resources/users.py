# -*- coding: utf-8 -*-
from flask_restful import reqparse, abort,Resource,fields,marshal_with
from werkzeug.security import generate_password_hash

from aunet.Admin.models import User,Node,Role,LoginLog
from aunet import db

parser=reqparse.RequestParser()		#User zhong method get de parser
parser.add_argument('page',type=int,help="page")#若请求中无此参数，默认为None
parser.add_argument('per_page',type=int,help="per_page")

Users_fields={									
	'userId':fields.Integer,
	"userName":fields.String,
	"loginTime":fields.DateTime(dt_format='rfc822/iso8601'),
	"loginIp":fields.String,
	"status":fields.Integer,
	"roleName":fields.String
}
Role_fields={
	"roleId":fields.Integer(attribute="id"),
	"roleName":fields.String,
	"remark":fields.String,
	"status":fields.Integer
	
}
Node_fields={
	"nodeid":fields.Integer(attribute="id"),
	"nodeName":fields.String,
	"remark":fields.String,
	"status":fields.Integer,
	"level":fields.Integer
}

User_parser=reqparse.RequestParser()			# User zhong method post de parser
User_parser.add_argument('userName',type=str,required =True,location="json",help="userName")
User_parser.add_argument('passWord',type=str,required =True,location="json",help="passWord")
User_parser.add_argument('email',type=str,location="json",help="email")
User_parser.add_argument('roleName',type=str,required =True,location="json",help="roleName")

User1_parser=reqparse.RequestParser()			#User1 zhong method post de parser
# User1_parser.add_argument('userId',type=int,required=True,location="json",help="userId")
User1_parser.add_argument('lock',type=int,location="json")
User1_parser.add_argument('email',type=str,location="json")
User1_parser.add_argument('passWord',type=str,location="json")
User1_parser.add_argument('roleName',type=str,location="json")
User1_parser.add_argument('userName',type=str,location="json")
User1_parser.add_argument('loginIp',type=str,location="json")
User1_parser.add_argument('loginTime',type=str,location="json") 

# Node_parser=reqparse.RequestParser()
# Node_parser.add_argument('page',type=int,help="page")
# Node_parser.add_argument('per_page',type=int,help="per_page")

NodeSpec_parser=reqparse.RequestParser()
NodeSpec_parser.add_argument('status',type=int,help="status type is int")

Role_parser=reqparse.RequestParser()
Role_parser.add_argument('roleName',type=str,location="json",required=True,help="roleName")
Role_parser.add_argument("remark",type=str,location="json",required=True,help="remark")

RoleSpec_parser=reqparse.RequestParser()
RoleSpec_parser.add_argument('roleName',type=str,location="json")
RoleSpec_parser.add_argument('remark',type=str,location="json")
RoleSpec_parser.add_argument('status',type=int,location="json")


def abort_if_not_exist(data,message):
	if data==None:
		abort(404,message="{} Not Found".format(message))

# def abort_if_node_not_exist(id):
# 	node=Node.query.filter(Node.id==id).first()
# 	if node==None:
# 		abort(404,message="Not Found")

class Users(Resource):
	@marshal_with(Users_fields)
	def get(self):
		args=parser.parse_args()
		page=args['page']
		per_page=args['per_page']
		datas=list()
		data=dict()
		if page!=None and per_page!=None:
			users=User.query.filter(User.id>=(page-1)*per_page,User.id<page*per_page).all()
		else:
			users=User.query.all()
		for user in users:
				log=LoginLog.query.filter(LoginLog.userName==user.userName).first()
				if log !=None:
					data['loginIp']=log.loginIp
					data['loginTime']=log.loginTime
				else:
					data['loginIp']=None
					data['loginTime']=None
				data['userId']=user.id
				data['userName']=user.userName

				data['status']=user.status
				data['roleName']=user.role[0].roleName
				datas.append(data)
		return datas
	def post(self):
		args=User_parser.parse_args()
		userName=args['userName']
		passWord=args['passWord']
		email=args['email']
		roleName=args['roleName']

		user=User(userName,passWord,email,roleName)
		db.session.add(user)
		db.session.commit()


class User1(Resource):			#不用User是避免与User表冲突
	#@marshal_with(Users_fields)
	def get(self,id):
		id=int(id)
		user=User.query.filter(User.id==id).first()
		abort_if_not_exist(user,"user")
		log=LoginLog.query.filter(LoginLog.userName==user.userName).first()
		data=dict()
		if log !=None:
			data['loginIp']=log.loginIp
			data['loginTime']=log.loginTime
		else:
			data['loginIp']=None
			data['loginTime']=None
		data['userId']=user.id
		data['userName']=user.userName
		data['status']=user.status
		data['roleName']=user.role[0].roleName
		return data
		
			# return {"message":"Not Found"} ,404		#


	def put(self,id):
		id=int(id)
		user=User.query.filter(User.id==id).first()
		abort_if_not_exist(user,"user")
		args=User1_parser.parse_args()
		# userId=args['userId']
		lock=args['lock']
		email=args['email']
		passWord=args['passWord']
		roleName=args['roleName']
		userName=args['userName']
		loginIp=args['loginIp']
		loginTime=args['loginTime']
		if lock!=None:
			user.lock=lock
		if email!=None:
			user.email=email
		if passWord!=None:
			user.passWord=generate_password_hash(passWord)
		if roleName!=None:
			user.role[0].roleName=roleName
		if userName!=None:
			user.userName=userName
		db.session.add(user)
		if loginIp!=None or loginTime !=None:
			log=LoginLog(user.userName,loginTime,loginIp)
			db.session.add(log)
		db.session.commit()



	def delete(self,id):
		user=User.query.filter(User.id==id).first()
		abort_if_not_exist(user,"user")
		db.session.delete(user)
		db.session.commit()


class UserRole(Resource):
	@marshal_with(Role_fields)
	def get(self,id):
		id=int(id)
		user=User.query.filter(User.id==id).first()
		abort_if_not_exist(user,"user")
		return user


class UserNodes(Resource):
	def get(self,id):
		id=int(id)
		user=User.query.filter(User.id==id).first()
		abort_if_not_exist(user,"user")
		datas=list()
		data=dict()
		for role in user.role:
			for node in role.nodes:
				data['nodeId']=node.id
				data['nodeName']=node.nodeName
				data['remark']=node.remark
				data['status']=node.status
				data['level']=node.level
				datas.append(data)
		return datas


class UserSpecNodes(Resource):
	@marshal_with(Node_fields)
	def get(self,userId,nodeId):
		userId=int(userId)
		nodeId=int(nodeId)
		user=User.query.filter(User.id==userId).first()
		abort_if_not_exist(user,"user")
		for node in user.nodes:
			if node.id==nodeId:
				return node
		abort(404,message="node Not Found")
		# node=Node.query.filter(Node.id==nodeId).first()

		# abort_if_not_exist(node,"node")
		# data=dict()
		# data['nodeId']=node.id
		# data['nodeName']=node.nodeName
		# data['remark']=node.remark
		# data['status']=node.status
		# data['level']=node.level
		# return data


class Node1(Resource):	
	@marshal_with(Node_fields)						#用Node1 而不用Node 是避免与Node表冲突
	def get(self):
		args=parser.parse_args()
		page=args['page']
		per_page=args['per_page']
		if page!=None and per_page!=None:
			nodes=Node.query.filter(Node.id>=(page-1)*per_page,Node.id<page*per_page).all()
		else :
			nodes=Node.query.all()
		return nodes


class NodeSpec(Resource):
	@marshal_with(Node_fields)
	def get(self,id):
		id=int(id)
		node=Node.query.filter(Node.id==id).first()
		abort_if_not_exist(node,"node")
		return node

	def put(self,id):
		id=int(id)
		node=Node.query.filter(Node.id==id).first()
		abort_if_not_exist(node,"node")
		args=NodeSpec_parser.parse_args()
		status=args['status']
		if status !=None:
			node.status=status
		db.session.add(node)
		db.session.commit()

class Role1(Resource):
	@marshal_with(Role_fields)
	def get(self):
		args=parser.parse_args()
		page=args['page']
		per_page=args['per_page']
		if page!=None and per_page!=None:
			roles=Role.query.filter(Role.id>=(page-1)*per_page,Role.id<page*per_page).all()
		else:
			roles=Role.query.all()
		return roles

	def post(self):
		agrs=Role_parser.parse_args()
		roleName=args['roleName']
		remark=args['remark']
		role=Role(roleName,remark)
		db.session.add(role)
		db.session.commit(role)

class RoleSpec(Resource):
	@marshal_with(Role_fields)
	def get(self,id):
		id=int(id)
		role=Role.query.filter(Role.id==id).first()
		abort_if_not_exist(role,"role")
		return role

	def put(self,id):
		id=int(id)
		role=Role.query.filter(Role.id==id).first()
		abort_if_not_exist(role,"role")
		args=RoleSpec_parser.parse_args()
		roleName=args['roleName']
		remark=args['remark']
		status=args['status']
		if roleName!=None:
			role.roleName=roleName
		if remark!=None:
			role.remark=remark
		if status!=None:
			role.status=status
		db.session.add(role)
		db.session.commit()
	def delete(self,id):
		id=int(id)
		role=Role.query.filter(Role.id==id).first()
		abort_if_not_exist(role,"role")
		db.session.delete(role)
		db.session.commit()