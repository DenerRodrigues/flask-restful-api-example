from sqlalchemy.dialects.postgresql import JSON
from marshmallow import fields, Schema

from api.app import db, bcrypt
from api.base.models import BaseModel, BaseSchema


class UserModel(BaseModel, db.Model):
    """
    User Model
    """

    __tablename__ = 'users'

    full_name = db.Column(db.String(128), nullable=True)
    email = db.Column(db.String(128), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=True)
    address = db.Column(JSON)

    wishes = db.relationship('WishModel', backref='users', lazy=True)

    def __init__(self, **kwargs):
        self.full_name = kwargs.get('full_name')
        self.email = kwargs.get('email')
        self.password = kwargs.get('password')
        self.address = kwargs.get('address')
        self.wishes = kwargs.get('wishes')
        super(UserModel, self).__init__()

    def save(self):
        self.password = self.__generate_hash(self.password)
        super(UserModel, self).save()

    def update(self, **kwargs):
        if kwargs.get('password'):
            kwargs['password'] = self.__generate_hash(kwargs.get('password'))
        super(UserModel, self).update(**kwargs)

    @staticmethod
    def __generate_password_hash(password):
        return bcrypt.generate_password_hash(password, rounds=10).decode('utf-8')

    def check_password_hash(self, password):
        return bcrypt.check_password_hash(self.password, password)

    @property
    def first_name(self):
        return self.full_name.split(' ')[0] if self.full_name else ''

    def __repr(self):
        return '<id {} - email {}>'.format(self.id, self.email)


class UserSchema(BaseSchema, Schema):
    """
    User Schema
    """
    full_name = fields.Str(required=True)
    email = fields.Email(required=True)
    password = fields.Str(required=True, load_only=True)
    address = fields.Dict(required=False)
