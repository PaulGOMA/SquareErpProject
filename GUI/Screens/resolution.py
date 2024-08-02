"""
    # This file contains all the functions needed to manage screen resolution and resizing. 
"""
import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QSize, QSizeF

# ::::::::Screen size recovery function::::::::::::: #
# screen resolution in pixel
def getResolutions() -> QSize:
    app = QApplication.instance() 
    if app is None:
        app = QApplication(sys.argv)
    return app.primaryScreen().size()

# Physical screen dimensions (width/height)
def getScreenPhysicalSize() -> QSizeF:
    app = QApplication.instance()
    if app is None:
        app = QApplication(sys.argv)
    return app.primaryScreen().physicalSize()

# Pixel per inch
def getDpi() -> float:
    app = QApplication.instance()
    if app is None:
        app = QApplication(sys.argv)
    return app.primaryScreen().logicalDotsPerInch()

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# ::::::::Responsive functions::::::::::::: #
# Keep proportions

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# ::::::::display window in center of screen::::::::::::: #
def centerWindow(window: QMainWindow) -> None:
    x = (getResolutions().width() - window.width()) // 2
    y = (getResolutions().height() - window.height()) // 2

    window.move(x, y)