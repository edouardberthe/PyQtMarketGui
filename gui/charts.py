from PyQt5.QtWidgets import QPushButton, QVBoxLayout, QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas, \
    NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

from core import Bucket
from core.pair import Pair


class Chart(QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Layout
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # Matplotlib Figure and Axes
        self.fig = Figure()
        self.axes = self.fig.add_subplot(111)
        self.canvas = FigureCanvas(self.fig)
        self.layout.addWidget(self.canvas)

        # Toolbar to interact
        self.toolbar = NavigationToolbar(self.canvas, self, coordinates=True)
        self.layout.addWidget(self.toolbar)


class BucketDataChart(Chart):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._bucket = Bucket()

        # Buttons
        update_btn = QPushButton("Update")
        update_btn.clicked.connect(self.update)
        self.layout.addWidget(update_btn)

    def __str__(self):
        return str([str(s) for s in self._bucket])

    @property
    def bucket(self):
        return self._bucket

    @bucket.setter
    def bucket(self, bucket: Bucket):
        if bucket != self._bucket:
            self._bucket = bucket
            self.update()

    def update(self):
        self.axes.clear()
        bar = self.window().statusBar()
        try:
            self._bucket.data.plot(ax=self.axes)
        except (TypeError, ValueError) as e:
            bar.showMessage("Error while plotting {}: no data in database".format(str(self)))
        else:
            self.axes.set_xlabel('')
            left = 0.06
            bottom = 0.1
            right = 0.97
            top = 0.95
            self.fig.subplots_adjust(left, bottom, right, top)
            self.canvas.draw()
            bar.showMessage("StockChart: successfully drawn current bucket {}".format(str(self)))


class PairChart(Chart):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._pair = None

    @property
    def pair(self):
        return self._pair

    @pair.setter
    def pair(self, other):
        if isinstance(other, Pair) and other != self.pair:
            self._pair = other
            self.draw()

    def draw(self):
        self.axes.clear()
        self._pair.data.plot(ax=self.axes)
