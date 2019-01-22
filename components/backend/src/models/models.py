"""SQLAlchemy database object and base class for all API-exposed models."""
import uuid

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import UUIDType


db = SQLAlchemy()  # type: SQLAlchemy


def sortable(*args):
    """Return a decorator for adding sort_query() to an APIModel."""
    def decorator(cls):
        """Add sort_query() to the given *cls*."""
        def sort_query(query, fields):
            """Sort a SQLAlchemy *query* by the given *fields*."""
            if not fields:
                return query
            if isinstance(fields, str):
                fields = fields.split(',')
            orderings = []
            for field in fields:
                attr = field.lstrip('-')
                if args and attr not in args:
                    raise APIError('sort_not_allowed',
                                   detail={'unallowed': attr, 'allowed': args})
                ordering = getattr(cls, attr)
                if field.startswith('-'):
                    ordering = ordering.desc()
                orderings.append(ordering)
            return query.order_by(*orderings)
        cls.sort_query = sort_query
        return cls
    return decorator
