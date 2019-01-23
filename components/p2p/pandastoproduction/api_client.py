import requests

from pandastoproduction.models import DataFrame, Site, Page


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
        print(resp.request.body.decode('utf-8'))
        print('Response:')
        print(resp.content.decode('utf-8'))
        return resp

    def create_page(self, page: Page):
        site_id = page.site_id
        if site_id is None:
            raise ValueError('Page site_id is missing.')
        resp = self._request('POST', f'/sites/{site_id}/pages/', json=page.to_json())
        page.id = resp.json()['id']

    def create_site(self, site: Site):
        resp = self._request('POST', '/sites/', json=site.to_json())
        site.id = resp.json()['id']

    def create_dataframe(self, dataframe: DataFrame):
        pass  # TODO

    def update_page(self, page: Page):
        pass  # TODO

    def update_site(self, site: Site):
        pass  # TODO

    def update_dataframe(self, dataframe: DataFrame):
        pass  # TODO

    def create_or_update_page(self, page: Page):
        pass  # TODO

    def create_or_update_site(self, site: Site):
        pass  # TODO

    def create_or_update_dataframe(self, dataframe: DataFrame):
        pass  # TODO
