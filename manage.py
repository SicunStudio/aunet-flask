from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand

from aunet import app,db



migrate=Migrate(app,db)

manager=Manager(app)
manager.add_command("db",MigrateCommand)

from aunet.Home.models import News,news_category,news_tag,Category,Tag,	SilderShow
from aunet.Admin.models import User,Node,Role,user_role,role_node

if __name__ == '__main__':
    manager.run()