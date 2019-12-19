import requests

from api.app import app
from api.authentication.tests import get_headers

BASE_URL = app.config.get('BASE_URL')


def get_me():
    url = '{}/me/'.format(BASE_URL)
    payload = requests.get(url=url, headers=get_headers())
    payload.raise_for_status()
    token = payload.json()
    return token
