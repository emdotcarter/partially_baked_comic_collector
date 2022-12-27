from flask import Blueprint, make_response, request

from server.extensions import db

from .models import Comic

routes = Blueprint("routes", __name__)


@routes.route("/1/comics", methods=["POST"])
def create_comic():
    comic = Comic(
        title=request.get_json()["title"],
    )
    db.session.add(comic)  # pylint: disable=no-member
    db.session.commit()  # pylint: disable=no-member

    return make_response(comic.serialize())


@routes.route("/1/comics", methods=["GET"])
def list_comics():
    # pylint: disable=no-member
    return make_response([c.serialize() for c in db.session.query(Comic).all()])
