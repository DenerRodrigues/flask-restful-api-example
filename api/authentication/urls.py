from flask_restful import Api

from api.app import app
from api.authentication import views

api = Api(app)

api.add_resource(views.GetAuthTokenView, '/token/')
