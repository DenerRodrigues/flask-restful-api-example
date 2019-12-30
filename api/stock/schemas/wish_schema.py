from marshmallow import fields, Schema

from api.base.models import BaseSchema


class WishListCreateSchema(BaseSchema, Schema):
    name = fields.Str(required=True)
    description = fields.Email(required=False)
    price = fields.Decimal(required=True)
    owner_id = fields.Int(dump_only=True)


class WishListUpdateSchema(BaseSchema, Schema):
    name = fields.Str(required=False)
    description = fields.Email(required=False)
    price = fields.Decimal(required=False)
    owner_id = fields.Int(dump_only=True)
