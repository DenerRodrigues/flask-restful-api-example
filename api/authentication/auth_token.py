from itsdangerous import BadSignature, SignatureExpired
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

from flask_httpauth import HTTPBasicAuth

from api.app import app
from api.account.models.user_model import UserModel


class BasicAuthToken(HTTPBasicAuth):
    def __init__(self, user=None):
        super(BasicAuthToken, self).__init__()
        self.user = user

    def authenticate(self, auth, stored_password=None):
        if auth and auth.get('token'):
            self.user = self.verify_auth_token(auth.get('token'))
        elif auth and auth.get('username') and auth.get('password'):
            self.user = UserModel.query.filter_by(email=auth.get('username'), is_active=True).one_or_none()
            if not self.user.check_password_hash(auth.get('password')):
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
        self.user = UserModel.query.get(data.get('id'))
        return self.user
