import sqlalchemy

from server.extensions import db


class Comic(db.Model):
    title = sqlalchemy.Column(sqlalchemy.Text, nullable=False)

    def serialize(self):
        return {
            "title": self.title,
        }
