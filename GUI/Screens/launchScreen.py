import sys

from PySide6.QtWidgets import QMainWindow, QWidget, QApplication
from PySide6.QtCore import Qt
from resolution import centerWindow


class launchScreen(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(800, 500)
        centerWindow(self)
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)

        self.centralArea = QWidget()
        self.centralArea.setStyleSheet(
            """
                background-image: url("GUI/Pictures/background_launch_screen.png")
            """
        )
        self.setCentralWidget(self.centralArea)

        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = launchScreen()
    sys.exit(app.exec())
