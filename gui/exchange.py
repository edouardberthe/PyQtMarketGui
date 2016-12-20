from PyQt5.QtCore import QAbstractTableModel, QModelIndex, Qt
from PyQt5.QtWidgets import QGridLayout, QLabel, QLineEdit, QWidget

from gui.stock import AbstractTableModel
from metadata import Exchange


class ExchangeCreate(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        ticker = QLabel('Ticker')
        name = QLabel('Name')

        tickerEdit = QLineEdit()
        nameEdit = QLineEdit()

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(ticker, 2, 0)
        grid.addWidget(tickerEdit, 2, 1)

        grid.addWidget(name, 1, 0)
        grid.addWidget(nameEdit, 1, 1)

        self.setLayout(grid)
        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Exchange Creation')
        self.show()


class ExchangeTableModel(AbstractTableModel):

    @property
    def entity(self):
        return Exchange

    @property
    def header(self):
        return ['Ticker', 'Name']

    @property
    def cols(self):
        return ['ticker', 'name']