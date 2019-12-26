from marshmallow import fields, Schema

from api.base.models import BaseSchema


class UserCreateSchema(BaseSchema, Schema):
    full_name = fields.Str(required=True)
    email = fields.Email(required=True)
    password = fields.Str(required=True, load_only=True)
    cep_address = fields.Str(required=True, load_only=True)
    address = fields.Dict(dump_only=True)


class UserListUpdateSchema(BaseSchema, Schema):
    full_name = fields.Str()
    email = fields.Email()
    cep_address = fields.Str(load_only=True)
    address = fields.Dict(dump_only=True)
