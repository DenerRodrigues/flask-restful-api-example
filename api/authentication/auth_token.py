from itsdangerous import BadSignature, SignatureExpired
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

from flask import request
from flask_httpauth import HTTPBasicAuth

from api.app import app
from api.account.models.user_model import UserModel


class AuthToken(HTTPBasicAuth):
    def __init__(self, user=None):
        super(AuthToken, self).__init__()
        self.user = user

    def get_auth(self):
        if request.authorization:
            self.scheme = 'Basic'
        else:
            self.scheme = 'Bearer'
        return super(AuthToken, self).get_auth()

    def authenticate(self, auth, stored_password=None):
        if auth and auth.get('token'):
            self.user = self.verify_auth_token(auth.get('token'))
        elif auth and auth.get('username') and auth.get('password'):
            self.user = UserModel.query.filter_by(email=auth.get('username'), is_active=True).one_or_none()
            if self.user and not self.user.check_password_hash(auth.get('password')):
                # invalid password
                return None
        return self.user

    def generate_auth_token(self):
        secret_key = app.config.get('FLASK_SECRET_KEY')
        token_expiration = app.config.get('AUTH_TOKEN_EXPIRATION')
        serializer = Serializer(secret_key, expires_in=token_expiration)
        token = serializer.dumps({'id': self.user.id})
        return token

    def verify_auth_token(self, token):
        secret_key = app.config.get('FLASK_SECRET_KEY')
        serializer = Serializer(secret_key)
        try:
            data = serializer.loads(token)
        except SignatureExpired:
            # valid token, but expired
            return None
        except BadSignature:
            # invalid token
            return None
        self.user = UserModel.query.filter_by(id=data.get('id'), is_active=True).one_or_none()
        return self.user
