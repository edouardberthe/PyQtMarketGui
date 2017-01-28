from typing import List

import numpy as np
import pandas as pd

from .security import Stock


class Bucket(list):

    def __init__(self, stocks: List[Stock]=[], name=None):
        super().__init__(stocks)
        self.name = name
        self._data = None

    def __str__(self):
        return self.name if self.name is not None else "Unnamed Bucket"

    def __repr__(self):
        return "<Bucket {:s}>".format(self.name) if self.name is not None else "<Bucket Unnamed>"

    @property
    def data(self):
        if self._data is None:
            self._data = pd.DataFrame({s.ticker: s.data for s in self})
        return self._data

    def load_from_yahoo(self):
        _data = pd.DataFrame({s.ticker: s.data for s in self})
        print("Removing missing values")
        _data = _data.loc[:, _data.isnull().sum() < 0.05 * len(_data)]
        print("Removing outliers")
        _data.drop(_data.index[((_data - _data.mean()).abs() > 3 * _data.std()).any(axis=1)], inplace=True)
        _data.dropna(inplace=True)
        self._data = _data

    def gross(self) -> pd.DataFrame:
        res = (self.data / self.data.shift())[1:]
        # We remove the values too extreme to be simply outliers (a daily return of more than 50% is VERY unlikely..).
        res.drop(res.index[(res > 1.5).any(axis=1)], inplace=True)
        return res

    def returns(self) -> pd.DataFrame:
        return self.gross() - 1


Returns = pd.DataFrame()
DailyMeanReturns = Returns.mean()
MeanReturns = DailyMeanReturns * 252

DailyVarReturns = Returns.var()
VarReturns = DailyVarReturns * 252

DailyVolReturns = Returns.std()
VolReturns = DailyVolReturns * np.sqrt(252)

CovReturns = Returns.cov() * 252


# For the report
# figsize = (10, 6.18)

figsize = (20, 10)


