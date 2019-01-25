from typing import List

from pandastoproduction.api_client import ApiClient
from pandastoproduction.config import CONFIG
from pandastoproduction.models import DataFrame, Page
from pandastoproduction.validate import validate_type_list


def publish(pages: List[Page] = [], dataframes: List[DataFrame] = []):
    validate_type_list('pages', pages, Page)
    validate_type_list('dataframes', dataframes, DataFrame)

    print('Publishing..')

    client = ApiClient(CONFIG['api_base_url'])
    for page in pages:
        client.create_or_update_page(page)
    for dataframe in dataframes:
        client.create_or_update_dataframe(dataframe)

    print('Done!')
