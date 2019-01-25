import json
from typing import List, Union

from jupyter_react import Component
import pandas as pd


from pandastoproduction.models import DataFrame
from pandastoproduction.validate import validate_type, validate_type_list


class SimpleEncoder(json.JSONEncoder):
    def default(self, o):  # pylint: disable=E0202
        return o.__dict__


class PageContent(object):
    render_type = "any"

    def __str__(self):
        return f'PageContent: type={self.render_type}'

    def to_json(self, include_df=False, **kwargs):
        obj = self.__dict__.copy()
        obj["render_type"] = self.render_type
        for key in obj:
            if obj[key] is None:
                obj.pop(key, None)
        return obj


class _TextContent(PageContent):
    render_type = "any_text"

    def __init__(self, data: str, **kwargs):
        validate_type('data', data, str)
        self.data = data
        self.__dict__.update(kwargs)

    def to_json(self, **kwargs):
        obj = self.__dict__.copy()
        obj["render_type"] = self.render_type
        for key in obj:
            if obj[key] is None:
                obj.pop(key, None)
        return obj


class Paragraph(_TextContent):
    render_type = "paragraph"


class Title(_TextContent):
    render_type = "title"


class SubTitle(_TextContent):
    render_type = "subtitle"


class _ChartContent(PageContent):
    render_type = "any_chart"

    def __init__(self, dataframe: Union[pd.DataFrame, DataFrame], **kwargs):
        if isinstance(dataframe, pd.DataFrame):
            self.dataframe = DataFrame(dataframe)
        elif isinstance(dataframe, DataFrame):
            self.dataframe = dataframe
        self.__dict__.update(kwargs)

    def to_json(self, include_df=False, **kwargs):
        obj = self.__dict__.copy()
        obj["render_type"] = self.render_type
        obj.pop('dataframe', None)
        if include_df:
            obj['data'] = self.dataframe.to_csv()
        for key in obj:
            if obj[key] is None:
                obj.pop(key, None)
        return obj


class Histogram(_ChartContent):
    render_type = "histogram"


class Boxplot(_ChartContent):
    render_type = "boxplot"


class Scatterplot(_ChartContent):
    render_type = "scatter"


class Page(Component):
    module = 'P2PBaseComponent'

    def __init__(self, title: str = None, content: List[PageContent] = []):
        validate_type('title', title, str)
        validate_type_list('content', content, PageContent)
        self.title = title
        self.content = content
        self.id = None
        super().__init__(target_name='p2p', props={'groups': [c.to_json(include_df=True) for c in self.content]})
        self.on_msg(self._handle_msg)

    def _handle_msg(self, msg):
        print(msg)

    def __str__(self):
        return f'Page: title="{self.title}" content={self.content} id={self.id}'

    def to_json(self, **kwargs):
        obj = self.__dict__.copy()
        obj['content'] = [c.to_json() for c in self.content]
        for key in obj:
            if obj[key] is None:
                obj.pop(key, None)
        return obj
