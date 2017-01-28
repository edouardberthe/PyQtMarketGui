from PyQt5.QtWidgets import QMessageBox, QPushButton, QVBoxLayout, QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

from core import Stock


class StockDataChart(QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._stock = None

        # Layout
        layout = QVBoxLayout()
        self.setLayout(layout)

        # Matplotlib Figure and Axes
        fig = Figure()
        self.axes = fig.add_subplot(111)
        self.canvas = FigureCanvas(fig)
        layout.addWidget(self.canvas)

        # Buttons
        update_btn = QPushButton("Update")
        update_btn.clicked.connect(self.update)
        layout.addWidget(update_btn)

    @property
    def stock(self) -> Stock:
        return self._stock

    @stock.setter
    def stock(self, stock: Stock):
        if stock != self._stock:
            self._stock = stock
            print("Chart: new stock", self._stock)
            self.update()

    def update(self):
        print("Chart: updating current stock", self.stock)
        self.axes.clear()
        self.setWindowTitle("{} data".format(str(self._stock)))
        try:
            self._stock.data.plot(ax=self.axes)
        except TypeError as e:
            print("Error while plotting stock {}".format(str(self._stock)))
        else:
            self.canvas.draw()
