from typing import List

from pandastoproduction.api_client import ApiClient
from pandastoproduction.config import CONFIG
from pandastoproduction.models import DataFrame, Page
from pandastoproduction.validate import validate_type_list


def publish(pages: List[Page] = [], verbose=False):
    validate_type_list('pages', pages, Page)

    client = ApiClient(CONFIG['api_base_url'], verbose=verbose)
    for page in pages:
        for pagecontent in page.content:
            if hasattr(pagecontent, 'dataframe'):
                client.create_or_update_dataframe(pagecontent.dataframe)
        client.create_or_update_page(page)
        print(f'Page "{page.title}" URL: http://localhost/{page.id}')
