from . import admin
from flask import render_template,current_app,redirect,request,make_response
from flask_login import current_user,login_user,logout_user,login_required
from flask_principal import identity_loaded,RoleNeed,UserNeed,ActionNeed
from flask_principal import Identity, AnonymousIdentity, \
     identity_changed,Permission
import json,os

from .news import SilderShow1,SliderShowSpec,News1,NewsSpec,NewsSpecDetail,Tags,Tag1,Categorys,Category1
from .users import Users,UserSpec,Roles,RoleSpec,Nodes,NodeSpec,CurrentUser
from .search import SearchNews


from aunet import lm,app,api
from .models import User,LoginLog
from .models import EditUserPermission,EditUserNeed

from collections import namedtuple
from functools import partial


#user has the permission of edit himself
EditUserNeed=partial(namedtuple("user",['method','value']),'edit')

class EditUserPermission(Permission):
    def __init__(self,user_id):
        need=EditUserNeed(int(user_id))
        super(EditUserPermission,self).__init__(need)


@lm.user_loader
def load_user(id):
    return User.query.get(int(id))


@identity_loaded.connect_via(app)
def on_identity_loaded(sender, identity):
    # Set the identity user object
    identity.user = current_user
    #user has the permission of edit himself

    identity.provides.add(EditUserPermission(current_user.id))

    # Add the UserNeed to the identity
    if hasattr(current_user, 'id'):
        identity.provides.add(UserNeed(current_user.id))
        identity.provides.add(RoleNeed(current_user.role[0].roleName))

    # Assuming the User model has a list of nodes, update the
    # identity with the nodes that the user provides
    if hasattr(current_user,"nodes"):
    	for node in current_user.role[0].nodes:
    	   if (node.status==1) and (current_user.status==1) and (current_user.role[0].status==1):
    	       identity.provides.add(ActionNeed(node.nodeName))

    
    		
@admin.route('/index')
@admin.route('/')
def index():    
    return render_template("Admin/index.html")


@admin.route('/login',methods=["POST","GET"])
def login():
    if request.method=="POST":
        user=User.query.filter(User.userName==request.form['userName']).first()
        if user==None:
            return "user doesn't existed"
        elif user.verify_password(request.form['password']) is not True:
            return "password error"
        else:
            
            login_user(user)
            ip=request.remote_addr
            log=LoginLog(current_user.userName,ip)
            identity_changed.send(current_app._get_current_object(),identity=Identity(user.id))   
            return "good"
            return redirect(request.args.get('next') or '/')

    return render_template("Admin/index.html")



@app.route('/logout')
@login_required
def logout():
    # Remove the user information from the session
    logout_user()

    # Remove session keys set by Flask-Principal
    for key in ('identity.name', 'identity.auth_type'):
        session.pop(key, None)

    # Tell Flask-Principal the user is anonymous
    identity_changed.send(current_app._get_current_object(),
                          identity=AnonymousIdentity())

    return redirect(request.args.get('next') or '/')


@app.route('/api/modules/<path:string>',methods=['GET',"POST"])
def getHtml():
    # path=request.args.get("path","templates/Home/index/index.html")
    #return "dg"
    path=os.path.join(app.config['BASEDIR'],'aunet/',path)
    path=str(path)
    try:
        f=open(path)
        text=f.read()
        res = make_response(text)
        return res
    except:
        return "not found" ,404
    

@admin.route('/upload',methods=['GET',"POST"])
def upload():
    pass


#User 模块
api.add_resource(Users, '/api/User/Users')
api.add_resource(UserSpec,"/api/User/Users/<string:id>")
api.add_resource(Nodes,"/api/User/Nodes")
api.add_resource(NodeSpec,"/api/User/Nodes/<string:id>")
api.add_resource(Roles,"/api/User/Role")
api.add_resource(RoleSpec,"/api/User/Role/<string:id>")


#News 模块

api.add_resource(SilderShow1,"/api/News/SilderShow")
api.add_resource(SliderShowSpec,"/api/News/SilderShow/<string:id>")
api.add_resource(News1,"/api/News/News")
api.add_resource(NewsSpec,"/api/News/News/<string:id>")
api.add_resource(NewsSpecDetail,"/api/News/News/<string:id>/Detail")
api.add_resource(Tags,"/api/News/Tags")
api.add_resource(Tag1,"/api/News/Tags/<string:id>")
api.add_resource(Categorys,"/api/News/Categorys")
api.add_resource(Category1,"/api/News/Categorys/<string:id>")

#Search 模块

api.add_resource(SearchNews,"/api/Search/News")
