from pandas_datareader._utils import RemoteDataError
from pandas_datareader.data import DataReader
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship

from models.declarative_base import Base


class Stock(Base):

    __tablename__ = 'stock'

    ticker = Column(String(5), primary_key=True)
    name = Column(String(20))
    exchange_ticker = Column('exchange', String(2), ForeignKey('exchange.ticker'))
    exchange = relationship('Exchange')

    _data = None

    def __repr__(self):
        return "<Stock {:s}>".format(str(self))

    def __str__(self):
        return self.name if self.name is not None else self.ticker

    @property
    def yahoo_ticker(self):
        return "{}.{}".format(self.ticker, self.exchange.ticker)

    def load_from_yahoo(self, start='2005-01-01', end=None):
        print('Loading data for', self)
        try:
            self._data = DataReader(self.yahoo_ticker, 'yahoo', start, end)['Adj Close']
        except RemoteDataError as e:
            print('Data not loaded', e)

    @property
    def data(self):
        if self._data is None:
            self.load_from_yahoo()
        return self._data

    def returns(self):
        return self.data / self.data.shift() - 1

    def mean_return(self):
        return self.returns.mean()
