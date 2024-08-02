import sys

from PySide6.QtGui import QPixmap, QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QHBoxLayout


class FullScreenWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(800, 500)
        self.showMaximized()
        self.centralArea = QWidget()
        self.setCentralWidget(self.centralArea)
        # self.label = QLabel(centralArea)
        # self.label.setPixmap(QPixmap("Pictures/loading_screen_square_erp_project.png"))
        # layout = QHBoxLayout()
        # centralArea.setLayout(layout)
        # layout.addWidget(self.label)
        # layout.setContentsMargins(0, 0, 0, 0)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FullScreenWindow()
    sys.exit(app.exec())