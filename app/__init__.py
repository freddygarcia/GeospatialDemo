
from flask import Flask
from project.settings import get_config


def create_app():
    Config = get_config()()
    app = Flask(__name__)
    app.config.from_object(Config)

    return app
