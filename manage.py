from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand

from aunet import app,db
from aunet.Home.models import News


migrate=Migrate(app,db)

manager=Manager(app)
manager.add_command("db",MigrateCommand)

from aunet.Home.models import News,Notice,AdvanceNotice,StarAssociation,CharmAssociation,AssociationTag


if __name__ == '__main__':
    manager.run()