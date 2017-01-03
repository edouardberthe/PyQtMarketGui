from abc import ABCMeta, abstractmethod
from datetime import date

from pandas_datareader._utils import RemoteDataError
from pandas_datareader.data import DataReader


class GenericOption:

    __metaclass__ = ABCMeta

    def __init__(self, underlying, maturity: date, strike: float):
        self.underlying = underlying
        self.maturity = maturity
        self.strike = strike

    @abstractmethod
    def payoff(self) -> float:
        raise NotImplementedError

    @property
    def ticker(self):
        if isinstance(self.underlying, str):
            return self.underlying
        else:
            return self.underlying.ticker

    def yahoo_ticker(self):
        return "{:s}{:s}C{:s}".format(self.ticker,
                                      self.maturity.strftime("%d%m%y"),
                                      "{:d}".format(self.strike*1000).zfill(8))

    def load_from_yahoo(self, start='2005-01-01', end=None):
        print('Loading data of', self, ' from yahoo')
        try:
            self._data = DataReader(self.ticker, 'yahoo', start, end)['Adj Close']
        except RemoteDataError as e:
            print('Data not loaded because of RemoteDataError:', e)


class CallOption(GenericOption):

    def payoff(self) -> float:
        return max(self.underlying.price - self.strike)


class PutOption(GenericOption):

    def payoff(self) -> float:
        return max(self.strike - self.underlying.price)
