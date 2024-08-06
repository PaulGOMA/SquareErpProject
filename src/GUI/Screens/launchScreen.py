import sys
sys.path.append("..")

from PySide6.QtWidgets import QMainWindow, QLabel, QSizePolicy
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap

from GUI.Components.components import setBackgroundImage
from Utils.responsiveLayout import fitWindowToScreen, centerWindow

from Assets import pictures

class LaunchScreen(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(fitWindowToScreen(width=800, height=500))
        centerWindow(self)

        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.centralArea = QLabel()
        self.centralArea.setPixmap(QPixmap(":/Pictures/background_launch.png"))
        self.centralArea.setScaledContents(True)
        self.centralArea.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.setCentralWidget(self.centralArea)

        self.show()
