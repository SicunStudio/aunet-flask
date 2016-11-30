# -*- coding:utf-8 -*-
from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand

from aunet import app,db
from aunet.Home.models import News,news_category,news_tag,Category,Tag,	SilderShow
from aunet.Admin.models import User,Node,Role,user_role,role_node


migrate=Migrate(app,db)
manager=Manager(app)

manager.add_command("db",MigrateCommand)#数据库我迁移命令


@manager.option('-n', '--name', dest="name",help='Your name',default="admin")
@manager.option('-p','--password',dest='password',help="Your password",default="123456")
@manager.option('-e','--email',dest="email",help="your email",default=None)
@manager.option('--phone',dest="phone",help="your phone",default=None)
def CreateSuperUser(name,password,email,phone):
	try:
		user=User(name,password,email,phone)
		user.addRole("超管")
		db.session.add(user)
		db.session.commit()
		print ("successfully create a super user name:%s,password:%s,email:%s,phone:%s"%(name,password,email,phone))
	except:
		print("something wrong.please ensure you have created a super role and your name is unique")

@manager.command
def CreateSuperRole():
	try:
		role=Role("超管")
		node1=Node("添加用户",1)
		node2=Node("修改用户",1)
		node3=Node("删除用户",1)
		node4=Node("添加角色",1)
		node5=Node("修改角色",1)
		node6=Node("删除角色",1)
		node7=Node("添加新闻",1)
		node8=Node("修改新闻",1)
		node9=Node("删除新闻",1)
		node10=Node("添加新闻属性",1)
		node11=Node("修改新闻属性",1)
		node12=Node("删除新闻属性",1)
		node13=Node("添加新闻标签",1)
		node14=Node("修改新闻标签",1)
		node15=Node("删除新闻标签",1)
		node16=Node("修改节点",1)
		node17=Node("materialAdmin",1)
		node18=Node("materialAction",1)
		node19=Node("查看新闻",1)
		node20=Node("查看新闻栏目",1)
		node21=Node("查看新闻标签",1)
		node22=Node("查看用户",1)
		node23=Node("查看角色",1)
		node24=Node("查看权限节点",1)
		db.session.add(node1)
		db.session.add(node2)
		db.session.add(node3)
		db.session.add(node4)
		db.session.add(node5)
		db.session.add(node6)
		db.session.add(node7)
		db.session.add(node8)
		db.session.add(node9)
		db.session.add(node10)
		db.session.add(node11)
		db.session.add(node12)
		db.session.add(node13)
		db.session.add(node14)
		db.session.add(node15)
		db.session.add(node16)
		db.session.add(node17)
		db.session.add(node18)
		db.session.add(node19)
		db.session.add(node20)
		db.session.add(node21)
		db.session.add(node22)
		db.session.add(node23)
		db.session.add(node24)
		db.session.add(role)
		db.session.commit()
		role=Role.query.filter(Role.roleName=="超管").first()
		role.addNode("添加用户")
		role.addNode("删除用户")
		role.addNode("修改用户")
		role.addNode("添加角色")
		role.addNode("修改角色")
		role.addNode("删除角色")
		role.addNode("添加新闻")
		role.addNode("修改新闻")
		role.addNode("删除新闻")
		role.addNode("添加新闻属性")
		role.addNode("修改新闻属性")
		role.addNode("删除新闻属性")
		role.addNode("添加新闻标签")
		role.addNode("修改新闻标签")
		role.addNode("删除新闻标签")
		role.addNode("修改节点")
		role.addNode("materialAdmin")
		role.addNode("materialAction")
		role.addNode("查看新闻")
		role.addNode("查看新闻栏目")
		role.addNode("查看新闻标签")
		role.addNode("查看用户")
		role.addNode("查看角色")
		role.addNode("查看权限节点")

		db.session.add(role)
		db.session.commit()
		print("successfully create a super role name:超管");
	except:
		print("you can only run it once")



if __name__ == '__main__':
    manager.run()
