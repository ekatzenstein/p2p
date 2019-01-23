import json
import requests

from pandastoproduction.models import DataFrame, Site, Page


class SimpleEncoder(json.JSONEncoder):
    def default(self, o):  # pylint: disable=E0202
        return o.__dict__


class ApiClient(object):
    """API Client"""

    def __init__(self, api_base_url: str):
        self._api_base_url = api_base_url

    def _request(self, method: str, path: str, **kwargs):
        url = f'{self._api_base_url}/{path}'
        resp = requests.request(
            method,
            url,
            **kwargs,
        )
        return resp

    def create_page(self, page: Page):
        site_id = page.site_id
        self._request('POST', f'/sites/{site_id}/pages/', json=json.dumps(page, cls=SimpleEncoder))

    def create_site(self, site: Site):
        self._request('POST', '/sites/', json=json.dumps(site, cls=SimpleEncoder))

    def create_dataframe(self, dataframe: DataFrame):
        df_resp = self._request('POST', '/dataframes/', json=json.dumps(dataframe, cls=SimpleEncoder))
        dataframe_id = df_resp.json()['id']
        self._request('POST', f'/dataframes/{dataframe_id}', json=dataframe.df)
