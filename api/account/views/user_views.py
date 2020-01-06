from flask import request

from flask_restful import Resource
from flask_restful_swagger import swagger

from marshmallow.exceptions import ValidationError
from sqlalchemy.exc import IntegrityError

from api.account.views.docs.user_doc import SignUpViewDoc, GetMeViewDoc, UserChangePasswordViewDoc
from api.account.models.user_model import UserModel
from api.account.schemas.user_schema import UserCreateSchema, UserListUpdateSchema, UserChangePasswordSchema
from api.authentication.auth_token import AuthToken
from api.base.views import BaseView
from api.base.utils import get_address_from_cep

auth = AuthToken()


class SignUpView(BaseView, Resource):
    schema = UserCreateSchema()
    operation = SignUpViewDoc()

    @swagger.operation(**operation.post())
    def post(self):
        try:
            data = self.schema.load(request.json or request.args)
        except ValidationError as e:
            return self.response(405, False, e.messages)
        try:
            address = get_address_from_cep(data.get('cep_address'))
        except Exception as e:
            return self.response(405, False, e)

        full_name = data.get('full_name')
        email = data.get('email')
        password = data.get('password')

        user = UserModel(full_name, email, password, address)
        try:
            user.save()
        except IntegrityError as e:
            result = e._message().split('DETAIL:  ')[1].replace('\n', '')
            return self.response(405, False, result)

        result = self.schema.dump(user)
        return self.response(201, True, result)


class GetMeView(BaseView, Resource):
    schema = UserListUpdateSchema()
    operation = GetMeViewDoc()

    @auth.login_required
    @swagger.operation(**operation.get())
    def get(self):
        user = auth.user
        data = self.schema.dump(user)
        return self.response(200, True, data)

    @auth.login_required
    @swagger.operation(**operation.delete())
    def delete(self):
        user = auth.user
        user.delete()
        return self.response(204, True)

    @auth.login_required
    @swagger.operation(**operation.put())
    def put(self):
        try:
            data = self.schema.load(request.args or request.json)
        except ValidationError as e:
            return self.response(405, False, e.messages)
        try:
            data['address'] = get_address_from_cep(data.get('cep_address'))
        except Exception as e:
            return self.response(405, False, str(e))

        user = auth.user
        user.update(**data)
        result = self.schema.dump(user)
        return self.response(201, True, result)


class UserChangePasswordView(BaseView, Resource):
    schema = UserChangePasswordSchema()
    operation = UserChangePasswordViewDoc()

    @auth.login_required
    @swagger.operation(**operation.put())
    def put(self):
        try:
            data = self.schema.load(request.args or request.json)
        except ValidationError as e:
            return self.response(405, False, e.messages)
        user = auth.user
        if user.check_password_hash(data.get('old_password')):
            user.set_password(data.get('new_password'))
        else:
            return self.response(405, False, 'Incorrect Password')
        return self.response(204, True)
