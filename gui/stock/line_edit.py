from PyQt5.QtCore import QModelIndex
from PyQt5.QtWidgets import QLineEdit

from gui.stock.completer import StockCompleter


class StockLineEdit(QLineEdit):

    def __init__(self, *args):
        super().__init__(*args)
        self.completer = StockCompleter()
        self.setCompleter(self.completer)
        self.completer.activated.connect(self.update)
        self.stock = None

    def update(self, index: QModelIndex):
        print(index)
        self.stock = self.completer.model.entity(index)
