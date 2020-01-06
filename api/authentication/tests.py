import requests

from getpass import getpass
from requests.auth import HTTPBasicAuth

from api.app import app

BASE_URL = app.config.get('BASE_URL')


def get_token():
    email = input('Enter your e-mail account: ')
    password = getpass('Enter your password: ')

    url = '{}/token/'.format(BASE_URL)
    auth = HTTPBasicAuth(email, password)
    payload = requests.post(url=url, auth=auth)
    payload.raise_for_status()
    response = payload.json()
    result = response.get('result')

    print('POST {}/token/'.format(BASE_URL))
    print('> {}'.format(response))
    print('')

    return result.get('token')


def get_headers(token: str = None):
    if not token:
        token = get_token()
    return {
        'Content-Type': 'application/json',
        'Authorization': 'Basic {}'.format(token),
    }
