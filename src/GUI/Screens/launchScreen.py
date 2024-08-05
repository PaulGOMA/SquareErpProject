import sys
sys.path.append("..")

from PySide6.QtWidgets import QMainWindow, QWidget, QApplication
from PySide6.QtCore import Qt
from GUI.Screens.resolution import centerWindow

from Assets import pictures

class LaunchScreen(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(800, 500)
        centerWindow(self)
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)

        self.centralArea = QWidget()
        self.centralArea.setStyleSheet(
            """
                background-image: url(":/Pictures/background_launch.png")
            """
        )
        self.setCentralWidget(self.centralArea)

        self.show()
