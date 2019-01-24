"""Schemas for function-based views."""
from marshmallow import fields as field, Schema

from models.page import Page
from models.dataframe import Dataframe


class PageSchema(Schema):
    id = field.Int(attribute='id_', dump_only=True)
    title = field.Str()
    content = field.Str()
    site_id = field.Str(dump_only=True)
    dataframe_id = field.Str()

    # pylint: disable=too-few-public-methods
    class Meta:
        """Meta class sets class-wide options."""

        strict = True


class DataframeSchema(Schema):
    id = field.Int(attribute='id_', dump_only=True)
    digest = field.Str(dump_only=True)
    url = field.Str(dump_only=True)

    # pylint: disable=too-few-public-methods
    class Meta:
        """Meta class sets class-wide options."""

        strict = True
