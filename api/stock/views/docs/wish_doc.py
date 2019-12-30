from api.stock.models.wish_model import WishModel


class WishListCreateViewDoc:
    def __init__(self):
        self.response_class = WishModel.__name__

    def post(self):
        parameters = [
            dict(
                name='name',
                description='Wish name',
                required=True,
                dataType='str',
                paramType='query'
            ),
            dict(
                name='price',
                description='Wish price',
                required=True,
                dataType='decimal',
                paramType='query',
            ),
            dict(
                name='description',
                description='Wish description',
                required=False,
                dataType='str',
                paramType='query',
            ),
        ]

        response_messages = [
            dict(code=201, message='Created'),
            dict(code=405, message='Invalid input')
        ]

        return dict(responseClass=self.response_class, parameters=parameters, responseMessages=response_messages)

    def get(self):
        parameters = [
            dict(
                name='name',
                description='Wish name',
                required=False,
                dataType='str',
                paramType='query'
            ),
        ]
        response_messages = [dict(code=200, message='Success')]
        return dict(responseClass=self.response_class, parameters=parameters, responseMessages=response_messages)


class WishViewDoc:
    def __init__(self):
        self.response_class = WishModel.__name__

    def get(self):
        response_messages = [dict(code=200, message='Success')]
        return dict(responseClass=self.response_class, responseMessages=response_messages)

    def delete(self):
        response_messages = [dict(code=204, message='Deleted')]
        return dict(responseClass=self.response_class, responseMessages=response_messages)

    def put(self):
        parameters = [
            dict(
                name='name',
                description='Wish name',
                required=True,
                dataType='str',
                paramType='query'
            ),
            dict(
                name='price',
                description='Wish price',
                required=True,
                dataType='decimal',
                paramType='query',
            ),
            dict(
                name='description',
                description='Wish description',
                required=False,
                dataType='str',
                paramType='query',
            ),
        ]

        response_messages = [
            dict(code=201, message='Updated'),
            dict(code=405, message='Invalid input')
        ]

        return dict(responseClass=self.response_class, parameters=parameters, responseMessages=response_messages)
