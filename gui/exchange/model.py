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
