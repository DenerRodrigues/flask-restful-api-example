from flask import request

from flask_restful import Resource
from flask_restful_swagger import swagger
from marshmallow.exceptions import ValidationError

from api.stock.models.wish_model import WishModel, WishSchema
from api.authentication.auth_token import BasicAuthToken
from api.base.views import BaseView

auth = BasicAuthToken()
wish_schema = WishSchema()


class WishCreateView(BaseView, Resource):
    @swagger.operation()
    @auth.login_required
    def post(self):
        user = auth.user
        request.form['owner_id'] = user.id
        try:
            data = wish_schema.load(request.form)
        except ValidationError as e:
            return self.response(401, False, e.messages)

        user = WishModel(**data)
        user.save()

        result = wish_schema.dump(user)
        return self.response(201, True, result)


class WishView(BaseView, Resource):
    @auth.login_required
    @swagger.operation(
        responseClass=WishModel.__name__
    )
    def get(self, pk):
        user = auth.user
        wish = WishModel.query.filter_by(id=pk, owner_id=user.id, is_active=True)
        if not wish:
            return self.not_found()
        result = wish_schema.dump(wish)
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
    @swagger.operation(
        responseClass=WishModel.__name__
    )
    def put(self, pk):
        user = auth.user
        wish = WishModel.query.filter_by(id=pk, owner_id=user.id, is_active=True)
        if not wish:
            return self.not_found()

        data = wish_schema.load(request.form, partial=True)
        wish.update(**data)
        result = wish_schema.dump(wish)
        return self.response(201, True, result)
