import io
import json
import requests

from pandastoproduction.models import DataFrame, Page
from pandastoproduction.validate import validate_not_null


def print_json(obj):
    if obj is None:
        print('None')
        return
    try:
        obj = obj.decode('utf-8')
    except AttributeError:
        pass
    try:
        print(json.dumps(json.loads(obj), indent=4, sort_keys=True))
    except:
        print(obj)


class ApiClient(object):
    """API Client"""

    def __init__(self, api_base_url: str):
        self._api_base_url = api_base_url.rstrip('/')

    def _request(self, method: str, path: str, **kwargs):
        url = '{}/{}'.format(
            self._api_base_url,
            path.lstrip('/')
        )
        resp = requests.request(
            method,
            url,
            **kwargs,
        )
        print('Request:')
        print(method + ' ' + url)
        print_json(resp.request.body)
        print('Response:')
        print_json(resp.content)
        return resp

    def create_page(self, page: Page):
        resp = self._request('POST', f'/pages/', json=page.to_json())
        page.id = resp.json()['id']

    def create_dataframe(self, dataframe: DataFrame):
        # resp = self._request('POST', '/dataframes/')
        # dataframe.id = resp.json()['id']
        stream = io.StringIO()
        dataframe.df.to_csv(stream)
        files = {'file': ('dataframe.csv', stream)}
        self._request('POST', f'/dataframes/', files=files)

    def update_page(self, page: Page):
        validate_not_null('id', page.id)
        self._request('PUT', f'/pages/{page.id}', json=page.to_json())

    def update_dataframe(self, dataframe: DataFrame):
        validate_not_null('id', dataframe.id)
        stream = io.StringIO()
        dataframe.df.to_csv(stream)
        files = {'file': ('dataframe.csv', stream)}
        self._request('PUT', f'/dataframes/{dataframe.id}', files=files)

    def create_or_update_page(self, page: Page):
        if page.id is not None:
            self.update_page(page)
        else:
            self.create_page(page)

    def create_or_update_dataframe(self, dataframe: DataFrame):
        if dataframe.id is not None:
            self.update_dataframe(dataframe)
        else:
            self.create_dataframe(dataframe)
