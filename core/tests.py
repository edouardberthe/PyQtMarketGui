import unittest

from core import Bucket
from core import Exchange
from core import Stock


class StockTestCase(unittest.TestCase):

    def test_init(self):
        with self.assertRaises(TypeError):
            Stock()
        with self.assertRaises(TypeError):
            Stock('Re')
        with self.assertRaises(TypeError):
            Stock(exchange=Exchange('PA'))
        self.assertIsInstance(Stock('RE', exchange=Exchange('PA')), Stock)


class ExchangeTestCase(unittest.TestCase):

    def test_init(self):
        with self.assertRaises(TypeError):
            Exchange()
        with self.assertRaises(TypeError):
            Exchange(name='Coucou')
        self.assertIsInstance(Exchange(ticker='ER'), Exchange)
        self.assertIsInstance(Exchange(ticker='ER', name='ED'), Exchange)


class BucketTestCase(unittest.TestCase):

    def test_init(self):
        bucket = Bucket()
        self.assertIsInstance(bucket, Bucket)
        self.assertIsInstance(bucket, list)
        self.assertEqual(len(bucket), 0)
        self.assertIsNone(bucket.name)

        named_bucket = Bucket([], "Hello")
        self.assertIsInstance(named_bucket, Bucket)
        self.assertIsNotNone(named_bucket.name)
