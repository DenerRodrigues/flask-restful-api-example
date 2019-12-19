from api.account.tests import get_me


class Tests:
    @staticmethod
    def run():
        print(get_me())


if __name__ == '__main__':
    Tests().run()
