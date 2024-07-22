"""
    #This file contains all the functions
    # required to create the componants used in the application, 
    # such as buttons, search bars, etc.
"""

import sys
from PySide6.QtWidgets import  QMainWindow, QWidget, QHBoxLayout, QApplication, QPushButton, QBoxLayout, QSizePolicy, QFrame, QLineEdit
from PySide6.QtGui import QIcon, QFont, Qt
from PySide6.QtCore import QSize


# ::::::::Buttons::::::::::::: #

# Add new element button
def add_button_without_text(parent: QWidget, layout: QBoxLayout):
    button = QPushButton(parent)
    button.setIcon(QIcon("Icons/big_plus_icon.svg"))
    button.setFlat(True)
    button.setFixedSize(44, 44)
    button.setStyleSheet(
        """
        QPushButton {background-color: #744BE0;border: none;}
        QPushButton:pressed {background-color: #52349f;}
        """
    )
    layout.addWidget(button)
    return button


def add_button_with_text(parent: QWidget, layout: QBoxLayout, text: str):
    button = QPushButton(QIcon("Icons/big_plus_icon.svg"), text, parent)
    button.setFlat(True)
    button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
    button.setFont(QFont("Montserrat", 11, QFont.DemiBold))
    button.setLayoutDirection(Qt.RightToLeft)
    button.setStyleSheet(
        """
        QPushButton {background-color: #744BE0; color: white; border: none; 
            padding-top: 10px; padding-right: 20px; padding-bottom: 10px; padding-left: 20px;}
        QPushButton:pressed {background-color: #52349f; color: white;}
        """
    )
    layout.addWidget(button)
    return button

# Validate button
def validate_button(parent: QWidget, layout: QBoxLayout):
    button = QPushButton(QIcon("Icons/validate_icon_button.svg"), "Valider ", parent)
    button.setFlat(True)
    button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
    button.setFont(QFont("Montserrat", 11, QFont.DemiBold))
    button.setLayoutDirection(Qt.RightToLeft)
    button.setStyleSheet(
        """
        QPushButton {background-color: #744BE0; color: white; border: none; 
            padding-top: 10px; padding-right: 20px; padding-bottom: 10px; padding-left: 20px;}
        QPushButton:pressed {background-color: #52349f; color: white;}
        """
    )
    layout.addWidget(button)
    return button

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# ::::::::text input line::::::::::::: #

# Search bar 

def searchbar_for_navbar(parent: QWidget, layout: QBoxLayout):
    frame = QFrame(parent)
    frame.setFixedSize(424, 52)
    frame.setStyleSheet("QFrame {background-color: transparent; border: 3px solid #e1e2fe;}")

    frame_layout = QHBoxLayout()
    frame.setLayout(frame_layout)

    line_input = QLineEdit(frame)
    line_input.setFixedWidth(350)
    line_input.setPlaceholderText("Recherchez...")
    line_input.setFrame(QFrame.NoFrame)
    line_input.setStyleSheet("background-color: transparent; color: #3d3d3d;")
    line_input.setFont(QFont("Montserrat", 11, QFont.Normal))
    frame_layout.addWidget(line_input)

    frame_layout.addStretch()

    icon = QPushButton(frame)
    icon.setFlat(True)
    icon.setIcon(QIcon("Icons/search_icon.svg"))
    icon.setIconSize(QSize(26, 22))
    icon.setStyleSheet(
        "QPushButton:pressed {icon: url('Icons/search_icon_clicked.svg')}"
    )
    frame_layout.addWidget(icon)

    layout.addWidget(frame)
    return frame


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(600, 500)
        self.centralArea = QWidget()
        self.setCentralWidget(self.centralArea)
        self.centralArea.setStyleSheet("background-color: #f6f6f6;")
        self.layout = QHBoxLayout()
        self.centralArea.setLayout(self.layout)

        add_button_without_text(parent=self.centralArea, layout=self.layout)
        add_button_with_text(parent=self.centralArea, layout=self.layout, text="Nouveau message ")
        validate_button(parent=self.centralArea, layout=self.layout)
        searchbar_for_navbar(parent=self.centralArea, layout=self.layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
