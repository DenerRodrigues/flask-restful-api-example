import requests


def get_address_from_cep(cep: str):
    payload = requests.get('http://viacep.com.br/ws/{cep}/json'.format(cep=cep))
    address = payload.json()
    return address
