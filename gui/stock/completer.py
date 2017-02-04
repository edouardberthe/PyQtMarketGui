from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QCompleter

from database import Session
from gui.stock.model import StockSearchModel


class StockCompleter(QCompleter):

    def __init__(self, session: Session=Session()):
        super().__init__()
        self.setCaseSensitivity(Qt.CaseInsensitive)
        self.model = StockSearchModel(session)
        self.setModel(self.model)
        self.setCompletionRole(Qt.DisplayRole)
        self.setFilterMode(Qt.MatchContains)
        self.stock = None
        self.activated.connect(self.update)

    def update(self, index):
        self.stock = self.model.entity(index)
