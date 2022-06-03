
from flask import Flask
from flask_restx import Api
from app.core.initialize_db import initialize_db
from app.settings import get_config


def create_app():
    Config = get_config()()
    app = Flask(__name__)
    api = Api(app)
    app.config.from_object(Config)

    from app.api.routes import api_namespace
    api.add_namespace(api_namespace)

    if app.config['SHOULD_INIT_DB']:
        initialize_db()

    return app
