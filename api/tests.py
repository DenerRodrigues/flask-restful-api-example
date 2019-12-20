from flask_script import Command

from api.app import app
from api.account.tests import get_me

BASE_URL = app.config.get('BASE_URL')


class TestsCommand(Command):

    def run(self):
        get_me()
