from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtWidgets import QAction, QMainWindow, QTabWidget, \
    QToolTip, qApp

from gui.main.database import DatabaseTab


class RegressionTab(QTabWidget):
    pass


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

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
        central_widget = QTabWidget(self)
        central_widget.addTab(DatabaseTab(self), "Database")
        central_widget.addTab(RegressionTab(self), "Regressions")
        self.setCentralWidget(central_widget)

        # Window Size and Title
        self.setGeometry(300, 200, 800, 500)
        self.setWindowTitle('Tooltips')

        self.show()
