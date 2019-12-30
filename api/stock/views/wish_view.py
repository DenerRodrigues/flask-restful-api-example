from flask import request

from flask_restful import Resource
from flask_restful_swagger import swagger

from marshmallow.exceptions import ValidationError
from sqlalchemy.exc import IntegrityError

from api.authentication.auth_token import BasicAuthToken
from api.base.views import BaseView
from api.stock.models.wish_model import WishModel
from api.stock.schemas.wish_schema import WishListCreateSchema, WishListUpdateSchema


auth = BasicAuthToken()


class WishListCreateView(BaseView, Resource):
    schema = WishListCreateSchema()

    @swagger.operation()
    @auth.login_required
    def post(self):
        try:
            data = self.schema.load(request.args)
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

        result = self.schema.dump(wish)
        return self.response(201, True, result)

    @auth.login_required
    @swagger.operation()
    def get(self):
        try:
            data = self.schema.load(request.args)
        except ValidationError as e:
            return self.response(405, False, e.messages)

        owner_id = auth.user.id
        wishes = WishModel.query.filter_by(owner_id=owner_id, is_active=True)

        if data.get('name'):
            wishes = wishes.filter(WishModel.name.ilike('%{}%'.format(data.get('name'))))

        result = self.schema.dump(wishes, many=True)
        return self.response(200, True, result)


class WishView(BaseView, Resource):
    schema = WishListUpdateSchema()

    @auth.login_required
    @swagger.operation()
    def get(self, pk):
        user = auth.user
        wish = WishModel.query.filter_by(id=pk, owner_id=user.id, is_active=True)
        if not wish:
            return self.not_found()
        result = self.schema.dump(wish)
        return self.response(200, True, result)

    @auth.login_required
    @swagger.operation(
        responseClass=WishModel.__name__
    )
    def delete(self, pk):
        user = auth.user
        wish = WishModel.query.filter_by(id=pk, owner_id=user.id, is_active=True)
        if not wish:
            return self.not_found()

        user.delete()
        return self.response(204, True)

    @auth.login_required
    @swagger.operation()
    def put(self, pk):
        user = auth.user
        wish = WishModel.query.filter_by(id=pk, owner_id=user.id, is_active=True)
        if not wish:
            return self.not_found()

        data = self.schema.load(request.args, partial=True)
        wish.update(**data)
        result = self.schema.dump(wish)
        return self.response(201, True, result)
