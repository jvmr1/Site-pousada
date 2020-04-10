from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_login import LoginManager

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///storage.db'
app.config.from_object('config')
db = SQLAlchemy(app)
migrate = Migrate(app, db)

login_manager = LoginManager()
login_manager.init_app(app)

from app.models.tables import User

@login_manager.user_loader
def load_user(user_id):
    return User.get_id

manager = Manager(app)
manager.add_command('db', MigrateCommand)

from app.controllers import default
from app.models import tables, forms
