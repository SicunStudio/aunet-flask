from . import admin
from flask import render_template,current_app,redirect,request,make_response
from flask_login import current_user,login_user,logout_user,login_required
from flask_principal import identity_loaded,RoleNeed,UserNeed,ActionNeed
from flask_principal import Identity, AnonymousIdentity, \
     identity_changed,Permission
import json,os

from .news import SilderShow1,SliderShowSpec,News1,NewsSpec,NewsSpecDetail
from .users import User1,Users,UserNodes,UserRole,UserSpecNodes,Node1,NodeSpec,RoleSpec,Role1
from .search import SearchNews


from aunet import lm,app,api
from .models import User

@lm.user_loader
def load_user(id):
    return User.query.get(int(id))

@identity_loaded.connect_via(app)
def on_identity_loaded(sender, identity):
    # Set the identity user object
    identity.user = current_user

    # Add the UserNeed to the identity
    if hasattr(current_user, 'id'):
        identity.provides.add(UserNeed(current_user.id))

    # Assuming the User model has a list of nodes, update the
    # identity with the nodes that the user provides
    if hasattr(current_user,"nodes"):
    	for node in current_user.nodes:
    		if node.status==1:
    			identity.provides.add(ActionNeed(node.nodeName))


    		
@admin.route('/index')
@admin.route('/')
def index():
	return render_template("Admin/index.html")




@admin.route('/login',methods=["POST","GET"])
def login():
    if request.method=="POST":
        user=User.query.filter_by(User.userName==form.userName.data).first()
        if user==None:
            return "user doesn't existed"
        elif user.verify_password(form.password.data) is not True:
            return "password error"
        else:
            login_user(user)
            identity_changed.send(current_app._get_current_object(),identity=Identity(user.id))   
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


@admin.route('/getHtml',methods=['GET',"POST"])
def getHtml():
    path=request.args.get("path","templates/Home/index/index.html")
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
api.add_resource(User1,"/api/User/Users/<string:id>")
api.add_resource(UserRole,"/api/User/Users/<string:id>/Role")
api.add_resource(UserNodes,"/api/User/Users/<string:id>/Nodes")
api.add_resource(UserSpecNodes,"/api/User/Users/<string:userId>/Nodes/<string:nodeId>")
api.add_resource(Node1,"/api/User/Nodes")
api.add_resource(NodeSpec,"/api/User/Nodes/<string:id>")
api.add_resource(Role1,"/api/User/Role")
api.add_resource(RoleSpec,"/api/User/Role/<string:id>")


#News 模块

api.add_resource(SilderShow1,"/api/News/SilderShow")
api.add_resource(SliderShowSpec,"/api/News/SilderShow/<string:id>")
api.add_resource(News1,"/api/News")
api.add_resource(NewsSpec,"/api/News/<string:id>")
api.add_resource(NewsSpecDetail,"/api/News/<string:id>/Detail")



#Search 模块

api.add_resource(SearchNews,"/api/Search/News")
