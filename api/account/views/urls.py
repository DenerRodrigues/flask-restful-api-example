from api.app import api
from api.account.views import user_views

api.add_resource(user_views.SignUpView, '/signup/')
api.add_resource(user_views.GetMeView, '/me/')
api.add_resource(user_views.UserChangePasswordView, '/me/change_password/')
