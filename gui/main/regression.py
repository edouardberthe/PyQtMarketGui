from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QTabWidget


class RegressionTab(QTabWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        s1 = QLineEdit(self)

