from PyQt5.QtWidgets import QFormLayout, QPushButton, QWidget

from core.pair import Pair
from database import Session
from gui.stock.line_edit import StockLineEdit


class PairForm(QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.session = Session()

        # Layout
        layout = QFormLayout()
        self.setLayout(layout)

        # Security 1
        self.security1_edit = StockLineEdit(self)
        layout.addRow("Security 1", self.security1_edit)

        # Security 2
        self.security2_edit = StockLineEdit(self)
        layout.addRow("Security 2", self.security2_edit)

        # Button
        button = QPushButton("Launch")
        layout.addRow(button)

        # Business Logic
        button.clicked.connect(self.update)

    def update(self):
        self.pair = Pair(self.security1_edit.stock, self.security2_edit.stock)

