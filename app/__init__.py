
from flask import Flask
from flask_restx import Api
from app.core.initialize_db import initialize_db
from app.settings import get_config
import logging

def create_app(config):
    app = Flask(__name__)
    api = Api(app)
    app.config.from_object(config)

    from app.api.routes import api_namespace
    api.add_namespace(api_namespace)

    if app.config['SHOULD_INIT_DB']:
        try:
            initialize_db()
        except Exception as e:
            logging.error(e)
            logging.error("Could not initialize the database.")
            logging.error("Please make sure that the database is running.")
            exit(1)

    return app
