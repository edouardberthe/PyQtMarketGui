from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QCompleter

from database import Session
from gui.exchange.model import ExchangeSearchModel


class ExchangeCompleter(QCompleter):

    def __init__(self, session: Session=Session()):
        super().__init__()
        self.setCaseSensitivity(Qt.CaseInsensitive)
        self.setModel(ExchangeSearchModel(session))
        self.setCompletionRole(Qt.DisplayRole)
        self.setCompletionMode(QCompleter.PopupCompletion)
        self.setFilterMode(Qt.MatchContains)
