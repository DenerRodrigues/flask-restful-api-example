from flask import request

from flask_restful import Resource
from marshmallow.exceptions import ValidationError

from api.account.models.user_model import UserModel, UserSchema
from api.authentication.auth_token import BasicAuthToken
from api.base.views import BaseView

auth = BasicAuthToken()
user_schema = UserSchema()


class SigInView(BaseView, Resource):
    def post(self):
        try:
            data = user_schema.load(request.form)
        except ValidationError as e:
            return self.response(401, False, e.messages)

        user = UserModel(**data)
        user.save()

        result = user_schema.dump(user)
        return self.response(201, True, result)


class GetMeView(BaseView, Resource):
    @auth.login_required
    def get(self):
        user = auth.user
        if not user:
            return self.not_found()

        result = user_schema.dump(user)
        return self.response(200, True, result)

    @auth.login_required
    def delete(self):
        user = auth.user
        if not user:
            return self.not_found()

        user.delete()
        return self.response(204, True)

    @auth.login_required
    def put(self):
        user = auth.user
        if not user:
            return self.not_found()

        data = user_schema.load(request.form, partial=True)
        user.update(**data)
        result = user_schema.dump(user)
        return self.response(201, True, result)
