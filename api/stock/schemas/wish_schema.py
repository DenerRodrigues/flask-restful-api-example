from decimal import Decimal

from marshmallow import fields, Schema
from marshmallow.validate import Range

from api.base.models import BaseSchema


class WishCreateSchema(BaseSchema, Schema):
    name = fields.Str(required=True)
    description = fields.Str(required=False)
    price = fields.Number(required=True, validate=[Range(min=0.01, error='Value must be greater than 0')])
    owner_id = fields.Int(dump_only=True)


class WishListUpdateSchema(BaseSchema, Schema):
    name = fields.Str(required=False)
    description = fields.Str(required=False)
    price = fields.Number(required=False, validate=[Range(min=0.01, error='Value must be greater than 0')])
    owner_id = fields.Int(dump_only=True)
