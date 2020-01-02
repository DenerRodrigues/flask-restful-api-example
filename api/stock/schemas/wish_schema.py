from marshmallow import fields, Schema

from api.base.models import BaseSchema


class WishCreateSchema(BaseSchema, Schema):
    name = fields.Str(required=True)
    description = fields.Str(required=False)
    price = fields.Number(required=True)
    owner_id = fields.Int(dump_only=True)


class WishListUpdateSchema(BaseSchema, Schema):
    name = fields.Str(required=False)
    description = fields.Str(required=False)
    price = fields.Number(required=False)
    owner_id = fields.Int(dump_only=True)
