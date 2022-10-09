import jwt, uuid, os
from datetime import datetime
import time
from enum import Enum
from abc import abstractmethod, ABC
from app import config
from models.dynamodb.user_refresh_token import UserRefreshToken as DynRefreshToken
from models.dynamodb.user_access_token import UserAccessToken as DynAccessToken
from exceptions.token_revoked import TokenRevoked
from exceptions.token_expired import TokenExpired


class AuthType(Enum):
    WEB = 'web'
    APP = 'app'


class AbstractAuth(ABC):

    def __init__(self, auth_type=None):
        self.auth_type = auth_type
        self.access_token_expire_in = 15
        self.refresh_token_expire_in = 60
        self.dynAccessToken = DynAccessToken()
        self.dynRefreshToken = DynRefreshToken()

    @abstractmethod
    def authenticate(self, extra_data=None):
        pass

    @abstractmethod
    def login(self, params):
        pass

    @abstractmethod
    def logout(self, params):
        pass

    @abstractmethod
    def refresh(self, params):
        pass

    def encode_jwt(self, payload):
        return jwt.encode(payload, config.JWT_SECRET, algorithm="HS256")

    def decode_jwt(self, token):
        return jwt.decode(token, config.JWT_SECRET, algorithms=["HS256"])

    def access_token_exp(self):
        return int(time.time()) + int(self.access_token_expire_in) * 60

    def refresh_token_exp(self):
        return int(time.time()) + int(self.refresh_token_expire_in) * 60

    def generate_token_id(self):
        return os.urandom(40).hex()

    def generate_user_access_token(self, auth_data):
        token_id = self.generate_token_id()
        now = datetime.now()
        token_payload = {
            'token_id': token_id,
            'user_id': auth_data['user_id'],
            'expires_at': self.access_token_exp(),
            'created_at': str(now),
            'updated_at': str(now)
        }
        print(token_payload)
        self.dynAccessToken.table.put_item(Item={
            'id': str(token_id),
            'data': token_payload
        })

        return token_payload

    def generate_user_refresh_token(self, auth_data):
        refresh_token_id = self.generate_token_id()
        now = datetime.now()
        refresh_token_payload = {
            'token_id': refresh_token_id,
            'access_token_id': auth_data['access_token_id'],
            'user_id': auth_data['user_id'],
            'expires_at': self.refresh_token_exp(),
            'created_at': str(now),
            'updated_at': str(now)
        }
        self.dynRefreshToken.table.put_item(Item={
            'id': str(refresh_token_id),
            'data': refresh_token_payload
        })

        return refresh_token_payload

    def fetch_access_token(self, token_id):
        response = self.dynAccessToken.table.get_item(Key={
            'id': str(token_id)
        })
        item = response.get('Item', None)
        if item is None:
            raise TokenRevoked('Token revoked')
        expires_at = item['data']['expires_at']
        now = int(time.time())
        if now > expires_at:
            raise TokenExpired('Token expired')

        return dict(token_id=item.get('id', None), expires_at=expires_at, user_id=item['data']['user_id'])

    def fetch_refresh_token(self, refresh_token_id):
        response = self.dynRefreshToken.table.get_item(Key={
            'id': str(refresh_token_id)
        })
        item = response.get('Item', None)
        if item is None:
            raise TokenRevoked('Token revoked')
        expires_at = item['data']['expires_at']
        now = int(time.time())
        if now > expires_at:
            raise TokenExpired('Token expired')

        return dict(token_id=item.get('id', None), expires_at=expires_at, user_id=item['data']['user_id'])
