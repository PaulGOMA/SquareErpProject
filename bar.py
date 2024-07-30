"""
    # This file contains all main headers and bars used commonly 
    # in the application
"""

from PySide6.QtWidgets import QFrame, QWidget, QBoxLayout,\
    QSizePolicy, QHBoxLayout, QLabel
from PySide6.QtGui import QFont, QPalette, QColor
from PySide6.QtCore import Qt

from components import addButtonWithText, validateButton

# ::::::::Headers::::::::::::: #

def header(parent: QWidget, layout: QBoxLayout, text: str, textButton: str) -> QFrame:
    frame = QFrame(parent)
    frame.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
    frame.setStyleSheet("background-color: white;")

    frameLayout = QHBoxLayout()
    frame.setLayout(frameLayout)
    frameLayout.setContentsMargins(12, 12, 12, 12)

    title = QLabel(frame)
    title.setText(text)
    title.setFont(QFont("Montserrat", 14, QFont.DemiBold))
    palette = title.palette()
    palette.setColor(QPalette.WindowText, QColor("#744BE0"))  # Couleur du texte
    title.setPalette(palette)
    frameLayout.addWidget(title)

    frameLayout.addStretch()

    addButtonWithText(frame, frameLayout, textButton)
    
    layout.addWidget(frame)
    return frame

def headerWithValidateButton(parent: QWidget, layout: QBoxLayout, text: str) -> QFrame:
    frame = QFrame(parent)
    frame.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
    frame.setStyleSheet("background-color: white;")

    frameLayout = QHBoxLayout()
    frame.setLayout(frameLayout)
    frameLayout.setContentsMargins(12, 12, 12, 12)

    title = QLabel(frame)
    title.setText(text)
    title.setFont(QFont("Montserrat", 14, QFont.DemiBold))
    palette = title.palette()
    palette.setColor(QPalette.WindowText, QColor("#744BE0"))
    title.setPalette(palette)
    frameLayout.addWidget(title)

    frameLayout.addStretch()

    validateButton(frame, frameLayout)
    
    layout.addWidget(frame)
    return frame

def headerWithoutButton(parent: QWidget, layout: QBoxLayout, text: str) -> QFrame:
    frame = QFrame(parent)
    frame.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
    frame.setStyleSheet("background-color: white;")

    frameLayout = QHBoxLayout()
    frame.setLayout(frameLayout)
    frameLayout.setContentsMargins(12, 12, 12, 12)

    title = QLabel(frame)
    title.setText(text)
    title.setFont(QFont("Montserrat", 14, QFont.DemiBold))
    palette = title.palette()
    palette.setColor(QPalette.WindowText, QColor("#744BE0"))
    title.setPalette(palette)
    frameLayout.addWidget(title)

    frameLayout.addStretch()
    
    layout.addWidget(frame)
    return frame

