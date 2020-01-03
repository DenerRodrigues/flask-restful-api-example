from decimal import Decimal

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
    __table_args__ = (db.UniqueConstraint('name', 'owner_id'),)

    name = db.Column(db.String(128), nullable=False)
    price = db.Column(db.Numeric, nullable=False)
    description = db.Column(db.String(256), nullable=True)

    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __init__(self, name: str, price: Decimal, owner_id: int, description: str = None):
        self.name = name
        self.price = abs(price)
        self.owner_id = owner_id
        self.description = description
        super(WishModel, self).__init__()

    def __str__(self):
        return '{} - {} - $ {}'.format(self.id, self.name, self.price)
