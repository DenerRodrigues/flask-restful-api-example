from flask_restful import Api

from api.app import app
from api.account.views import user_view

api = Api(app)

api.add_resource(user_view.SigInView, '/sigin/')
api.add_resource(user_view.GetMeView, '/me/')
