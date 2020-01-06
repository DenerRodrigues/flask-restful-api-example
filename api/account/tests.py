import requests

from getpass import getpass

from api.app import app
from api.authentication.tests import get_headers

BASE_URL = app.config.get('BASE_URL')


def signup():
    data = dict(
        full_name=input('Enter your full name: '),
        email=input('Enter your e-mail: '),
        password=getpass('Enter your password: '),
        cep_address=input('Enter your cep address: '),
    )

    url = '{}/signup/'.format(BASE_URL)
    payload = requests.post(url=url, json=data)
    payload.raise_for_status()
    response = payload.json()
    result = response.get('result')

    print('POST {}/signup/'.format(BASE_URL))
    print('> {}'.format(response))
    print('')

    return result


def get_me(token):
    url = '{}/me/'.format(BASE_URL)
    payload = requests.get(url=url, headers=get_headers(token))
    payload.raise_for_status()
    response = payload.json()
    result = response.get('result')

    print('GET {}/me/'.format(BASE_URL))
    print('> {}'.format(response))
    print('')

    return result
