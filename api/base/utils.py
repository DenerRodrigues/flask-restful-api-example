import requests


def get_address_from_cep(cep: str):
    payload = requests.get('http://viacep.com.br/ws/{cep}/json'.format(cep=cep.replace('-', '')))
    try:
        payload.raise_for_status()
    except requests.HTTPError:
        raise requests.HTTPError('Invalid CEP')
    address = payload.json()
    if address.get('erro'):
        raise requests.HTTPError('Invalid CEP')
    return {
        'cep': address.get('cep'),
        'street': address.get('logradouro'),
        'neighborhood': address.get('bairro'),
        'city': address.get('localidade'),
        'state': address.get('uf'),
        'country': 'BR',
    }
