from api.account.models.user_model import UserModel


class SigInViewDoc:
    def __init__(self):
        self.response_class = UserModel.__name__

    def post(self):
        parameters = [
            dict(
                name='full_name',
                description='User fullname',
                required=True,
                dataType='str',
                paramType='query'
            ),
            dict(
                name='email',
                description='User e-mail',
                required=True,
                dataType='str',
                paramType='query',
            ),
            dict(
                name='password',
                description='User password',
                required=True,
                dataType='str',
                paramType='query',
            ),
            dict(
                name='cep_address',
                description='User CEP address',
                required=True,
                dataType='str',
                paramType='query'
            ),
        ]

        response_messages = [
            dict(code=201, message='Created'),
            dict(code=405, message='Invalid input')
        ]

        return dict(responseClass=self.response_class, parameters=parameters, responseMessages=response_messages)


class GetMeViewDoc:
    def __init__(self):
        self.response_class = UserModel.__name__

    def get(self):
        response_messages = [dict(code=200, message='Success')]
        return dict(responseClass=self.response_class, responseMessages=response_messages)

    def delete(self):
        response_messages = [dict(code=204, message='Deleted')]
        return dict(responseClass=self.response_class, responseMessages=response_messages)

    def put(self):
        parameters = [
            dict(
                name='fullname',
                description='User fullname',
                required=False,
                dataType='str',
                paramType='query'
            ),
            dict(
                name='email',
                description='User e-mail',
                required=False,
                dataType='str',
                paramType='query'
            ),
            dict(
                name='cep_address',
                description='User CEP address',
                required=False,
                dataType='str',
                paramType='query'
            ),
        ]

        response_messages = [
            dict(code=201, message='Updated'),
            dict(code=405, message='Invalid input')
        ]

        return dict(responseClass=self.response_class, parameters=parameters, responseMessages=response_messages)


class UserChangePasswordViewDoc:
    def __init__(self):
        self.response_class = UserModel.__name__

    def put(self):
        parameters = [
            dict(
                name='password',
                description='User password',
                required=True,
                dataType='str',
                paramType='query'
            ),
        ]

        response_messages = [
            dict(code=204, message='Updated'),
            dict(code=405, message='Invalid input')
        ]
        return dict(responseClass=self.response_class, parameters=parameters, responseMessages=response_messages)
