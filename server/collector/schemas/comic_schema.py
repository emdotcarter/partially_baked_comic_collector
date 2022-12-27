from server.extensions import marshmallow

from ..models.comic import Comic


class ComicSchema(marshmallow.SQLAlchemySchema):
    class Meta:
        model = Comic

    title = marshmallow.auto_field()


comic_schema = ComicSchema()
