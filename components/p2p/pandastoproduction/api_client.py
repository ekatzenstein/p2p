import json
import requests

from pandastoproduction.models import DataFrame, Site, Page
from pandastoproduction.validate import validate_not_null


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
        print(json.dumps(json.loads(resp.request.body.decode('utf-8')), indent=4, sort_keys=True))
        print('Response:')
        print(json.dumps(json.loads(resp.content.decode('utf-8')), indent=4, sort_keys=True))
        return resp

    def create_page(self, page: Page):
        validate_not_null('site_id', page.site.id)
        resp = self._request('POST', f'/sites/{page.site.id}/pages/', json=page.to_json())
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
