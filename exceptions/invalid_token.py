from exceptions.app_exception import AppException


class InvalidToken(AppException):

    def __init__(self, message, payload=None):
        super(InvalidToken, self).__init__(message, 401, payload)
