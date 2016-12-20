import numpy as np
import pandas as pd


class Group(list):

    _data = None

    @property
    def data(self):
        if self._data is None:
            self.load_from_pickle()
        return self._data

    def save(self):
        self.data.to_pickle("pickle/data.pkl")

    def load_from_pickle(self):
        self._data = pd.read_pickle("pickle/data.pkl")

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


PA = Exchange('Paris', 'PA')
CAC40Tickers = ['AC', 'ACA', 'AI', 'AIR', 'BN', 'BNP', 'CA', 'CAP', 'CS', 'DG', 'EI', 'EN', 'ENGI', 'FP', 'FR', 'GLE', 'KER', 'LHN', 'LI', 'LR', 'MC', 'ML', 'MT', 'NOKIA', 'OR', 'ORA', 'PUB', 'RI', 'RNO', 'SAF', 'SAN', 'SGO', 'SOLB', 'SU', 'SW', 'TEC', 'UG', 'UL', 'VIE', 'VIV']
CAC40 = Group([Stock(ticker, PA) for ticker in CAC40Tickers])
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


