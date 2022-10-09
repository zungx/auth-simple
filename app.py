from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from database.dynamodb import DynamoDB
from config.config import Config

config = Config()
db = SQLAlchemy()
dyn = DynamoDB()


def create_app():
    app_main = Flask(__name__)

    app_main.config.from_object(config)

    db.init_app(app_main)

    dyn.init_app(app_main)

    from routes.route_api import api as api_blueprint
    app_main.register_blueprint(api_blueprint, url_prefix='/api')

    return app_main


app = create_app()

if __name__ == '__main__':
    app.run()
