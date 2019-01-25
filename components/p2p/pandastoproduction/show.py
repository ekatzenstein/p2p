from typing import List

from IPython.display import display

from pandastoproduction.models import PageContent
from pandastoproduction.validate import validate_type_list, validate_type


def show(content: List[PageContent] = []):
    print("show: NotImplemented")
    print("enjoy display() instead :)")
    display(content)
