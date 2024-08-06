"""
    # This file contains all the functions needed to manage screen positioning and resizing.
"""
import sys

from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import QSize

# Screen size recovery function
def getResolutions() -> QSize:
    app = QApplication.instance() 
    if app is None:
        app = QApplication(sys.argv)
    return app.primaryScreen().size()

# Display window in center of screen
def centerWindow(window: QWidget) -> None:
    x = (getResolutions().width() - window.width()) // 2
    y = (getResolutions().height() - window.height()) // 2

    window.move(x, y)

# Adjust component size to fit the screen
def fitSizeToScreen(width: int | None, height: int | None) -> QSize | int:
    screenWidth = getResolutions().width()
    ratio = screenWidth  / 1536

    if width is None and height is not None:
        newHeight = 1 if int(ratio * height) == 0 else int(ratio * height)
        return newHeight
    elif height is None and width is not None:
        newWidth = 1 if int(ratio * width) == 0 else int(ratio * width)
        return newWidth
    else:
        newWidth = 1 if int(ratio * width) == 0 else int(ratio * width)
        newHeight = 1 if int(ratio * height) == 0 else int(ratio * height)
        return QSize(newWidth, newHeight)
    
# Adjust one value to fit the screen    
def fitValueToScreen(value: int) -> int:
    screenWidth = getResolutions().width()
    ratio = screenWidth  / 1536
    newValue = 1 if int(ratio * value) == 0 else int(ratio * value)

    return newValue

# Adjust window size to fit the screen
def fitWindowToScreen(width: int, height: int) -> QSize:
    screenWidth = getResolutions().width()
    ratio = screenWidth  / 1536

    newWidth = 1 if int(ratio * width) == 0 else int(ratio * width)
    newHeight = 1 if int(ratio * height) == 0 else int(ratio * height)

    return QSize(newWidth, newHeight)