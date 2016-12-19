from math import pi

from PyQt5.QtWidgets import QPushButton, QVBoxLayout, QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from numpy import linspace
from numpy.ma import cos, sin

from models.stock import Stock


class StockDataChart(QWidget):
    def __init__(self, stock: Stock):
        QWidget.__init__(self)
        self.setWindowTitle("{:s} data".format(stock))
        self.layout = QVBoxLayout()

        self.fig = Figure()
        self.axes = self.fig.add_subplot(111)

        self.x = linspace(-pi, pi, 30)
        self.y = cos(self.x)
        self.line, = self.axes.plot(self.x, self.y)

        self.canvas = FigureCanvas(self.fig)
        self.layout.addWidget(self.canvas)  # the matplotlib canvas

        self.bouton_cos = QPushButton("Cosinus")
        self.bouton_cos.clicked.connect(self.appui_cosinus)
        self.layout.addWidget(self.bouton_cos)

        self.bouton_sin = QPushButton("Sinus")
        self.bouton_sin.clicked.connect(self.appui_sinus)
        self.layout.addWidget(self.bouton_sin)

        self.setLayout(self.layout)
        self.show()

    def appui_cosinus(self):
        self.y = cos(self.x)
        self.line.set_ydata(self.y)
        self.canvas.draw()

    def appui_sinus(self):
        self.y = sin(self.x)
        self.line.set_ydata(self.y)
        self.canvas.draw()
