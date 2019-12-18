from flask import Flask

from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object('api.settings')

# initializing database
db = SQLAlchemy(app)
db.init_app(app)

# initializing bcrypt
bcrypt = Bcrypt()
bcrypt.init_app(app)
