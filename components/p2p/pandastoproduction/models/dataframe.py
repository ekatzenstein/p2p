import pandas as pd

from pandastoproduction.validate import validate_type


class DataFrame(object):
    def __init__(self, df: pd.DataFrame):
        validate_type('df', df, pd.DataFrame)
        self._df = df
        self._id = None

    @property
    def df(self):
        return self._df

    @property
    def id(self):
        return self._id

    def __str__(self):
        return f'DataFrame: {self._df}'
