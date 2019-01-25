import pandas as pd

from pandastoproduction.validate import validate_type


class DataFrame(object):
    def __init__(self, df: pd.DataFrame):
        validate_type('df', df, pd.DataFrame)
        self.df = df
        self.id = None
        self.digest = None
        self.url = None

    def to_csv(self, *args, **kwargs):
        return self.df.to_csv(*args, **kwargs, index=False)

    def __str__(self):
        return f'DataFrame: {self.df}'

    def to_json(self, **kwargs):
        obj = self.__dict__.copy()
        obj.pop('df', None)
        keys_to_remove = [key for key in obj if obj[key] is None]
        for key in keys_to_remove:
            obj.pop(key, None)
        return obj
