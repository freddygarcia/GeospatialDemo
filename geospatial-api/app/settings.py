import os
import dotenv
import logging

logging.basicConfig(level=logging.INFO)
dotenv.load_dotenv()


class BaseConfig:
    """Base configuration"""
    TESTING = False

    DB_ENGINE = os.getenv('DB_ENGINE')
    DB_USER = os.getenv('DB_USER')
    DB_PASSWORD = os.getenv('DB_PASSWORD')
    DB_HOST = os.getenv('DB_HOST')
    DB_PORT = os.getenv('DB_PORT')
    DB_NAME = os.getenv('DB_NAME')
    FLASK_ENV = os.getenv('FLASK_ENV')
    DEVELOPMENT = os.getenv('FLASK_ENV') == 'development'

    SQLALCHEMY_DATABASE_URI = \
        f"{DB_ENGINE}://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # If the database should be reset on application start
    SHOULD_INIT_DB = os.getenv('INIT_DB', True)


class DevelopmentConfig(BaseConfig):
    """Development configuration"""
    TESTING = False


class TestingConfig(BaseConfig):
    """Testing configuration"""
    TESTING = True
    SHOULD_INIT_DB = False


class ProductionConfig(BaseConfig):
    """Production configuration"""
    pass


def get_config():
    """Get configuration based on environment"""

    mode = os.getenv('FLASK_ENV', 'production')

    config = {
        'development': DevelopmentConfig,
        'testing': TestingConfig,
        'production': ProductionConfig
    }[mode]

    return config
