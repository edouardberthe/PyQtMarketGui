from PyQt5.QtWidgets import QDataWidgetMapper, QHBoxLayout, QLineEdit, QPushButton, QTableView, QVBoxLayout, QWidget, \
    qApp

from database import session
from .stock import StockCreateWidget, StockListModel


class CentralWidget(QWidget):

    def __init__(self, *args):
        super().__init__(*args)

        ok_btn = QPushButton("Ok")
        quit_btn = QPushButton("Quit")
        quit_btn.clicked.connect(qApp.quit)

        top_btn_box = QHBoxLayout()
        # Stock List
        stock_table = QTableView(self)
        model = StockListModel(session)
        stock_table.setModel(model)
        stock_table.setToolTip("List of stocks")
        top_btn_box.addWidget(stock_table)
        top_btn_box.addWidget(StockCreateWidget(session, self))

        # Stock List Mapper
        mapper = QDataWidgetMapper(self)
        nameEdit = QLineEdit()
        tickerEdit = QLineEdit()
        mapper.setModel(model)
        mapper.addMapping(nameEdit, 0)
        mapper.addMapping(tickerEdit, 1)

        # Bottom buttons
        bottom_btn_box = QHBoxLayout()
        bottom_btn_box.addStretch(1)
        bottom_btn_box.addWidget(ok_btn)
        bottom_btn_box.addWidget(quit_btn)

        vbox = QVBoxLayout()
        vbox.addLayout(top_btn_box)
        vbox.addLayout(bottom_btn_box)

        self.setLayout(vbox)
