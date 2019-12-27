from api.app import api
from api.account.views import user_view

api.add_resource(user_view.SigInView, '/sigin/')
api.add_resource(user_view.GetMeView, '/me/')
api.add_resource(user_view.UserChangePasswordView, '/me/change_password/')
