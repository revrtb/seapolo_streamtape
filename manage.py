from flask_script import Manager
from linkapp import application, db, bcrypt
from flask_migrate import Migrate, MigrateCommand
from flask_script import Command
from lib import link, user
import base64
import hashlib

import sys, os
curDir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, curDir)

manager = Manager(application)

class InitDbCommand(Command):
    """ Initialize the database."""

    def run(self):
        init_db()

def init_db():
	try:
		db.drop_all()
		db.create_all()
		usero = user.User("admin@revrtb.com", bcrypt.generate_password_hash("4everR3vRtb9090"))
		db.session.add(usero)
		db.session.commit()
	except Exception as e:
		print(e)

class TestCommand(Command):
    """ Initialize the database."""

    def run(self):
        test()

migrate = Migrate(application, db)
manager.add_command('initdb', InitDbCommand)
manager.add_command('test', TestCommand)

if __name__ == "__main__":
    manager.run()

