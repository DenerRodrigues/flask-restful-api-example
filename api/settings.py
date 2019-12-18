import os

from dotenv import load_dotenv

load_dotenv()

FLASK_DEBUG = os.getenv('FLASK_DEBUG', False)
FLASK_ENV = os.getenv('FLASK_ENV', 'production')

SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
SQLALCHEMY_TRACK_MODIFICATIONS = False
