"""
    # This file contains all main headers and bars used commonly in the application
"""

import sys
sys.path.append("..")


from PySide6.QtWidgets import QFrame, QWidget, QBoxLayout,\
    QSizePolicy, QHBoxLayout, QLabel, QVBoxLayout, QButtonGroup,\
    QPushButton
from PySide6.QtGui import QFont, QPalette, QColor, QPixmap
from PySide6.QtCore import Qt

from GUI.Components.components import addButtonWithText, validateButton,\
    sidebarButton, separator, searchbarForNavbar, attendanceStatus, \
    user, closeWindowButton, resizeWindowButton, minimizeWindowButton,\
    addButtonWithoutText
from Utils.enumeration import CONNEXION_STATUS as STATUS
from Utils.responsiveLayout import fitValueToScreen

from Assets import icons, pictures

# ::::::::BAR::::::::::::: #

# Headers
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
    palette.setColor(QPalette.WindowText, QColor("#5234a5"))  # Couleur du texte
    title.setPalette(palette)
    frameLayout.addWidget(title)

    frameLayout.addStretch()

    button = addButtonWithText(frame, frameLayout, textButton)
    button.setObjectName("button")
    
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
    palette.setColor(QPalette.WindowText, QColor("#5234a5"))
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
    palette.setColor(QPalette.WindowText, QColor("#5234a5"))
    title.setPalette(palette)
    frameLayout.addWidget(title)

    frameLayout.addStretch()
    
    layout.addWidget(frame)
    return frame

# Sidebar
def sidebar(parent: QWidget, layout: QBoxLayout) -> QFrame:
    frame = QFrame(parent)
    frame.setFixedWidth(186)
    frame.setStyleSheet("background-color: #5234A5;")
    frame.setFrameShape(QFrame.NoFrame)
    frame.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)

    frameLayout = QVBoxLayout()
    frame.setLayout(frameLayout)
    frameLayout.setContentsMargins(0, 24, 0, 0)
    
    logo = QLabel(frame)
    logo.setPixmap(QPixmap(":/Pictures/full_logo.png"))
    logo.setScaledContents(True)
    logo.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
    logo.setFixedSize(140, 50)
    frameLayout.addWidget(logo)
    frameLayout.setAlignment(logo, Qt.AlignHCenter)

    groupbutton = QButtonGroup(frame)
    groupbutton.setObjectName("groupbutton")
    groupbutton.setExclusive(True)

    frameLayout.addStretch(2)

    dashboard = sidebarButton(parent=frame, text="  Dashboard", uncheckedIconPath=":/Icons/unchecked_dashboard.svg", checkedIconPath=":/Icons/checked_dashboard.svg", layout=frameLayout, group=groupbutton)
    dashboard.setObjectName("dashboard")

    report = sidebarButton(parent=frame, text="  Rapport", uncheckedIconPath=":/Icons/unchecked_reporting.svg", checkedIconPath=":/Icons/checked_reporting.svg", layout=frameLayout, group=groupbutton)
    report.setObjectName("report")

    tracking = sidebarButton(parent=frame, text="  Suivi", uncheckedIconPath=":/Icons/unchecked_collection.svg", checkedIconPath=":/Icons/checked_collection.svg", layout=frameLayout, group=groupbutton)
    tracking.setObjectName("tracking")

    location = sidebarButton(parent=frame, text="  Site", uncheckedIconPath=":/Icons/unchecked_map.svg", checkedIconPath=":/Icons/checked_map.svg", layout=frameLayout, group=groupbutton)
    location.setObjectName("location")

    graph = sidebarButton(parent=frame, text="  Analyse", uncheckedIconPath=":/Icons/unchecked_tracking.svg", checkedIconPath=":/Icons/checked_tracking.svg", layout=frameLayout, group=groupbutton)
    graph.setObjectName("graph")

    frameLayout.addStretch(2)

    separator(parent=frame, layout=frameLayout)

    frameLayout.addStretch(2)

    message = sidebarButton(parent=frame, text="  Message", uncheckedIconPath=":/Icons/unchecked_message.svg", checkedIconPath=":/Icons/checked_message.svg", layout=frameLayout, group=groupbutton)
    message.setObjectName("message")

    admin = sidebarButton(parent=frame, text="  Admistration", uncheckedIconPath=":/Icons/unchecked_admin.svg", checkedIconPath=":/Icons/checked_admin.svg", layout=frameLayout, group=groupbutton)
    admin.setObjectName("admin")

    logOut = sidebarButton(parent=frame, text="  Déconnexion", uncheckedIconPath=":/Icons/unchecked_logout.svg", checkedIconPath=":/Icons/checked_logout.svg", layout=frameLayout, group=groupbutton)
    logOut.setObjectName("logOut")

    frameLayout.addStretch(4)

    layout.addWidget(frame)
    return frame

# Titlebar
def titlebar(parent: QWidget, layout: QBoxLayout, connexionstatus: STATUS, name: str, mail: str) -> QFrame:
    frame = QFrame(parent)
    frame.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
    frame.setFrameShape(QFrame.NoFrame)
    frame.setStyleSheet("background-color: white;")

    frameLayout = QHBoxLayout()
    frame.setLayout(frameLayout)
    frameLayout.setContentsMargins(32, 0, 0, 0)

    searchbar = searchbarForNavbar(frame, frameLayout)
    searchbar.setObjectName("searchbar")

    frameLayout.addStretch(12)

    status = attendanceStatus(frame, frameLayout, connexionstatus)
    status.setObjectName("status")

    frameLayout.addStretch(1)

    person =user(frame, frameLayout, name, mail)
    person.setObjectName("person")

    frameLayout.addStretch(1)

    minimizeButton = minimizeWindowButton(frame, frameLayout)
    minimizeButton.setObjectName("minimizeButton")

    resizeButton = resizeWindowButton(frame, frameLayout)
    resizeButton.setObjectName("resizeButton")

    closeButton = closeWindowButton(frame, frameLayout)
    closeButton.setObjectName("closeButton")

    layout.addWidget(frame)
    return frame


# ::::::::empty pages::::::::::::: #
def createEmptypageWithButton(title: str, imagePath: str, textButton: str, firstText: str, secondText: str) -> QFrame:
    frame = QFrame()
    frame.setFrameShape(QFrame.NoFrame)
    frame.setStyleSheet("background-color: none; border: none;")
    frame.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

    frameLayout = QVBoxLayout()
    frame.setLayout(frameLayout)

    bar = header(parent=frame, layout=frameLayout, text=title, textButton=textButton)
    button = bar.findChild(QPushButton, "button", Qt.FindDirectChildrenOnly)
    button.setObjectName("HeaderButton")
    frameLayout.setAlignment(bar, Qt.AlignTop)

    imageLayout = QHBoxLayout()
    frameLayout.addLayout(imageLayout)
    frameLayout.setAlignment(imageLayout, Qt.AlignCenter)

    image = QLabel(frame)
    image.setPixmap(QPixmap(imagePath))
    image.setScaledContents(True)
    image.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
    image.setStyleSheet("background-color: none; border: none;")
    imageLayout.addWidget(image)

    firstLabel = QLabel(frame)
    firstLabel.setText(firstText)
    firstLabel.setFont(QFont("Montserrat", fitValueToScreen(value=20), QFont.Medium))
    firstLabel.setStyleSheet("QLabel { color: black; background: none; border: none;}")
    firstLabel.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
    frameLayout.addWidget(firstLabel)
    frameLayout.setAlignment(firstLabel, Qt.AlignCenter)

    textLayout = QHBoxLayout()
    frameLayout.addLayout(textLayout)
    frameLayout.setAlignment(textLayout, Qt.AlignCenter)

    textLayout.addStretch(1)

    secondLabel = QLabel(frame)
    secondLabel.setText(secondText)
    secondLabel.setFont(QFont("Montserrat", fitValueToScreen(value=20), QFont.Medium))
    secondLabel.setStyleSheet("QLabel { color: black; background: none; border: none;}")
    secondLabel.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
    textLayout.addWidget(secondLabel)

    buttonWithoutText = addButtonWithoutText(parent=frame, layout=textLayout)
    buttonWithoutText.setObjectName("buttonWithoutText")

    textLayout.addStretch(1)

    return frame