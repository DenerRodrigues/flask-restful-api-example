from flask import request

from flask_restful import Resource
from flask_restful_swagger import swagger

from marshmallow.exceptions import ValidationError
from sqlalchemy.exc import IntegrityError

from api.authentication.auth_token import AuthToken
from api.base.views import BaseView
from api.stock.models.wish_model import WishModel
from api.stock.schemas.wish_schema import WishCreateSchema, WishListUpdateSchema
from api.stock.views.docs.wish_doc import WishViewDoc, WishListCreateViewDoc


auth = AuthToken()


class WishListCreateView(BaseView, Resource):
    create_schema = WishCreateSchema()
    list_schema = WishListUpdateSchema()
    operation = WishListCreateViewDoc()

    @swagger.operation(**operation.post())
    @auth.login_required
    def post(self):
        try:
            data = self.create_schema.load(request.json or request.form or request.args)
        except ValidationError as e:
            return self.response(405, False, e.messages)

        owner_id = auth.user.id
        name = data.get('name')
        price = data.get('price')
        description = data.get('description')

        wish = WishModel(name, price, owner_id, description)
        try:
            wish.save()
        except IntegrityError as e:
            result = e._message().split('DETAIL:  ')[1].replace('\n', '')
            return self.response(405, False, result)

        result = self.create_schema.dump(wish)
        return self.response(201, True, result)

    @auth.login_required
    @swagger.operation(**operation.get())
    def get(self):
        try:
            data = self.list_schema.load(request.json or request.form or request.args)
        except ValidationError as e:
            return self.response(405, False, e.messages)

        owner_id = auth.user.id
        wishes = WishModel.query.filter_by(owner_id=owner_id, is_active=True)

        if data.get('name'):
            wishes = wishes.filter(WishModel.name.ilike('%{}%'.format(data.get('name'))))

        result = self.list_schema.dump(wishes.all(), many=True)
        return self.response(200, True, result)


class WishView(BaseView, Resource):
    schema = WishListUpdateSchema()
    operation = WishViewDoc()

    @auth.login_required
    @swagger.operation(**operation.get())
    def get(self, pk):
        user = auth.user
        wish = WishModel.query.filter_by(id=pk, owner_id=user.id, is_active=True).one_or_none()
        if not wish:
            return self.not_found()
        result = self.schema.dump(wish)
        return self.response(200, True, result)

    @auth.login_required
    @swagger.operation(**operation.delete())
    def delete(self, pk):
        user = auth.user
        wish = WishModel.query.filter_by(id=pk, owner_id=user.id, is_active=True).one_or_none()
        if not wish:
            return self.not_found()

        wish.delete()
        return self.response(204, True)

    @auth.login_required
    @swagger.operation(**operation.put())
    def put(self, pk):
        try:
            data = self.schema.load(request.json or request.form or request.args)
        except ValidationError as e:
            return self.response(405, False, e.messages)

        user = auth.user
        wish = WishModel.query.filter_by(id=pk, owner_id=user.id, is_active=True).one_or_none()
        if not wish:
            return self.not_found()

        wish.update(**data)
        result = self.schema.dump(wish)
        return self.response(201, True, result)
