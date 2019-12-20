from api.app import api
from api.stock.views import wish_view

api.add_resource(wish_view.WishCreateView, '/wish/')
api.add_resource(wish_view.WishView, '/wish/<pk>/')
