import requests

from api.app import app
from api.authentication.tests import get_headers

BASE_URL = app.config.get('BASE_URL')


def create_wish(token):
    data = dict(
        name=input('Enter wish name: '),
        price=input('Enter wish price: (1.99) '),
        description=input('Enter wish description: '),
    )

    url = '{}/wish/'.format(BASE_URL)
    payload = requests.post(url=url, json=data, headers=get_headers(token))
    payload.raise_for_status()
    response = payload.json()
    result = response.get('result')

    print('POST {}/wish/'.format(BASE_URL))
    print('> {}'.format(response))
    print('')

    return result
