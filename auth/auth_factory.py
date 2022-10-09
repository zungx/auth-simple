from auth.web_auth import WebAuth
from auth.mobile_auth import MobileAuth
from auth.abstract_auth import AuthType


class AuthFactory:

    auth = None

    @staticmethod
    def get_auth(auth_type):
        if AuthFactory.auth is not None:
            return AuthFactory.auth

        if auth_type == AuthType.WEB.value:
            return WebAuth()

        if auth_type == AuthType.APP.value:
            return MobileAuth()

        raise Exception('Auth Not found')
