from flask_restful_swagger import swagger

from api.account.models.user_model import UserModel


@swagger.model
class UserCreateModel(UserModel):
    def __init__(self, full_name: str, email: str, password : str, cep_address: dict):
        self.full_name = full_name
        self.email = email
        self.password = password
        self.cep_address = cep_address


@swagger.model
class UserUpdateModel(UserModel):
    def __init__(self, full_name: str, email: str, cep_address: dict):
        self.full_name = full_name
        self.email = email
        self.cep_address = cep_address


class SignUpViewDoc:
    @staticmethod
    def post():
        parameters = [
            dict(
                name='data',
                description='Create User',
                dataType=UserCreateModel.__name__,
                paramType='body',
            ),
        ]

        response_messages = [
            dict(code=201, message='Created'),
            dict(code=405, message='Invalid input')
        ]

        return dict(responseClass=UserCreateModel.__name__, parameters=parameters, responseMessages=response_messages)


class GetMeViewDoc:
    @staticmethod
    def get():
        response_messages = [dict(code=200, message='Success')]
        return dict(responseMessages=response_messages)

    @staticmethod
    def delete():
        response_messages = [dict(code=204, message='Deleted')]
        return dict(responseMessages=response_messages)

    @staticmethod
    def put():
        parameters = [
            dict(
                name='data',
                description='Update User',
                dataType=UserUpdateModel.__name__,
                paramType='body',
            ),
        ]

        response_messages = [
            dict(code=201, message='Updated'),
            dict(code=405, message='Invalid input')
        ]

        return dict(responseClass=UserUpdateModel.__name__, parameters=parameters, responseMessages=response_messages)


@swagger.model
class UserChangePasswordModelDoc(UserModel):
    def __init__(self, old_password: str, new_password: str):
        self.old_password = old_password
        self.new_password = new_password


class UserChangePasswordViewDoc:
    def __init__(self):
        self.response_class = UserChangePasswordModelDoc.__name__

    def put(self):
        parameters = [
            dict(
                name='data',
                description='User password',
                required=True,
                dataType=self.response_class,
                paramType='body'
            ),
        ]

        response_messages = [
            dict(code=204, message='Updated'),
            dict(code=405, message='Invalid input')
        ]
        return dict(responseClass=self.response_class, parameters=parameters, responseMessages=response_messages)
