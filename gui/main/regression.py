from PyQt5.QtWidgets import QHBoxLayout, QTabWidget, QVBoxLayout

from gui.pair.form import PairForm


class RegressionTab(QTabWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        # Main Layout
        layout = QHBoxLayout(self)
        self.setLayout(layout)

        # Left part
        left_layout = QVBoxLayout()
        form = PairForm(self)
        left_layout.addWidget(form)
        layout.addLayout(left_layout)

        # Right part
        layout.addStretch()
