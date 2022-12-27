import os

from sqlalchemy.engine import URL


class Config:  # pylint: disable=too-few-public-methods
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SECRET_KEY = os.getenv("SECRET_KEY")
    SESSION_COOKIE_NAME = os.getenv("SESSION_COOKIE_NAME")
    STATIC_FOLDER = "static"
    TEMPLATES_FOLDER = "templates"
    TESTING = False


class ProdConfig(Config):  # pylint: disable=too-few-public-methods
    FLASK_ENV = "production"
    DATABASE_URI = os.getenv("")


class DevConfig(Config):  # pylint: disable=too-few-public-methods
    FLASK_ENV = "development"
    TESTING = True
    SQLALCHEMY_DATABASE_URI = URL.create(
        drivername="postgresql",
        username=os.getenv("POSTGRES_USERNAME"),
        password=os.getenv("POSTGRES_PASSWORD"),
        host=os.getenv("POSTGRES_HOST"),
        port=os.getenv("POSTGRES_PORT"),
        database=os.getenv("POSTGRES_DATABASE"),
    )


config = {
    "development": DevConfig,
    "testing": DevConfig,
    "production": ProdConfig,
    "default": DevConfig,
}
