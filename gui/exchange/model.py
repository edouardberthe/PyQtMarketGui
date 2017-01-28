from PyQt5.QtCore import QModelIndex, Qt

from core import Exchange
from gui.model import AbstractTableModel


class ExchangeTableModel(AbstractTableModel):

    @property
    def entity_class(self):
        return Exchange

    @property
    def header(self):
        return ['Ticker', 'Name']

    @property
    def cols(self):
        return ['ticker', 'name']


class ExchangeSearchModel(AbstractTableModel):

    @property
    def entity_class(self):
        return Exchange

    @property
    def header(self):
        return ['Full Name']

    @property
    def cols(self):
        return ['full_name']

    def data(self, index: QModelIndex, role: int=None):
        if role == Qt.DisplayRole:
            return str(self.entity(index).ticker + " " + self.entity(index).name)
