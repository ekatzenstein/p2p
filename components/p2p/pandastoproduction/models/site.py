from pandastoproduction.models import Page
from pandastoproduction.validate import validate_type


class Site(object):
    def __init__(self, slug: str = None, default_page_id: str = None):
        validate_type('slug', slug, str)
        validate_type('default_page_id', default_page_id, str)
        self._slug = slug
        self._default_page_id = default_page_id

    @property
    def slug(self):
        return self._slug

    @slug.setter
    def slug(self, slug):
        validate_type('slug', slug, str)
        self._slug = slug

    @property
    def default_page_id(self):
        return self._default_page_id

    @default_page_id.setter
    def default_page_id(self, default_page_id):
        validate_type('default_page_id', default_page_id, str)
        self._default_page_id = default_page_id

    def __str__(self):
        return f'Site: slug={self._slug} default_page_id={self._default_page_id}'
