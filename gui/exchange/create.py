from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QDialog, QFormLayout, QLineEdit, QPushButton

from core import Exchange
from database import Session


class ExchangeCreateDialog(QDialog):

    created = pyqtSignal(Exchange)

    def __init__(self, session=Session()):
        super().__init__()
        self.session = session

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Exchange Creation')
        self.show()

        # Layout
        layout = QFormLayout()
        layout.setSpacing(10)
        self.setLayout(layout)

        # Ticker
        self.ticker_edit = QLineEdit()
        layout.addRow("Ticker: ", self.ticker_edit)

        # Name
        self.name_edit = QLineEdit()
        layout.addRow("Name: ", self.name_edit)

        # Buttons
        submit = QPushButton("Create")
        submit.clicked.connect(self.submit)
        layout.addWidget(submit)

        submit_and_close = QPushButton("Create and close")
        submit_and_close.clicked.connect(self.submitAndClose)
        layout.addWidget(submit_and_close)

        cancel = QPushButton("Cancel")
        cancel.clicked.connect(self.close)
        layout.addWidget(cancel)

    def submit(self):
        ticker = self.ticker_edit.text()
        if ticker != '':
            name = self.name_edit.text()
            if name == '':
                exchange = Exchange(ticker=ticker)
            else:
                exchange = Exchange(ticker=ticker, name=name)
            try:
                self.session.add(exchange)
                self.session.commit()
            except Exception as e:
                print("Error while inserting:", e)
                self.session.rollback()
            else:
                self.created.emit(exchange)
                self.ticker_edit.clear()
                self.name_edit.clear()

    def submitAndClose(self):
        self.submit()
        self.close()
