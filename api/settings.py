import os

from dotenv import load_dotenv

load_dotenv()

FLASK_DEBUG = os.getenv('FLASK_DEBUG', False)
FLASK_ENV = os.getenv('FLASK_ENV', 'production')
FLASK_SECRET_KEY = os.getenv('FLASK_SECRET_KEY')

SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
SQLALCHEMY_TRACK_MODIFICATIONS = False

BASE_URL = os.getenv('BASE_URL')

AUTH_TOKEN_EXPIRATION = os.getenv('AUTH_TOKEN_EXPIRATION', 600)
