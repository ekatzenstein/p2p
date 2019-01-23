"""SQLAlchemy database object and base class for all API-exposed models."""
import uuid

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import UUIDType


db = SQLAlchemy()  # type: SQLAlchemy


# pylint: disable=too-few-public-methods,no-self-use
class APIModel(db.Model):
    """Base class for providing a consistent representation of resource objects to the API."""

    __abstract__ = True

    @classmethod
    def resource_type(cls):
        """Return a string that describes what type of resource this is."""
        table_name = cls.__tablename__
        if table_name.endswith('s'):
            return table_name[:-1]
        return table_name

    def meta(self):
        """Return a dict of meta information about the resource.

        This information can not be represented as an attribute or relationship. Commonly used
        for contextual information related to a search query.
        """
        return getattr(self, 'meta_dict', None)

    def load_meta(self, key, value):
        """Load meta information for this Dataset, which will be serialized in the `meta` dict under the given key."""
        # pylint: disable=attribute-defined-outside-init
        self.meta_dict = meta = getattr(self, 'meta_dict', {})
        meta[key] = value

    @classmethod
    def require_by_id(cls, id_):
        """Retrieve the resource with the primary key *id_*.

        :param id_: The primary key identifier for the resource
        """
        type_detail = {'type': cls.__name__.lower()}
        if isinstance(cls.id_.type, UUIDType):
            if not isinstance(id_, uuid.UUID):
                try:
                    id_ = uuid.UUID(id_)
                except (TypeError, ValueError):
                    raise APIError('resource_not_found', detail=type_detail)
        resource = cls.query.get(id_)
        if resource is None:
            raise APIError('resource_not_found', detail=type_detail)
        return resource


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
