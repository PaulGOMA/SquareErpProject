import sys
sys.path.append("..")

from PySide6.QtWidgets import QLabel
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap

from Utils.responsiveLayout import fitWindowToScreen, centerWindow

from Assets import pictures

class LaunchWindow(QLabel):
    def __init__(self):
        super().__init__()
        self.setFixedSize(fitWindowToScreen(width=800, height=500))
        centerWindow(self)
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.setPixmap(QPixmap(":/Pictures/background_launch.png"))
        self.setScaledContents(True)

        self.show()
