from datetime import datetime

import sqlalchemy
from flask_login import LoginManager
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_sqlalchemy.model import Model
from flask_cors import CORS


class Base(Model):  # pylint: disable=too-few-public-methods
    __abstract__ = True

    id = sqlalchemy.Column(sqlalchemy.BigInteger, primary_key=True)
    created_at = sqlalchemy.Column(
        sqlalchemy.DateTime, nullable=False, default=datetime.now()
    )
    updated_at = sqlalchemy.Column(
        sqlalchemy.DateTime,
        nullable=False,
        default=datetime.now(),
        onupdate=datetime.now(),
    )


db = SQLAlchemy(model_class=Base)
migrate = Migrate()
login_manager = LoginManager()
marshmallow = Marshmallow()
cors = CORS()