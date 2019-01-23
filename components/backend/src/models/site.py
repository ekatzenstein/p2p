"""Site model."""
from datetime import datetime

from .models import db, APIModel, sortable

@sortable('name')
class Site(APIModel):
    """Representation of a Site."""

    __tablename__ = 'site'

    id_ = db.Column('id', db.Integer, primary_key=True)
    name = db.Column(db.String)
    slug = db.Column(db.String)
    default_page_id = db.Column(db.String, nullable=True)
    pages = db.relationship('Page', backref='page',
                               order_by='Page.title')
