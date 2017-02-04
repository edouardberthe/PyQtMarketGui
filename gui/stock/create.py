from PyQt5.QtWidgets import QComboBox, QDialog, QFormLayout, QLineEdit, QListView, QMessageBox, QPushButton, \
    QSizePolicy, QSpacerItem

from core import Stock
from database import Session
from gui.exchange.completer import ExchangeCompleter


class StockCreateDialog(QDialog):

    def __init__(self, *args, **kwargs):
        from gui.exchange import ExchangeTableModel
        super().__init__(*args, **kwargs)
        self.session = Session()

        # Form
        form = QFormLayout()
        form.setSpacing(5)
        self.setLayout(form)

        # Name
        self.name_edit = QLineEdit()
        form.addRow("Name: ", self.name_edit)

        # Ticker
        self.ticker_edit = QLineEdit()
        form.addRow("Ticker: ", self.ticker_edit)

        # Exchange Table
        self.exchange_model = ExchangeTableModel(self.session)
        self.exchange_list = QListView(self)
        self.exchange_list.setModel(self.exchange_model)
        form.addRow("Exchange :", self.exchange_list)

        # Exchange Completer Line Edit test
        self.exchange_edit = QComboBox(self)
        self.exchange_edit.setEditable(True)
        self.exchange_edit.setCompleter(ExchangeCompleter(self.session))
        form.addRow('Exchange 2nd :', self.exchange_edit)

        # Space
        form.addItem(QSpacerItem(100, 100, QSizePolicy.Expanding, QSizePolicy.Fixed))

        # Buttons
        submit = QPushButton("Submit and close", self)
        close = QPushButton(self)
        close.setText("Close")
        form.addWidget(submit)
        form.addWidget(close)

        self.name_edit.returnPressed.connect(self.submitQuery)
        self.ticker_edit.returnPressed.connect(self.submitQuery)
        submit.clicked.connect(self.submitQuery)
        close.clicked.connect(self.close)

    def submitQuery(self):
        ticker = self.ticker_edit.text()
        exchange_indexes = self.exchange_list.selectedIndexes()
        if ticker != '' and len(exchange_indexes) != 0:
            name = self.name_edit.text()
            exchange = self.exchange_model.entity(exchange_indexes[0])
            if name == '':
                self.session.add(Stock(ticker=ticker, exchange=exchange))
            else:
                self.session.add(Stock(ticker=ticker, name=name, exchange=exchange))
            try:
                self.session.commit()
            except Exception as e:
                print("Error", e)
                self.session.rollback()
                alertPopup = QMessageBox()
                alertPopup.setText("Could not successfully insert: {}".format(e))
                alertPopup.setIcon(alertPopup.Critical)
                alertPopup.exec_()
            else:
                self.name_edit.setText("")
                self.ticker_edit.setText("")
            finally:
                self.name_edit.setFocus()
        else:
            alert = QMessageBox()
            alert.setText("Some fields are still empty!")
            alert.setIcon(alert.Critical)
            alert.exec_()
