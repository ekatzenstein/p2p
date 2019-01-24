from typing import List

from pandastoproduction.api_client import ApiClient
from pandastoproduction.config import CONFIG
from pandastoproduction.models import DataFrame, Page, Site
from pandastoproduction.validate import validate_type_list


def publish(dataframes: List[DataFrame] = [], sites: List[Site] = []):
    validate_type_list('dataframes', dataframes, DataFrame)
    validate_type_list('sites', sites, Site)

    print('Publishing..')

    client = ApiClient(CONFIG['api_base_url'])
    for site in sites:
        client.create_or_update_site(site)
        for page in site.pages:
            client.create_or_update_page(page)
    for dataframe in dataframes:
        client.create_or_update_dataframe(dataframe)

    print('Done!')
