from PyQt5.QtWidgets import QHBoxLayout, QPushButton, QTableView, QVBoxLayout, QWidget

from core import Exchange
from database import Session
from gui.exchange import ExchangeCreateDialog, ExchangeTableModel


class ExchangeWidget(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.session = Session()

        # Main Layout
        main_layout = QHBoxLayout()
        self.setLayout(main_layout)

        # Left Part
        left_layout = QVBoxLayout()
        main_layout.addLayout(left_layout)

        # Exchange List
        table = QTableView(self)
        self.model = ExchangeTableModel(self.session)
        table.setModel(self.model)
        table.setToolTip("List of stocks")
        left_layout.addWidget(table)

        # Buttons
        btn_layout = QHBoxLayout()
        left_layout.addLayout(btn_layout)

        # Create
        create_btn = QPushButton("New +")
        create_btn.clicked.connect(self.new)
        btn_layout.addWidget(create_btn)

        # Cancel
        cancel_btn = QPushButton("Cancel")
        cancel_btn.clicked.connect(self.close)
        btn_layout.addWidget(cancel_btn)

        # Right part
        main_layout.addStretch(1)

    def new(self):
        dialog = ExchangeCreateDialog(self.session)
        dialog.created.connect(self.updateStatusBar)
        dialog.exec()

    def updateStatusBar(self, exchange: Exchange):
        self.window().statusBar().showMessage('Exchange {} added'.format(exchange))
