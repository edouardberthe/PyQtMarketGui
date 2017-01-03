from PyQt5.QtWidgets import QTabWidget

from gui.main.exchange import ExchangeWidget
from gui.main.stock import StockWidget


class DatabaseTab(QTabWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.addTab(StockWidget(self), "Stocks")
        self.addTab(ExchangeWidget(self), "Exchanges")
