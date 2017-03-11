# -*-coding:utf-8 -*-
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from flask_principal import Permission


from datetime import datetime
from collections import namedtuple
from functools import partial

from .. import lm, db

EditUserNeed = partial(namedtuple("user", ['method', 'value']), 'edit')


class EditUserPermission(Permission):

    def __init__(self, user_id):
        need = EditUserNeed(id)
        super(EditUserPermission, self).__init__(need)


role_node = db.Table('role_node',  # 角色权限关联表
                     db.Column(
                         'node_id', db.Integer, db.ForeignKey('node.id')),
                     db.Column(
                         'role_id', db.Integer, db.ForeignKey('role.id')),
                     db.Column('created_at', db.DateTime, default=datetime.now)
                     )

user_role = db.Table('user_role',  # 用户角色关联表
                     db.Column(
                         'user_id', db.Integer, db.ForeignKey('user.id')),
                     db.Column(
                         'role_id', db.Integer, db.ForeignKey('role.id')),
                     db.Column('created_at', db.DateTime, default=datetime.now)
                     )


class User(db.Model, UserMixin):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    userName = db.Column(db.String(64), unique=True, index=True)
    passWord = db.Column(db.String(128))
    email = db.Column(db.String(40))
    status = db.Column(db.Boolean)
    remark = db.Column(db.String(20))
    phone = db.Column(db.String(20))
    roles = db.relationship(
        "Role", secondary=user_role, backref=db.backref('users', lazy="dynamic"))

    def verify_password(self, passWord):
        return check_password_hash(self.passWord, passWord)

    def get_id(self):
        return self.id

    # def get_id(self):
    #     return str(self.id)  # python 3

    @property
    def nodes(self):
        node = []
        for r in self.role:
            node = node+r.nodes
        return node

    def addRole(self, roleName):
        r = Role.query.filter(Role.roleName == roleName).first()
        self.roles.append(r)

    def __init__(self, userName, passWord, email, phone):
        self.userName = userName
        self.passWord = generate_password_hash(passWord)
        self.email = email
        self.status = True
        self.phone = phone

    def __str__(self):
        return self.userName

    __repr__ = __str__


class LoginLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userName = db.Column(db.String(64))
    loginTime = db.Column(db.DateTime)
    loginIp = db.Column(db.String(40))

    def __init__(self, userName, loginIp):
        self.userName = userName
        self.loginTime = datetime.utcnow()
        self.loginIp = loginIp

    def __str__(self):
        return self.userName
    __repr__ = __str__


class Role(db.Model):
    __tablename__ = "role"
    id = db.Column(db.Integer, primary_key=True)
    roleName = db.Column(db.String(30), unique=True)
    status = db.Column(db.Boolean)
    remark = db.Column(db.String(30))
    nodes = db.relationship(
        "Node", secondary=role_node, backref=db.backref('roles', lazy="dynamic"))

    def addNode(self, nodeName):
        n = Node.query.filter(Node.nodeName == nodeName).first()
        self.nodes.append(n)

    def __init__(self, roleName):
        self.roleName = roleName
        self.status = 1

    def __str__(self):
        return self.roleName

    __repr__ = __str__


class Node(db.Model):
    __tablename__ = "node"
    id = db.Column(db.Integer, primary_key=True)
    nodeName = db.Column(db.String(30), unique=True)
    remark = db.Column(db.String(30))
    status = db.Column(db.Boolean)
    level = db.Column(db.Integer)

    def __init__(self, nodeName, level):
        self.nodeName = nodeName
        self.status = 1
        self.level = level

    def __str__(self):
        return self.nodeName

    __repr__ = __str__
