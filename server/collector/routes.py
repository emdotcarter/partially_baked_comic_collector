from flask import Blueprint, make_response, request

from server.extensions import db

from .models import Comic
from .schemas.comic_schema import comic_schema, comics_schema

routes = Blueprint("routes", __name__)


@routes.route("/1/comics", methods=["POST"])
def create_comic():
    comic = Comic(
        title=request.get_json()["title"],
    )
    db.session.add(comic)  # pylint: disable=no-member
    db.session.commit()  # pylint: disable=no-member

    return make_response(comics_schema.dump(comic))


@routes.route("/1/comics", methods=["GET"])
def list_comics():
    # pylint: disable=no-member
    return make_response([comic_schema.dump(c) for c in db.session.query(Comic).all()])
