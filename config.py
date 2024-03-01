import os 
from datetime import timedelta

DEBUG = bool(int(os.getenv('FLASK_DEBUG', 0)))
FLASK_APP = os.getenv('FLASK_APP', 'app')
PROPAGATE_EXCEPTIONS = True

API_TITLE = "store apis"
API_VERSION = "v1"
OPENAPI_VERSION = "3.0.3"
OPENAPI_URL_PREFIX = "/"
OPENAPI_SWAGGER_UI_PATH = "/swagger"
OPENAPI_SWAGGER_UI_URL = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', "sqlite:///stores.db")
SQLALCHEMY_TRACK_MODIFICATIONS = False

JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', '381836fe163039ab7bcd0a84bf54dded9fbd4269')
JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)
JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=30)