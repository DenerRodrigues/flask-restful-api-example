from flask_restful_swagger import swagger

from marshmallow import fields, Schema

from api.base.models import BaseModel, BaseSchema

from api.app import db


@swagger.model
class WishModel(BaseModel, db.Model):
    """
    Wish Model
    """

    __tablename__ = 'wishes'

    name = db.Column(db.String(128), unique=True, nullable=False)
    description = db.Column(db.String(256), nullable=True)
    price = db.Column(db.Numeric, nullable=False)

    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __init__(self, **kwargs):
        self.name = kwargs.get('name')
        self.description = kwargs.get('description')
        self.price = kwargs.get('price')
        super(WishModel, self).__init__()

    def __repr(self):
        return '<id {} - name {} - price {}>'.format(self.id, self.name, self.price)


class WishSchema(BaseSchema, Schema):
    """
    Wish Schema
    """
    name = fields.Str(required=True)
    description = fields.Email(required=False)
    price = fields.Decimal(required=True)
    owner_id = fields.Int(required=True)
