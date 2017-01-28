from core import Stock
from gui.model import AbstractTableModel


class StockTableModel(AbstractTableModel):

    @property
    def entity_class(self):
        return Stock

    @property
    def cols(self):
        return ['name', 'ticker', 'exchange']

    @property
    def header(self):
        return ['Name', 'Ticker', 'Exchange']
