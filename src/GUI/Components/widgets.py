"""
    # This file contains all main headers and bars used commonly in the application
"""

import sys
sys.path.append("..")


from PySide6.QtWidgets import QFrame, QWidget, QBoxLayout,\
    QSizePolicy, QHBoxLayout, QLabel, QVBoxLayout, QButtonGroup,\
    QPushButton, QMessageBox
from PySide6.QtGui import QFont, QPalette, QColor, QPixmap, QIcon
from PySide6.QtCore import Qt

from GUI.Components.components import addButtonWithText, validateButton,\
    sidebarButton, separator, searchbarForNavbar, attendanceStatus, \
    user, closeWindowButton, resizeWindowButton, minimizeWindowButton,\
    addButtonWithoutText, contactAcronym, contactDetails
from Utils.enumeration import CONNEXION_STATUS as STATUS, SIZE
from Utils.responsiveLayout import fitValueToScreen, fitSizeToScreen

from Assets import icons, pictures

# ::::::::BAR::::::::::::: #

# Headers
def header(parent: QWidget, layout: QBoxLayout, text: str, textButton: str) -> QFrame:
    frame = QFrame(parent)
    frame.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
    frame.setStyleSheet("background-color: white;")

    frameLayout = QHBoxLayout()
    frame.setLayout(frameLayout)
    frameLayout.setContentsMargins(fitValueToScreen(12), fitValueToScreen(12), fitValueToScreen(12), fitValueToScreen(12))

    title = QLabel(frame)
    title.setText(text)
    title.setFont(QFont("Montserrat", fitValueToScreen(14), QFont.DemiBold))
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
    frameLayout.setContentsMargins(fitValueToScreen(12), fitValueToScreen(12), fitValueToScreen(12), fitValueToScreen(12))

    title = QLabel(frame)
    title.setText(text)
    title.setFont(QFont("Montserrat", fitValueToScreen(14), QFont.DemiBold))
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
    frameLayout.setContentsMargins(fitValueToScreen(12), fitValueToScreen(12), fitValueToScreen(12), fitValueToScreen(12))

    title = QLabel(frame)
    title.setText(text)
    title.setFont(QFont("Montserrat", fitValueToScreen(14), QFont.DemiBold))
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
    frame.setFixedWidth(fitSizeToScreen(width=186, height=None))
    frame.setStyleSheet("background-color: #5234A5;")
    frame.setFrameShape(QFrame.NoFrame)
    frame.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)

    frameLayout = QVBoxLayout()
    frame.setLayout(frameLayout)
    frameLayout.setContentsMargins(0, fitValueToScreen(24), 0, 0)
    frameLayout.setSpacing(0)
    
    logo = QLabel(frame)
    logo.setPixmap(QPixmap(":/Pictures/full_logo.png"))
    logo.setScaledContents(True)
    logo.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
    logo.setFixedSize(fitSizeToScreen(width=140, height=50))
    frameLayout.addWidget(logo)
    frameLayout.setAlignment(logo, Qt.AlignHCenter)

    groupbutton = QButtonGroup(frame)
    groupbutton.setObjectName("groupbutton")
    groupbutton.setExclusive(True)

    frameLayout.addStretch(3)

    dashboard = sidebarButton(parent=frame, text="  Dashboard", uncheckedIconPath=":/Icons/unchecked_dashboard.svg", checkedIconPath=":/Icons/checked_dashboard.svg", layout=frameLayout, group=groupbutton)
    dashboard.setChecked(True)
    dashboard.setObjectName("dashboard")
    groupbutton.setId(dashboard, 0)

    report = sidebarButton(parent=frame, text="  Rapport", uncheckedIconPath=":/Icons/unchecked_reporting.svg", checkedIconPath=":/Icons/checked_reporting.svg", layout=frameLayout, group=groupbutton)
    report.setObjectName("report")
    groupbutton.setId(report, 1)

    tracking = sidebarButton(parent=frame, text="  Suivi", uncheckedIconPath=":/Icons/unchecked_collection.svg", checkedIconPath=":/Icons/checked_collection.svg", layout=frameLayout, group=groupbutton)
    tracking.setObjectName("tracking")
    groupbutton.setId(tracking, 2)

    location = sidebarButton(parent=frame, text="  Site", uncheckedIconPath=":/Icons/unchecked_map.svg", checkedIconPath=":/Icons/checked_map.svg", layout=frameLayout, group=groupbutton)
    location.setObjectName("location")
    groupbutton.setId(location, 3)

    graph = sidebarButton(parent=frame, text="  Analyse", uncheckedIconPath=":/Icons/unchecked_tracking.svg", checkedIconPath=":/Icons/checked_tracking.svg", layout=frameLayout, group=groupbutton)
    graph.setObjectName("graph")
    groupbutton.setId(graph, 4)

    frameLayout.addStretch(4)

    separator(parent=frame, layout=frameLayout, color="#ffffff")

    message = sidebarButton(parent=frame, text="  Message", uncheckedIconPath=":/Icons/unchecked_message.svg", checkedIconPath=":/Icons/checked_message.svg", layout=frameLayout, group=groupbutton)
    message.setObjectName("message")
    groupbutton.setId(message, 5)

    admin = sidebarButton(parent=frame, text="  Admistration", uncheckedIconPath=":/Icons/unchecked_admin.svg", checkedIconPath=":/Icons/checked_admin.svg", layout=frameLayout, group=groupbutton)
    admin.setObjectName("admin")
    groupbutton.setId(admin, 6)

    logOut = sidebarButton(parent=frame, text="  Déconnexion", uncheckedIconPath=":/Icons/unchecked_logout.svg", checkedIconPath=":/Icons/checked_logout.svg", layout=frameLayout, group=groupbutton)
    logOut.setObjectName("logOut")
    groupbutton.setId(logOut, 7)

    frameLayout.addStretch(2)

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
    frameLayout.setContentsMargins(fitValueToScreen(32), 0, 0, 0)

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


# Message bar
def messageBar(parent: QWidget, layout: QBoxLayout, connexionstatus: STATUS, fName: str, lName: str) -> QFrame:
    frame = QFrame(parent)
    frame.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
    frame.setStyleSheet("background-color: white;")

    frameLayout = QHBoxLayout()
    frame.setLayout(frameLayout)
    frameLayout.setContentsMargins(fitValueToScreen(12), fitValueToScreen(12), fitValueToScreen(12), fitValueToScreen(12))

    contactAcronym(parent=frame, layout=frameLayout, fName=fName, lName=lName, size=SIZE.Short)

    username = QLabel(frame)
    username.setText(f"{fName.capitalize() + " " + lName.upper()}")
    username.setFont(QFont("Montserrat", fitValueToScreen(13), QFont.DemiBold))
    palette = username.palette()
    palette.setColor(QPalette.WindowText, QColor("#3d3d3d"))
    username.setPalette(palette)
    frameLayout.addWidget(username)

    if connexionstatus == STATUS.OnLine:
        status = QFrame(frame)
        status.setFrameShape(QFrame.NoFrame)
        status.setFixedSize(fitSizeToScreen(width=12, height=12))
        status.setStyleSheet(f"background-color: #28FF98; border-radius: {fitValueToScreen(6)}; border: none;")
        frameLayout.addWidget(status)

    frameLayout.addStretch()
    
    layout.addWidget(frame)
    return frame

# ::::::::Pages::::::::::::: #

# empty page
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

    frameLayout.addStretch()

    return frame

# page in maintenance
def displayPageInMaintenance(title: str) -> QFrame:
    frame = QFrame()
    frame.setFrameShape(QFrame.NoFrame)
    frame.setStyleSheet("background-color: none; border: none;")
    frame.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

    frameLayout = QVBoxLayout()
    frame.setLayout(frameLayout)

    headerWithoutButton(parent=frame, layout=frameLayout, text=title)

    imageLayout = QHBoxLayout()
    frameLayout.addLayout(imageLayout)
    frameLayout.setAlignment(imageLayout, Qt.AlignCenter)

    image = QLabel(frame)
    image.setPixmap(QPixmap(":/Pictures/maintenance.png"))
    image.setScaledContents(True)
    image.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
    image.setStyleSheet("background-color: none; border: none;")
    imageLayout.addWidget(image)

    label = QLabel(frame)
    label.setText("Section en cours de création")
    label.setFont(QFont("Montserrat", fitValueToScreen(value=20), QFont.Medium))
    label.setStyleSheet("QLabel { color: black; background: none; border: none;}")
    label.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
    frameLayout.addWidget(label)
    frameLayout.setAlignment(label, Qt.AlignCenter)

    frameLayout.addStretch()

    return frame

# no task page
def noTaskPage() -> QFrame:
    frame = QFrame()
    frame.setFrameShape(QFrame.NoFrame)
    frame.setStyleSheet("background-color: none; border: none;")
    frame.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

    frameLayout = QVBoxLayout()
    frame.setLayout(frameLayout)

    headerWithoutButton(parent=frame, layout=frameLayout, text="Suivi des missions et interventions")

    imageLayout = QHBoxLayout()
    frameLayout.addLayout(imageLayout)
    frameLayout.setAlignment(imageLayout, Qt.AlignCenter)

    image = QLabel(frame)
    image.setPixmap(QPixmap(":/Pictures/no_task.png"))
    image.setScaledContents(True)
    image.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
    image.setStyleSheet("background-color: none; border: none;")
    imageLayout.addWidget(image)

    label = QLabel(frame)
    label.setText("Aucune mission en vue")
    label.setFont(QFont("Montserrat", fitValueToScreen(value=20), QFont.Medium))
    label.setStyleSheet("QLabel { color: black; background: none; border: none;}")
    label.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
    frameLayout.addWidget(label)
    frameLayout.setAlignment(label, Qt.AlignCenter)

    frameLayout.addStretch()

    return frame

# ::::::::Contact::::::::::::: #
def contact(parent: QWidget, layout: QBoxLayout, fName: str, lName: str, mail: str, phone: str, job: str, field: str) -> QFrame:
    frame = QFrame(parent)
    frame.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
    frame.setFrameShape(QFrame.NoFrame)
    frame.setStyleSheet("background-color: white; border: none;")

    frameLayout = QVBoxLayout()
    frame.setLayout(frameLayout)

    frameLayout.addStretch(2)

    acronymLayout = QHBoxLayout()
    frameLayout.addLayout(acronymLayout)

    acronym = contactAcronym(parent=frame, layout=acronymLayout, fName=fName, lName=lName, size=SIZE.Long)
    acronymLayout.addWidget(acronym)

    nameLayout = QHBoxLayout()
    nameLayout.setAlignment(Qt.AlignCenter)
    frameLayout.addLayout(nameLayout)

    username = QLabel(frame)
    username.setText(f"{fName.capitalize() + " " + lName.upper()}")
    username.setFont(QFont("Montserrat", fitValueToScreen(value=24), QFont.Medium))
    username.setStyleSheet("background-color: none; border: none; color: #3d3d3d")
    nameLayout.addWidget(username)

    jobLayout = QHBoxLayout()
    jobLayout.setAlignment(Qt.AlignCenter)
    frameLayout.addLayout(jobLayout)

    userjob = QLabel(frame)
    userjob.setText(job)
    userjob.setFont(QFont("Montserrat", fitValueToScreen(value=13), QFont.Medium, True))
    userjob.setStyleSheet("background-color: none; border: none; color: #989898")
    jobLayout.addWidget(userjob)

    frameLayout.addStretch(1)

    separator(parent=frame, layout=frameLayout, color="#888888")

    frameLayout.addStretch(1)

    title = QLabel(frame)
    title.setText("Détails du contact")
    title.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
    title.setFont(QFont("Montserrat", fitValueToScreen(value=20), QFont.Medium))
    title.setStyleSheet("background-color: none; border: none; color: #3d3d3d")
    frameLayout.addWidget(title)

    frameLayout.addStretch(1)

    contactDetails(parent=frame, layout=frameLayout, mail=mail, phone=phone, job=job, field=field)

    frameLayout.addStretch(4)

    layout.addWidget(frame)
    
    return frame

# ::::::::Pop up::::::::::::: #
def displayMessageError(title: str, message: str) -> QMessageBox:
    box_error = QMessageBox()
    box_error.setWindowIcon(QIcon(":/Pictures/icon.png"))
    box_error.setIcon(QMessageBox.Critical)
    box_error.setWindowTitle(title)
    box_error.setText(message)
    box_error.exec()

    return box_error

def closeApp() -> QMessageBox:
    box = QMessageBox()
    box.setWindowTitle("Fermeture de l'application")
    box.setWindowIcon(QIcon(":/Pictures/icon.png"))
    box.setIcon(QMessageBox.Question)
    box.setText("Souhaitez-vous fermer l'application ?")
    acceptButton = box.addButton("Oui", QMessageBox.AcceptRole)
    rejectButton = box.addButton("Non", QMessageBox.RejectRole)

    acceptButton.clicked.connect(box.accept)
    rejectButton.clicked.connect(box.reject)

    return box
