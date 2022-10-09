import os
import logging


class Config(object):

    DEBUG = True
    TESTING = True
    LOG_LEVEL = logging.DEBUG
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    DB_HOST = os.getenv('DB_HOST', '')
    DB_PORT = os.getenv('DB_PORT', '')
    DB_DATABASE = os.getenv('DB_DATABASE', '')
    DB_USERNAME = os.getenv('DB_USERNAME', '')
    DB_PASSWORD = os.getenv('DB_PASSWORD', '')
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID', '')
    AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY', '')
    AWS_REGION_NAME = os.getenv('AWS_REGION_NAME', '')
    DYNAMODB_ENDPOINT_URL = os.getenv('DYNAMODB_ENDPOINT_URL', '')
    DYNAMODB_TABLE_ACCESS_TOKEN = os.getenv('DYNAMODB_TABLE_ACCESS_TOKEN', '')
    DYNAMODB_TABLE_REFRESH_TOKEN = os.getenv('DYNAMODB_TABLE_REFRESH_TOKEN', '')
    JWT_SECRET = os.getenv('JWT_SECRET', '')
    ACCESS_TOKEN_EXPIRE_IN_MINUTE = os.getenv('ACCESS_TOKEN_EXPIRE_IN_MINUTE', '')
    REFRESH_TOKEN_EXPIRE_IN_MINUTE = os.getenv('REFRESH_TOKEN_EXPIRE_IN_MINUTE', '')
