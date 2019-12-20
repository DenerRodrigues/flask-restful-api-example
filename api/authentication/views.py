from flask_restful import Resource
from flask_restful_swagger import swagger

from api.base.views import BaseView
from api.authentication.auth_token import BasicAuthToken

auth = BasicAuthToken()


class GetAuthTokenView(BaseView, Resource):
    @auth.login_required
    @swagger.operation()
    def get(self):
        token = auth.generate_auth_token()
        result = {'token': token.decode('ascii')}
        return self.response(200, True, result)
