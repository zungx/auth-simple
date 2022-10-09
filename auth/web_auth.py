from flask import request
import jwt
from auth.abstract_auth import AbstractAuth, AuthType
from models.user import User
from app import config
from exceptions.invalid_token import InvalidToken
from exceptions.token_expired import TokenExpired


def get_user_access_token():
    if 'Authorization' in request.headers:
        return request.headers['Authorization'].replace('Bearer ', '')
    return None


class WebAuth(AbstractAuth):

    def __init__(self):
        super(WebAuth, self).__init__(auth_type=AuthType.WEB.value)
        self.access_token_expire_in = config.ACCESS_TOKEN_EXPIRE_IN_MINUTE
        self.refresh_token_expire_in = config.REFRESH_TOKEN_EXPIRE_IN_MINUTE
        self.user_access_token = get_user_access_token()

    def authenticate(self, extra_data=None):
        try:
            if self.user_access_token is None:
                raise InvalidToken('Invalid token')
            payload = self.decode_jwt(self.user_access_token)
            auth_data = self.fetch_access_token(payload['token_id'])
            return auth_data
        except jwt.DecodeError:
            raise InvalidToken('Invalid token')
        except jwt.ExpiredSignatureError:
            raise TokenExpired('TokenExpired')

    def login(self, params):
        if not User.match(params['username'], params['password']):
            return False
        user = User.find_one(params['username'])
        auth_data = dict(user_id=user.id)
        token_payload = self.generate_user_access_token(auth_data)
        auth_data['access_token_id'] = token_payload['token_id']
        refresh_token_payload = self.generate_user_refresh_token(auth_data)
        atk = self.encode_jwt(dict(token_id=token_payload['token_id'], exp=self.access_token_exp()))
        rtk = self.encode_jwt(dict(token_id=refresh_token_payload['token_id'], exp=self.refresh_token_exp()))
        return dict(token_type='Bearer', access_token=atk, refresh_token=rtk)

    def logout(self, params):
        pass

    def refresh(self, params):
        try:
            refresh_token = params.get('refresh_token', None)
            if refresh_token is None:
                raise InvalidToken('Invalid token')
            rtk_payload = self.decode_jwt(refresh_token)
            rtk_data = self.fetch_refresh_token(rtk_payload['token_id'])
            new_atk_payload = self.generate_user_access_token(dict(user_id=rtk_data['user_id']))
            new_rtk_payload = self.generate_user_refresh_token(
                dict(user_id=rtk_data['user_id'], access_token_id=new_atk_payload['token_id'])
            )
            atk = self.encode_jwt(dict(token_id=new_atk_payload['token_id'], exp=self.access_token_exp()))
            rtk = self.encode_jwt(dict(token_id=new_rtk_payload['token_id'], exp=self.refresh_token_exp()))
            return dict(token_type='Bearer', access_token=atk, refresh_token=rtk)
        except jwt.DecodeError:
            raise InvalidToken('Invalid token')
        except jwt.ExpiredSignatureError:
            raise TokenExpired('TokenExpired')
