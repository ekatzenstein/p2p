
from typing import List

from pandastoproduction.models import DataFrame, Page, Site
from pandastoproduction.validate import validate_type_list


def publish(pages: List[Page] = [], dataframes: List[DataFrame] = [], sites: List[Site] = []):
    validate_type_list('pages', pages, Page)
    validate_type_list('dataframes', dataframes, DataFrame)
    validate_type_list('sites', sites, Site)
    print("Publishing...")
    for page in pages:
        print(page)
    for dataframe in dataframes:
        print(dataframe)
    for site in sites:
        print(site)
    print("Done!")
