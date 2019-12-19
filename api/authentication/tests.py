import json
import requests

from requests.auth import HTTPBasicAuth

from api.app import app

BASE_URL = app.config.get('BASE_URL')


def get_token():
    auth = HTTPBasicAuth('dl.rodrigues94@gmail.com', '123456')
    url = '{}/token/'.format(BASE_URL)
    payload = requests.get(url=url, auth=auth)
    payload.raise_for_status()
    token = json.loads(payload.json()).get('result', {}).get('token')
    return token


def get_headers():
    return {
        'Content-Type': 'application/json',
        'Authorization': 'Basic {}'.format(get_token()),
    }
