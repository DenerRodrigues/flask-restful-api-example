from api.app import api
from api.stock.views import wish_views

api.add_resource(wish_views.WishListCreateView, '/wish/')
api.add_resource(wish_views.WishView, '/wish/<pk>/')
