from decimal import Decimal

from flask_restful_swagger import swagger

from api.stock.models.wish_model import WishModel


@swagger.model
class WishCreateUpdateModel(WishModel):
    def __init__(self, name: str, price: Decimal, description: str = None):
        self.name = name
        self.price = abs(price)
        self.description = description


class WishListCreateViewDoc:
    @staticmethod
    def post():
        parameters = [
            dict(
                name='data',
                description='Create Wish',
                dataType=WishCreateUpdateModel.__name__,
                paramType='body',
            ),
        ]

        response_messages = [
            dict(code=201, message='Created'),
            dict(code=405, message='Invalid input')
        ]

        return dict(responseClass=WishCreateUpdateModel.__name__, parameters=parameters, responseMessages=response_messages)

    @staticmethod
    def get():
        parameters = [
            dict(
                name='name',
                description='Filter by name',
                dataType='str',
                paramType='query',
            ),
        ]
        response_messages = [dict(code=200, message='Success')]
        return dict(parameters=parameters, responseMessages=response_messages)


class WishViewDoc:
    @staticmethod
    def get():
        parameters = [
            dict(
                name='pk',
                description='Wish id',
                dataType='int',
                paramType='path',
                required=True,
            ),
        ]
        response_messages = [dict(code=200, message='Success')]
        return dict(parameters=parameters, responseMessages=response_messages)

    @staticmethod
    def delete():
        parameters = [
            dict(
                name='pk',
                description='Wish id',
                dataType='int',
                paramType='path',
                required=True,
            ),
        ]
        response_messages = [dict(code=204, message='Deleted')]
        return dict(parameters=parameters, responseMessages=response_messages)

    @staticmethod
    def put():
        parameters = [
            dict(
                name='pk',
                description='Wish id',
                dataType='int',
                paramType='path',
                required=True
            ),
            dict(
                name='data',
                description='Create Wish',
                dataType=WishCreateUpdateModel.__name__,
                paramType='body',
            ),
        ]

        response_messages = [
            dict(code=201, message='Updated'),
            dict(code=405, message='Invalid input')
        ]

        return dict(responseClass=WishCreateUpdateModel.__name__, parameters=parameters, responseMessages=response_messages)
