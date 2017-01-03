import pandas as pd
from pandas_datareader._utils import RemoteDataError
from pandas_datareader.data import DataReader
from sqlalchemy import orm

from core.exchange import Exchange
from exceptions import NoStockDataError


class Security:

    def __init__(self, ticker: str, exchange: Exchange, name: str=None):
        self.ticker = ticker
        self.exchange = exchange
        self.name = name
        self._data = None

    def __str__(self):
        return self.name if self.name is not None else self.yahoo_ticker

    def __repr__(self):
        return "<Stock {:s}>".format(str(self))

    @property
    def yahoo_ticker(self):
        return "{}.{}".format(self.ticker, self.exchange.ticker)

    def load_from_db(self):
        from database import engine
        df = pd.read_sql_query("select date, value from adj_close where stock_id = {:d} order by date".format(self.id),
                               engine, index_col='date', parse_dates=('date',))
        if len(df) < 100:
            raise NoStockDataError(self)
        else:
            self._data = df['value']
            self._data.name = 'Adj Close'

    def load_from_yahoo(self, start='2005-01-01', end=None):
        print("Loading data of", self, " from Yahoo API")
        try:
            self._data = DataReader(self.yahoo_ticker, 'yahoo', start, end)['Adj Close']
            self.save()
        except RemoteDataError as e:
            print("Error while loading data from Yahoo API:", e)

    @property
    def data(self):
        """Getter to _data internal private property. Useful for lazy loading of the data in database."""
        if self._data is None:
            try:
                self.load_from_db()
            except NoStockDataError:
                self._data = pd.DataFrame()
        return self._data

    def save(self):
        """
        Performs an update of the database by overriding the valuations by the values inside _data (needs previous
        action of load_from_yahoo).
        """
        if self._data is not None:
            from database import engine
            copy = pd.DataFrame(self._data)
            copy['stock_id'] = self.id
            copy.columns = ['value', 'stock_id']
            copy.index.name = 'date'
            copy.to_sql('adj_close', engine, if_exists='append')
            print("Data of", self, "saved to database.")
        else:
            print("Not saving: no internal Data loaded in ", self)

    def returns(self):
        return self.data / self.data.shift() - 1

    def mean_return(self):
        return self.returns.mean()


class Stock(Security):

    @orm.reconstructor
    def init_on_load(self):
        self._data = None


class Index(Security):
    pass


class Commodity(Security):
    pass


class DataFrame(pd.DataFrame):
    pass


class Pair(tuple):

    def __init__(self, security1: Security, security2: Security):
        super().__init__((security1, security2))

    def data(self):
        return pd.DataFrame(self[0].data, self[1].data)

    def r2(self):
        return self.data
