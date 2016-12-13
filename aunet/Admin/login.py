# -*-coding:utf-8 -*-
from flask_restful import reqparse, abort,Resource,fields,marshal_with
from flask_login import login_user,current_user,logout_user
from flask_principal import identity_loaded,RoleNeed,UserNeed,ActionNeed
from flask_principal import Identity, AnonymousIdentity, \
     identity_changed,Permission
from flask import request,current_app,session
from .models import User,LoginLog
from .models import EditUserPermission,EditUserNeed
from aunet import app,db

login_parser=reqparse.RequestParser()
login_parser.add_argument('userName',type=str,location="json",required=True)
login_parser.add_argument('password',type=str,location="json",required=True)

RequestMethod_parser=reqparse.RequestParser()
RequestMethod_parser.add_argument('requestMethod',type=str,location='json')


@identity_loaded.connect_via(app)
def on_identity_loaded(sender, identity):


    # Set the identity user object
    identity.user = current_user
    #user has the permission of edit himself

    identity.provides.add(EditUserPermission(current_user.id))

    # Add the UserNeed to the identity
    if hasattr(current_user, 'id'):
        identity.provides.add(UserNeed(current_user.id))
        for role in current_user.roles:
            identity.provides.add(RoleNeed(role.roleName))
        
    # Assuming the User model has a list of nodes, update the
    # identity with the nodes that the user provides
    if hasattr(current_user,"roles"):
        for role in current_user.roles:
            for node in role.nodes:
                if (node.status==1) and (current_user.status==1) and (role.status==1):
                    identity.provides.add(ActionNeed(node.nodeName))
    	

def abort_if_unauthorized(message):
	abort(401,message="{} permission Unauthorized".format(message))


class Login(Resource):
	def get(self):
		user=current_user
		if user.is_anonymous==True:
			abort(401,message="unlogined")
		if user.is_authenticated is not True:
			abort(401,message="unlogined")
		if user.is_active is not True:
			abort(401,message="unlogined")
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

	def post(self):
		request_arg=RequestMethod_parser.parse_args()
		requestMethod=request_arg['requestMethod']
		if requestMethod=="POST":
			args=login_parser.parse_args()
			userName=args['userName']
			password=args['password']
			user=User.query.filter(User.userName==userName).first()
			if user==None:
				abort(401,message="userName error")
			elif user.verify_password(password) is not True:
				abort(401,message="password error")
			else:
				session.permanent=True
				login_user(user)
				ip=str(request.remote_addr)
				log=LoginLog(current_user.userName,ip)
				db.session.add(log)
				db.session.commit()
				identity_changed.send(current_app._get_current_object(),identity=Identity(user.id))
		elif requestMethod=="DELETE":
			# Remove the user information from the session
			logout_user()
			for key in ('identity.name', 'identity.auth_type'):
				session.pop(key, None)
		else:
			abort(404,message="api not found")

    		
    		


		    
		  

		    


