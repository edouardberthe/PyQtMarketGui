import sys

from PyQt5.QtCore import QAbstractListModel, QModelIndex, Qt
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QFormLayout, QLabel, QLineEdit, QMessageBox, QPushButton, QSizePolicy, QSpacerItem, QWidget, \
    qApp

from models import Stock


class StockListModel(QAbstractListModel):

    def __init__(self, session):
        super().__init__()
        self.session = session
        self.stocks = []
        self.refresh()

    def refresh(self):
        self.stocks = self.session.query(Stock).all()

    def rowCount(self, parent=None, *args, **kwargs):
        return len(self.stocks)

    def data(self, index: QModelIndex, role: int=None):
        col = index.column()
        stock = self.stocks[index.row()]
        if role == Qt.DisplayRole:
            if col == 0:
                return stock.ticker
            elif col == 1:
                return stock.name

    def columnCount(self, *args, **kwargs):
        return 2


class StockCreateDialog(QDialog):

    def __init__(self, session, parent=None):
        super().__init__(parent)
        self.session = session
        self.initUI()

    def initUI(self):
        self.name_label = QLabel('Name: ')
        self.ticker_label = QLabel("Ticker: ")

        self.name_edit = QLineEdit()
        self.ticker_edit = QLineEdit()

        self.submit = QPushButton(self)
        self.submit.setText("Submit")

        self.close = QPushButton(self)
        self.close.setText("Close")

        self.spacer = QSpacerItem(100, 100, QSizePolicy.Expanding, QSizePolicy.Fixed)

        self.form = QFormLayout()
        self.form.setSpacing(5)

        self.form.addWidget(self.name_label)
        self.form.addWidget(self.name_edit)
        self.form.addWidget(self.ticker_label)
        self.form.addWidget(self.ticker_edit)
        self.form.addItem(self.spacer)
        self.form.addWidget(self.submit)
        self.form.addWidget(self.close)

        self.setLayout(self.form)

        self.name_edit.returnPressed.connect(self.submitQuery)
        self.ticker_edit.returnPressed.connect(self.submitQuery)
        self.submit.clicked.connect(self.submitQuery)
        self.close.clicked.connect(qApp.quit)

    def submitQuery(self):
        if self.name_edit.text() != '' and self.ticker_edit.text() != '':
            try:
                self.session.add(Stock(ticker=self.ticker_edit.text(), name=self.name_edit.text()))
                self.window().statusBar().showMessage('Successfully inserted')
                self.session.commit()
                self.name_edit.setText("")
                self.ticker_edit.setText("")
                self.name_edit.setFocus()
            except Exception as e:
                print("Error", e)
                self.session.rollback()
                alertPopup = QMessageBox()
                alertPopup.setText("Could not successfully insert!")
                alertPopup.setIcon(alertPopup.Critical)
                alertPopup.exec_()
                sys.exit(1)
        else:
            alertPopup = QMessageBox()
            alertPopup.setText("Some fields are still empty!")
            alertPopup.setIcon(alertPopup.Critical)
            alertPopup.exec_()
