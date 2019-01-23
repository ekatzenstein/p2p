import json
from typing import List, Union

from pandastoproduction.validate import validate_type, validate_type_list


class SimpleEncoder(json.JSONEncoder):
    def default(self, o):  # pylint: disable=E0202
        return o.__dict__


class PageContent(object):
    def __init__(self, content_type: str):
        validate_type('content_type', content_type, str)
        self._content_type = content_type

    @property
    def content_type(self):
        return self._content_type

    @content_type.setter
    def content_type(self, content_type: str):
        validate_type('content_type', content_type, str)
        self._content_type = content_type

    def __str__(self):
        return f'PageContent: type={self._content_type}'


class Paragraph(PageContent):
    CONTENT_TYPE = "paragraph"

    def __init__(self, text: str = None):
        super().__init__(self.CONTENT_TYPE)
        validate_type('text', text, str)
        self._text = text

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, text):
        validate_type('text', text, str)
        self._text = text


class Histogram(PageContent):
    CONTENT_TYPE = "histogram"

    def __init__(self):
        super().__init__(self.CONTENT_TYPE)


class Boxplot(PageContent):
    CONTENT_TYPE = "boxplot"

    def __init__(self):
        super().__init__(self.CONTENT_TYPE)


class Scatterplot(PageContent):
    CONTENT_TYPE = "scatterplot"

    def __init__(self):
        super().__init__(self.CONTENT_TYPE)


class Page(object):
    def __init__(self, title: str = None, content: List[PageContent] = [], site_id: str = None):
        validate_type('title', title, str)
        validate_type_list('content', content, PageContent)
        validate_type('site_id', site_id, str)
        self._title = title
        self._content = content
        self._site_id = site_id

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        validate_type('title', title, str)
        self._title = title

    @property
    def site_id(self):
        return self._site_id

    @site_id.setter
    def site_id(self, site_id):
        validate_type('site_id', site_id, str)
        self._site_id = site_id

    def add_content(self, content: Union[PageContent, List[PageContent]]):
        if isinstance(content, list):
            validate_type_list('content', content, PageContent)
            self._content.extend(content)
        else:
            validate_type('content', content, PageContent)
            self._content.append(content)

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        validate_type('id', id, int)
        self._id = id

    def __str__(self):
        return f'Page: title="{self._title}" content={self._content} site_id={self._site_id} id={self._id}'

    def to_json(self):
        obj = {
            'id': self._id,
            'title': self._title,
            'site_id': self._site_id,
            'content': json.dumps(self._content, cls=SimpleEncoder),
        }
        data = {}
        for key in obj:
            if obj[key] is not None:
                data[key] = obj[key]
        return data
