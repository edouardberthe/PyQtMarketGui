from PyQt5.QtCore import QModelIndex
from PyQt5.QtWidgets import QHBoxLayout, QPushButton, QTableView, QVBoxLayout, QWidget

from core import Bucket
from database import Session
from gui.charts import BucketDataChart
from gui.stock import StockCreateDialog, StockTableModel


class StockWidget(QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.session = Session()

        # Main Layout
        main_layout = QHBoxLayout()

        # Left Part #
        left_layout = QVBoxLayout()
        main_layout.addLayout(left_layout)

        # Stock List
        self.model = StockTableModel()
        self.table = QTableView(self)
        self.table.setModel(self.model)
        self.table.setToolTip("List of stocks")
        self.table.setFixedWidth(self.table.horizontalHeader().length())
        left_layout.addWidget(self.table)

        # Buttons
        btn_layout = QHBoxLayout()
        left_layout.addLayout(btn_layout)

        # Create button
        create_btn = QPushButton("New +")
        create_btn.clicked.connect(self.new)
        btn_layout.addWidget(create_btn)

        # Load button
        load_btn = QPushButton("Load Data")
        load_btn.clicked.connect(self.load)
        btn_layout.addWidget(load_btn)

        # Right Part
        self.chart = BucketDataChart()
        main_layout.addWidget(self.chart)

        # Signals
        self.table.clicked.connect(self.update)
        self.setLayout(main_layout)

    def update(self, index: QModelIndex):
        self.chart.bucket = Bucket([self.model.entity(index) for index in self.table.selectedIndexes()])

    def load(self):
        for index in self.table.selectedIndexes():
            stock = self.model.entity(index)
            """:type: Stock"""
            stock.load_from_yahoo()

    def new(self):
        StockCreateDialog(self).exec()
