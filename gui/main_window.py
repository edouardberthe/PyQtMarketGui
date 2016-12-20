from PyQt5.QtCore import QObject
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtWidgets import QAction, QDataWidgetMapper, QHBoxLayout, QLineEdit, QMainWindow, QMessageBox, QPushButton, \
    QTabWidget, QTableView, QToolTip, QVBoxLayout, QWidget, qApp
from sqlalchemy.orm import Session

from gui.exchange import ExchangeTableModel
from gui.stock import StockCreateDialog, StockListModel


class StockWidget(QWidget):

    def __init__(self, session: Session, parent=None):
        super().__init__(parent)
        self.session = session

        main_layout = QHBoxLayout()

        ## Left Part ##

        # Stock List
        stock_table = QTableView(self)
        model = StockListModel(session)
        stock_table.setModel(model)
        stock_table.setToolTip("List of stocks")

        # Buttons
        create_btn = QPushButton("New +")
        create_btn.clicked.connect(self.createStock)

        left_layout = QVBoxLayout()
        left_layout.addWidget(stock_table)
        left_layout.addWidget(create_btn)

        # Stock List Mapper
        self.stock_create_widget = StockCreateDialog(self.session, self)
        mapper = QDataWidgetMapper(self)
        nameEdit = QLineEdit()
        tickerEdit = QLineEdit()
        mapper.setModel(model)
        mapper.addMapping(nameEdit, 0)
        mapper.addMapping(tickerEdit, 1)

        # Main Layout
        main_layout.addLayout(left_layout)
        main_layout.addStretch(1)

        self.setLayout(main_layout)

    def createStock(self):
        self.stock_create_widget.exec_()


class ExchangeWidget(QWidget):

    def __init__(self, session: Session, parent: QObject=None):
        super().__init__(parent)
        self.session = session

        layout = QVBoxLayout()
        exchange_table = QTableView(self)
        exchange_table.setModel(ExchangeTableModel(self.session))
        layout.addWidget(exchange_table)

        self.setLayout(layout)


class DatabaseTab(QTabWidget):
    def __init__(self, session: Session, parent=None):
        super().__init__(parent)
        self.addTab(StockWidget(session, self), "Stocks")
        self.addTab(ExchangeWidget(session, self), "Exchanges")


class RegressionTab(QTabWidget):
    pass


class CentralTab(QTabWidget):

    def __init__(self, session: Session, parent=None):
        super().__init__(parent)

        self.addTab(DatabaseTab(session, self), "Database")
        self.addTab(RegressionTab(self), "Regressions")


class MainWindow(QMainWindow):

    def __init__(self, session: Session):
        super().__init__()

        QToolTip.setFont(QFont('SansSerif', 10))

        # Toolbar
        quit_action = QAction(QIcon('exit24.png'), '&Exit', self)
        quit_action.setShortcut('Ctrl+Q')
        quit_action.setStatusTip('Exit application')
        quit_action.triggered.connect(qApp.quit)
        self.addToolBar('Exit').addAction(quit_action)

        # Status Bar
        self.statusBar().showMessage('Ready')

        # Central Widget
        self.setCentralWidget(CentralTab(session, self))

        # Window Size and Title
        self.setGeometry(300, 300, 500, 300)
        self.setWindowTitle('Tooltips')

        self.show()

    def closeEvent(self, event):

        reply = QMessageBox.question(self, 'Message',
                                     "Are you sure to quit?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
