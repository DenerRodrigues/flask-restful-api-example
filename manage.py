from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from api.app import app, db

migrate = Migrate(app=app, db=db)

manager = Manager(app=app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
