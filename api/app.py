from flask import Flask

from flask_bcrypt import Bcrypt
from flask_cors import CORS
from flask_restful import Api
from flask_restful_swagger import swagger
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object('api.settings')

# initializing database
db = SQLAlchemy(app)
db.init_app(app)

# initializing bcrypt
bcrypt = Bcrypt()
bcrypt.init_app(app)

cors = CORS(app, resources={r'*': {'origins': '*'}})

api = swagger.docs(api=Api(app), api_spec_url=app.config.get('SWAGGER_URL'), apiVersion='1.0.0')
