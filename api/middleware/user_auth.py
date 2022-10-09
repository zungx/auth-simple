from functools import wraps
from flask import request
from auth.auth_factory import AuthFactory
from auth.abstract_auth import AuthType


def login_required(f):
    @wraps(f)
    def wraps_request(*args, **kwargs):
        auth = AuthFactory.get_auth(AuthType.WEB.value)
        user_auth = auth.authenticate()
        request.user_auth = user_auth
        return f(*args, **kwargs)

    return wraps_request
