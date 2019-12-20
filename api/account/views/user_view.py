from flask import request

from flask_restful import Resource
from flask_restful_swagger import swagger

from marshmallow.exceptions import ValidationError

from api.account.models.user_model import UserModel, UserSchema
from api.authentication.auth_token import BasicAuthToken
from api.base.views import BaseView

auth = BasicAuthToken()
user_schema = UserSchema()


class SigInView(BaseView, Resource):
    @auth.login_required
    @swagger.operation(
        responseClass=UserModel.__name__,
        parameters=[
            {
                "name": "fullname",
                "description": "User fullname",
                "required": True,
                "allowMultiple": False,
                "dataType": UserModel.__name__,
                "paramType": "str"
            },
            {
                "name": "email",
                "description": "User e-mail",
                "required": True,
                "allowMultiple": False,
                "dataType": UserModel.__name__,
                "paramType": "str"
            },
            {
                "name": "password",
                "description": "User password",
                "required": True,
                "allowMultiple": False,
                "dataType": UserModel.__name__,
                "paramType": "str"
            }
        ],
        responseMessages=[
            {
                "code": 201,
                "message": "Created"
            },
            {
                "code": 405,
                "message": "Invalid input"
            }
        ]
    )
    def post(self):
        try:
            data = user_schema.load(request.form)
        except ValidationError as e:
            return self.response(405, False, e.messages)
        user = UserModel(**data)
        user.save()
        result = user_schema.dump(user)
        return self.response(201, True, result)


class GetMeView(BaseView, Resource):
    @auth.login_required
    @swagger.operation(
        responseClass=UserModel.__name__
    )
    def get(self):
        user = auth.user
        result = user_schema.dump(user)
        return self.response(200, True, result)

    @auth.login_required
    @swagger.operation(
        responseClass=UserModel.__name__
    )
    def delete(self):
        user = auth.user
        user.delete()
        return self.response(204, True)

    @auth.login_required
    @swagger.operation(
        responseClass=UserModel.__name__
    )
    def put(self):
        user = auth.user
        data = user_schema.load(request.form, partial=True)
        user.update(**data)
        result = user_schema.dump(user)
        return self.response(201, True, result)
