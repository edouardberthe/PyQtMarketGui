from PyQt5.QtWidgets import QGridLayout, QLabel, QLineEdit, QWidget


class ExchangeCreate(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        name = QLabel('Name')
        ticker = QLabel('Ticker')

        nameEdit = QLineEdit()
        tickerEdit = QLineEdit()

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(name, 1, 0)
        grid.addWidget(nameEdit, 1, 1)

        grid.addWidget(ticker, 2, 0)
        grid.addWidget(tickerEdit, 2, 1)

        self.setLayout(grid)
        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Exchange Creation')
        self.show()
