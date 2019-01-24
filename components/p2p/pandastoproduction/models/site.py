from typing import List, Union

from pandastoproduction.validate import validate_type, validate_type_list


class Site(object):
    def __init__(self, name: str, slug: str = None, default_page: object = None, pages: List[object] = []):
        validate_type('name', name, str)
        validate_type('slug', slug, str)
        validate_type('default_page', default_page, object)
        self._name = name
        self._slug = slug
        self._default_page = default_page
        self._id = None
        self._pages = pages

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        validate_type('name', name, str)
        self._name = name

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        validate_type('id', id, int)
        self._id = id

    @property
    def slug(self):
        return self._slug

    @slug.setter
    def slug(self, slug):
        validate_type('slug', slug, str)
        self._slug = slug

    @property
    def default_page(self):
        return self._default_page

    @default_page.setter
    def default_page(self, default_page):
        validate_type('default_page', default_page, str)
        self._default_page = default_page

    @property
    def pages(self):
        return self._pages

    def add_pages(self, pages: Union[object, List[object]]):
        if isinstance(pages, list):
            validate_type_list('pages', pages, object)
            self._pages.extend(pages)
        else:
            validate_type('pages', pages, object)
            self._pages.append(pages)

    def __str__(self):
        return f'Site: slug={self._slug} default_page={self._default_page} name={self._name} id={self._id}'

    def to_json(self):
        obj = {
            'id': self._id,
            'name': self._name,
            'slug': self._slug,
            'default_page_id': self._default_page.id if self._default_page else None,
        }
        data = {}
        for key in obj:
            if obj[key] is not None:
                data[key] = obj[key]
        return data
