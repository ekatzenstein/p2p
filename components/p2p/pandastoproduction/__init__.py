from pandastoproduction.publish import publish
from pandastoproduction.models import *
from pandastoproduction.config import CONFIG

def _jupyter_nbextension_paths():
    return [{
        'section': 'notebook',
        'src': 'static',
        'dest': 'pandastoproduction',
        'require': 'pandastoproduction/index'
    }]
