from flask_restful_swagger import swagger

from sqlalchemy.dialects.postgresql import JSON

from api.app import db, bcrypt
from api.base.models import BaseModel


@swagger.model
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

    def __init__(self, full_name: str, email: str, password: str, address: dict):
        self.full_name = full_name
        self.email = email
        self.password = password
        self.address = address
        super(UserModel, self).__init__()

    def save(self):
        self.password = self.__generate_password_hash(self.password)
        super(UserModel, self).save()

    def update(self, **kwargs):
        super(UserModel, self).update(**kwargs)

    def set_password(self, password):
        password_hash = self.__generate_hash(password)
        super(UserModel, self).update(**{'password': password_hash})

    @staticmethod
    def __generate_password_hash(password):
        return bcrypt.generate_password_hash(password, rounds=10).decode('utf-8')

    def check_password_hash(self, password):
        return bcrypt.check_password_hash(self.password, password)

    @property
    def first_name(self):
        return self.full_name.split(' ')[0] if self.full_name else ''

    def __str__(self):
        return '<{} - {}>'.format(self.full_name, self.email)
