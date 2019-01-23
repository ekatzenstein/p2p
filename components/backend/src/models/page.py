"""Page model."""
from datetime import datetime

from .models import db, APIModel, sortable

@sortable('name')
class Page(APIModel):
    """Representation of a Page."""

    __tablename__ = 'page'

    id_ = db.Column('id', db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String)
    site_id = db.Column(db.Integer, db.ForeignKey(
                'site.id', ondelete='CASCADE'), nullable=False)
