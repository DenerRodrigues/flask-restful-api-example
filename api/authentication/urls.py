from api.app import api
from api.authentication import views

api.add_resource(views.GetAuthTokenView, '/token/')
