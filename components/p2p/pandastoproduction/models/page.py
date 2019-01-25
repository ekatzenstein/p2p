import json
from typing import List, Union

from jupyter_react import Component


from pandastoproduction.validate import validate_type, validate_type_list


class SimpleEncoder(json.JSONEncoder):
    def default(self, o):  # pylint: disable=E0202
        return o.__dict__


class PageContent(object):
    _render_type = 'any'

    @property
    def render_type(self):
        return self._render_type

    def __str__(self):
        return f'PageContent: type={self._render_type}'

    def to_json(self):
        obj = {
            'render_type': self._render_type,
        }
        data = {}
        for key in obj:
            if obj[key] is not None:
                data[key] = obj[key]
        return data


class _TextContent(PageContent):
    _render_type = "text"

    def __init__(self, data: str = None):
        validate_type('data', data, str)
        self._data = data

    @property
    def data(self):
        return self._data

    def to_json(self):
        obj = {
            **super().to_json(),
            'data': self._data,
        }
        data = {}
        for key in obj:
            if obj[key] is not None:
                data[key] = obj[key]
        return data


class Paragraph(_TextContent):
    _render_type = "paragraph"


class Title(_TextContent):
    _render_type = "title"


class SubTitle(_TextContent):
    _render_type = "subtitle"


class Histogram(PageContent):
    '''
    Histogram(required: df (with 1 column), 
              optional: nbins (int))
    '''

    _render_type = "histogram"

    def __init__(self, series: str = None, bins: int = 10):
        self._series = series
        self._bins = bins

    @property
    def series(self):
        return self._bins

    @property
    def bins(self):
        return self._series

    def to_json(self):
        obj = {
            **super().to_json(),
            'bins': self._bins,
            'series': self._series,
        }
        data = {}
        for key in obj:
            if obj[key] is not None:
                data[key] = obj[key]
        return data


class Boxplot(PageContent):
    '''
    Boxplot(required: df (with >= 1 column),
            optional: grouping - different boxplot for each group, 
            ? optional: whisker (boolean))
    '''

    _render_type = "boxplot"

    def __init__(self, xvar: str = None, grouping: str = None):
        self._xvar = xvar
        self._grouping = grouping

    @property
    def xvar(self):
        return self._xvar

    @property
    def grouping(self):
        return self._grouping

    def to_json(self):
        obj = {
            **super().to_json(),
            'grouping': self._grouping,
            'xvar': self._xvar,
        }
        data = {}
        for key in obj:
            if obj[key] is not None:
                data[key] = obj[key]
        return data


class Scatterplot(PageContent):
    '''
    Scatterplot(required: x_df (with 1 column),
                          y_df (with 1 column)
                optional: )
    '''

    _render_type = "scatterplot"

    def __init__(self, xvar: str = None, yvar: str = None):
        self._xvar = xvar
        self._yvar = yvar

    @property
    def yvar(self):
        return self._yvar

    def xvar(self):
        return self._xvar

    def to_json(self):
        obj = {
            **super().to_json(),
            'yvar': self._yvar,
            'xvar': self._xvar,
        }
        data = {}
        for key in obj:
            if obj[key] is not None:
                data[key] = obj[key]
        return data


class Page(Component):
    module = 'P2PBaseComponent'

    def __init__(self, title: str = None, content: List[PageContent] = []):
        validate_type('title', title, str)
        validate_type_list('content', content, PageContent)
        self._title = title
        self._content = content
        self._id = None
        super().__init__(target_name='p2p', props={'groups': [c.to_json() for c in self._content]})
        self.on_msg(self._handle_msg)

    def _handle_msg(self, msg):
        print(msg)

    @property
    def title(self):
        return self._title

    @property
    def id(self):
        return self._id

    def __str__(self):
        return f'Page: title="{self._title}" content={self._content}'

    def to_json(self):
        obj = {
            'id': self._id,
            'title': self._title,
            'content': [c.to_json() for c in self._content],
        }
        data = {}
        for key in obj:
            if obj[key] is not None:
                data[key] = obj[key]
        return data
