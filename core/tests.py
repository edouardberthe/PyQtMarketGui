import unittest

from core import Bucket
from core import Exchange


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
