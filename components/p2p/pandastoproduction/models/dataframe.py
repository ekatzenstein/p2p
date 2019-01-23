import pandas as pd

from pandastoproduction.validate import validate_type


class DataFrame(object):
    def __init__(self, df: pd.DataFrame):
        validate_type('df', df, pd.DataFrame)
        self._df = df

    def __str__(self):
        return f'DataFrame: {self._df}'
