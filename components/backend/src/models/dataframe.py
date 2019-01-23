"""Dataframe model."""
from .models import db, APIModel, sortable

@sortable('name')
class Dataframe(APIModel):
    """Representation of a Dataframe."""

    __tablename__ = 'dataframe'

    id_ = db.Column('id', db.Integer, primary_key=True)
    digest = db.Column(db.String, nullable=False)
    url = db.Column(db.String, nullable=False)
