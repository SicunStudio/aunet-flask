from . import admin
from flask import render_template,current_app,redirect,request
from flask_login import current_user,login_user,logout_user,login_required
from flask_principal import identity_loaded,RoleNeed,UserNeed,ActionNeed
from flask_principal import Identity, AnonymousIdentity, \
     identity_changed,Permission


from aunet import lm,app
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