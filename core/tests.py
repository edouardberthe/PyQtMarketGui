import unittest

from core import Exchange


class ExchangeTestCase(unittest.TestCase):

    def test_init(self):
        with self.assertRaises(TypeError):
            Exchange()
        with self.assertRaises(TypeError):
            Exchange(name='Coucou')
        self.assertIsInstance(Exchange(ticker='ER'), Exchange)
        self.assertIsInstance(Exchange(ticker='ER', name='ED'), Exchange)
