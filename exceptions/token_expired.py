from exceptions.app_exception import AppException


class TokenExpired(AppException):

    def __init__(self, message, payload=None):
        super(TokenExpired, self).__init__(message, 401, payload)

