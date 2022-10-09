from exceptions.app_exception import AppException


class TokenRevoked(AppException):

    def __init__(self, message, payload=None):
        super(TokenRevoked, self).__init__(message, 401, payload)
