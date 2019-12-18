from datetime import datetime

from marshmallow import fields

from api.app import db


class BaseModel:
    """
    Base Model
    """
    id = db.Column(db.Integer, primary_key=True)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime)
    modified_at = db.Column(db.DateTime)

    def __init__(self):
        self.created_at = datetime.utcnow()
        self.modified_at = datetime.utcnow()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self, **kwargs):
        for key, item in kwargs.items():
            setattr(self, key, item)
        self.modified_at = datetime.utcnow()
        db.session.commit()

    def delete(self):
        self.update(is_active=False)

    def __repr(self):
        return '<id {}>'.format(self.id)


class BaseSchema:
    """
    User Schema
    """
    id = fields.Int(dump_only=True)
    is_active = fields.Bool(dump_only=True)
    created_at = fields.DateTime(dump_only=True)
    modified_at = fields.DateTime(dump_only=True)
