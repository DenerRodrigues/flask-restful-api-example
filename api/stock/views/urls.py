from flask_restful import Api

from api.app import app
from api.stock.views import wish_view

api = Api(app)

api.add_resource(wish_view.WishCreateView, '/wish/')
api.add_resource(wish_view.WishView, '/wish/<pk>/')
