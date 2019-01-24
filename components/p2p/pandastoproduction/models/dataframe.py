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

    @id.setter
    def id(self, id):
        validate_type('id', id, int)
        self._id = id

    def __str__(self):
        return f'DataFrame: {self._df}'
