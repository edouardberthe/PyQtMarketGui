import unittest

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from config import test_config as config
from core import Exchange, Stock
from database import metadata


class BaseTestCaseWrapper:

    class BaseTestCase(unittest.TestCase):

        def setUp(self):
            self.engine = create_engine('{:s}://{:s}:{:s}@{:s}:{:d}/{:s}'.format(
                config['db_pdo'],
                config['db_user'],
                config['db_password'],
                config['db_host'],
                config['db_port'],
                config['db_name']
            ), echo=config['db_debug'])
            metadata.create_all(self.engine)
            self.session = Session(self.engine)

        def tearDown(self):
            self.session.commit()
            metadata.drop_all(self.engine)


class StockTestCase(BaseTestCaseWrapper.BaseTestCase):

        def test_add(self):
            exchange = Exchange(ticker='ER')
            stock = Stock(ticker='HELLO', exchange=exchange)

            self.assertNotIn(stock, self.session.query(Stock).all())

            self.session.add(stock)
            self.session.commit()
            self.assertIn(stock, self.session.query(Stock).all())


class ExchangeTestCase(BaseTestCaseWrapper.BaseTestCase):

    def test_add(self):
        exchange = Exchange(ticker='RE')
        self.assertNotIn(exchange, self.session.query(Exchange).all())

        self.session.add(exchange)
        self.session.commit()
        self.assertIn(exchange, self.session.query(Exchange).all())
