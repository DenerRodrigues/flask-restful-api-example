class BaseView:

    @staticmethod
    def response(status_code=200, success=True, result=None):
        return {'code': status_code, 'success': success, 'result': result}, status_code

    def not_found(self):
        return self.response(404, False, 'Not Found')
