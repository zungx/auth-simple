from flask import Blueprint
from api.login import do_login
from api.health import health
from api.user_me import user_me
from api.auth_token import request_access_token
from exceptions.error_handler import handle_exception
from exceptions.app_exception import AppException


api = Blueprint('api', __name__)

api.add_url_rule('/health', view_func=health, methods=['GET'])
api.add_url_rule('/login', view_func=do_login, methods=['POST'])
api.add_url_rule('/auth/access_token', view_func=request_access_token, methods=['POST'])
api.add_url_rule('/user_me', view_func=user_me, methods=['GET'])
api.register_error_handler(AppException, handle_exception)
