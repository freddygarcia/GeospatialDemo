from app import create_app
from app.settings import get_config

Config = get_config()
app = create_app(Config)