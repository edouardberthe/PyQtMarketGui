from PyQt5.QtCore import QModelIndex
from PyQt5.QtCore import Qt

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


class StockSearchModel(AbstractTableModel):

    @property
    def entity_class(self):
        return Stock

    @property
    def header(self):
        return ['Full Name']

    @property
    def cols(self):
        return ['full_name']

    def data(self, index: QModelIndex, role: int=None):
        if role == Qt.DisplayRole:
            stock = self.entity(index)
            return str(stock.ticker + "." + stock.exchange.ticker + ("" if stock.name is None else "(" + stock.name + ")"))
