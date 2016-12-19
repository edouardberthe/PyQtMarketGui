import sys

from PyQt5.QtWidgets import QApplication

from database import session
from models import *
from gui.main_window import MainWindow


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow(session)
    sys.exit(app.exec_())
