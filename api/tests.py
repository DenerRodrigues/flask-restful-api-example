from flask_script import Command

from api.app import app
from api.account.tests import get_me, signup
from api.authentication.tests import get_token
from api.stock.tests import create_wish

BASE_URL = app.config.get('BASE_URL')


class TestsCommand(Command):

    def run(self):
        # signup()
        token = get_token()
        # get_me(token)
        create_wish(token)
