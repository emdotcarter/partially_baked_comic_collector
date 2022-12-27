import os

from dotenv import load_dotenv

from .collector.models import *  # pylint: disable=wildcard-import, unused-wildcard-import

APPLICATION_NAME = "partially_baked_comic_collector"

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, "..", ".env"))


def create_app(config_name):
    # pylint: disable=import-outside-toplevel

    from flask import Flask

    from server.config.config import config

    from .collector.routes import routes as collector_routes
    from .extensions import db, login_manager, migrate

    local_app = Flask(APPLICATION_NAME)
    local_app.config.from_object(config[config_name])

    db.init_app(local_app)
    login_manager.init_app(local_app)

    local_app.register_blueprint(collector_routes)

    migrate.init_app(local_app, db)

    return local_app


app = create_app(os.getenv("FLASK_CONFIG") or "default")
