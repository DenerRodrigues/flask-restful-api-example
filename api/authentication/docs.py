class AuthTokenViewDoc:
    @staticmethod
    def post():
        parameters = [
            dict(
                name='username',
                description='User e-mail',
                required=True,
                dataType='str',
                paramType='header',
            ),
            dict(
                name='password',
                description='User password',
                required=True,
                dataType='str',
                paramType='header',
            ),
        ]
        return dict(parameters=parameters)
