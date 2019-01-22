"""Site model."""
from datetime import datetime

from .models import db, sortable

@sortable('created_at', 'name')
class Site(db.Model):
    """Representation of a Tag."""

    __bind_key__ = 'metadata'
    __tablename__ = 'site'

    id_ = db.Column('id', db.Integer, nullable=False, unique=True, primary_key=True, autoincrement=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    name = db.Column(db.String, nullable=False, unique=True)
    slug = db.Column(db.String)
    default_page_id = db.Column(db.String)
