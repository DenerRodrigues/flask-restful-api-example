import json
import requests

from getpass import getpass
from requests.auth import HTTPBasicAuth

from api.app import app

BASE_URL = app.config.get('BASE_URL')


def get_token():
    email = input('Enter your e-mail account: ')
    password = getpass('Enter your password: ')
    auth = HTTPBasicAuth(email, password)
    url = '{}/token/'.format(BASE_URL)
    payload = requests.get(url=url, auth=auth)
    payload.raise_for_status()
    response = payload.json()
    result = json.loads(response).get('result')

    print('GET {}/token/'.format(BASE_URL))
    print('> {}'.format(response))
    print('')

    return result


def get_headers():
    token = get_token()
    return {
        'Content-Type': 'application/json',
        'Authorization': 'Basic {}'.format(token.get('token')),
    }
