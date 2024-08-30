"""
    # This file contains all main headers and bars used commonly in the application
"""

import sys
sys.path.append("..")


from PySide6.QtWidgets import QFrame, QWidget, QBoxLayout,\
    QSizePolicy, QHBoxLayout, QLabel, QVBoxLayout, QButtonGroup,\
    QMessageBox, QStyle, QStatusBar
from PySide6.QtGui import QFont, QPalette, QColor, QPixmap, QIcon
from PySide6.QtCore import Qt, Slot, QSize

from GUI.Components.components import StandardButton,\
    separator, SearchBar,attendanceStatus, user,\
    TitleBarButton, contactAcronym, contactDetails, GroupButton
from Utils.enumeration import CONNEXION_STATUS as STATUS, SIZE
from Utils.responsiveLayout import fitValueToScreen, fitSizeToScreen


from Assets import icons, pictures

# ::::::::BAR::::::::::::: #

class Header(QFrame):
    """
    # This class implements standard header used in the application.

    ## Class attribute

    ( *color* ) backgroundColor : *str*
    ( *color* ) textColor : *str*
    
    ## Methods

    ####  Header(parent: QWidget, Layout: QBoxLayout, text: str) -> QFrame

    *Constructs an header with the given parent, layout and text*

    #### headerWithButton(textButton: str=None) -> QFrame

    *Constructs an header whith a button*
    """

    #Class attribute
    backgroundColor = "white"
    textColor = "#5234a5"

    def __init__(self, parent: QWidget, Layout: QBoxLayout, text: str):
        super().__init__(parent)

        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.setStyleSheet(f"background-color: {Header.backgroundColor};")

        self.frameLayout = QHBoxLayout()
        self.setLayout(self.frameLayout)
        self.frameLayout.setContentsMargins(fitValueToScreen(12), fitValueToScreen(12), fitValueToScreen(12), fitValueToScreen(12))  

        self.title = QLabel(self)
        self.title.setText(text)
        self.title.setFont(QFont("Montserrat", fitValueToScreen(14), QFont.DemiBold))
        palette = self.title.palette()
        palette.setColor(QPalette.WindowText, QColor(Header.textColor))
        self.title.setPalette(palette)
        self.frameLayout.addWidget(self.title)  

        self.frameLayout.addStretch()   

        Layout.addWidget(self)

    def headerWithButton(self, textButton: str=None) -> QFrame:
        self.frameLayout.addStretch() 
        self.button = StandardButton(self, self.frameLayout).ButtonWithText(textButton)

        return self
    
class Sidebar(QFrame):
    """
    # This class is used to create the application's side bar
    """

    # Class attribute
    backgroundColor = "#5234A5"
    separatorColor = "white"

    def __init__(self, parent: QWidget, Layout: QBoxLayout):
        super().__init__(parent)

        self.setFixedWidth(fitSizeToScreen(width=186, height=None))
        self.setStyleSheet(f"background-color: {Sidebar.backgroundColor};")
        self.setFrameShape(QFrame.NoFrame)
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)

        self.frameLayout = QVBoxLayout()
        self.setLayout(self.frameLayout)
        self.frameLayout.setContentsMargins(0, fitValueToScreen(24), 0, 0)
        self.frameLayout.setSpacing(0)

        self.logo = QLabel(self)
        self.logo.setPixmap(QPixmap(":/Pictures/full_logo.png"))
        self.logo.setScaledContents(True)
        self.logo.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.logo.setFixedSize(fitSizeToScreen(width=140, height=50))
        self.frameLayout.addWidget(self.logo)
        self.frameLayout.setAlignment(self.logo, Qt.AlignHCenter) 

        self.groupbutton = QButtonGroup(self)
        self.groupbutton.setObjectName("groupbutton")
        self.groupbutton.setExclusive(True)

        self.frameLayout.addStretch(3)

        self.dashboard = GroupButton(self, "Dashboard", self.frameLayout, self.groupbutton, 0).sidebarButton(uncheckedIconPath=":/Icons/unchecked_dashboard.svg", checkedIconPath=":/Icons/checked_dashboard.svg")
        self.report = GroupButton(self, "Rapport", self.frameLayout, self.groupbutton, 1).sidebarButton(uncheckedIconPath=":/Icons/unchecked_reporting.svg", checkedIconPath=":/Icons/checked_reporting.svg")
        self.tracking = GroupButton(self, "Suivi", self.frameLayout, self.groupbutton, 2).sidebarButton(uncheckedIconPath=":/Icons/unchecked_collection.svg", checkedIconPath=":/Icons/checked_collection.svg")
        self.location = GroupButton(self, "Site", self.frameLayout, self.groupbutton, 3).sidebarButton(uncheckedIconPath=":/Icons/unchecked_map.svg", checkedIconPath=":/Icons/checked_map.svg")
        self.graph = GroupButton(self, "Analyse", self.frameLayout, self.groupbutton, 4).sidebarButton(uncheckedIconPath=":/Icons/unchecked_tracking.svg", checkedIconPath=":/Icons/checked_tracking.svg")

        self.frameLayout.addStretch(4)

        separator(self, self.frameLayout, Sidebar.separatorColor)

        self.message = GroupButton(self, "Message", self.frameLayout, self.groupbutton, 5).sidebarButton(uncheckedIconPath=":/Icons/unchecked_message.svg", checkedIconPath=":/Icons/checked_message.svg")
        self.admin = GroupButton(self, "Administration", self.frameLayout, self.groupbutton, 6).sidebarButton(uncheckedIconPath=":/Icons/unchecked_admin.svg", checkedIconPath=":/Icons/checked_admin.svg")
        self.logOut = GroupButton(self, "Déconnexion", self.frameLayout, self.groupbutton, 7).sidebarButton(uncheckedIconPath=":/Icons/unchecked_logout.svg", checkedIconPath=":/Icons/checked_logout.svg")

        self.frameLayout.addStretch(2)

        Layout.addWidget(self)
        

class TitleBar(QFrame):
    """
    # This class is used to create the application's title bar
    """

    # Class attribute
    background = "white"
    

    def __init__(self, parent: QWidget, Layout: QBoxLayout):
        super().__init__(parent)

        self.name = "Paul Goma"
        self.mail = "Paulgoma07@gmail.com"
        

        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.setFrameShape(QFrame.NoFrame)
        self.setStyleSheet(f"background-color: {TitleBar.background};")

        self.frameLayout = QHBoxLayout()
        self.frameLayout.setContentsMargins(fitValueToScreen(32), 0, 0, 0) 
        self.setLayout(self.frameLayout)

        self.searchbar = SearchBar(self, self.frameLayout).searchbarForTitleBar()

        self.frameLayout.addStretch(12)

        self.notification = TitleBarButton(self, self.frameLayout)
        self.notification.setIconSize(fitSizeToScreen(25, 29))
        self.notification.setIcon(QIcon(":/Icons/not_notified_icon.svg"))

        self.frameLayout.addStretch(1)

        self.status = attendanceStatus(self, self.frameLayout)
        self.frameLayout.addStretch(1)
        self.user = user(self, self.frameLayout, self.name, self.mail)
        self.frameLayout.addStretch(1)

        self.hideButton  = TitleBarButton(self, self.frameLayout)
        self.hideButton.setIcon(self.style().standardIcon(QStyle.SP_TitleBarMinButton))
        self.hideButton.clicked.connect(parent.parent().showMinimized)
        self.resizeButton  = TitleBarButton(self, self.frameLayout)
        self.resizeButton.setIcon(self.style().standardIcon(QStyle.SP_TitleBarMaxButton))
        self.resizeButton.clicked.connect(self.resizeWindow)
        self.closeButton  = TitleBarButton(self, self.frameLayout, True)
        self.closeButton.setIcon(self.style().standardIcon(QStyle.SP_TitleBarCloseButton))
        self.closeButton.clicked.connect(self.closeApp)

        self.Layout = Layout
        self.Layout.addWidget(self)
    
    @Slot()
    def setNotification(self, number: int):
        if number == 0:
            self.notification.setIcon(QIcon(":/Icons/not_notified_icon.svg"))
        elif number > 0:
            self.notification.setIcon(QIcon(":/Icons/notified_icon.svg"))

    @Slot()
    def setStatus(self, status: STATUS) -> QLabel:
        self.status.setPixmap(QPixmap(":/Icons/online.svg" if status == STATUS.OnLine else ":/Icons/offline.svg"))

    @Slot()
    def closeApp(self):
        dialog = closeApp(deconnection=False)
        if dialog.exec():
            self.parent().parent().close()


    @Slot()
    def resizeWindow(self): 
        if self.parent().parent().isMaximized():
            self.resizeButton.setIcon(self.style().standardIcon(QStyle.SP_TitleBarNormalButton))
            self.parent().parent().showNormal()
        else:
            self.resizeButton.setIcon(self.style().standardIcon(QStyle.SP_TitleBarMaxButton))
            self.parent().parent().showMaximized() 

class Statusbar(QStatusBar):
    """
    This class is used to create the application's status bar
    """

    # Class attributes
    backgroundColor = "white"
    borderColor = "#f6f6f6"
    textColor = "#525252"

    def __init__(self):
        super().__init__()

        self.setStyleSheet(f"background-color: {Statusbar.backgroundColor}; padding-right: {fitValueToScreen(value=10)}px;")

        self.internetAccess = self.createFrame()
        self.databaseAccess = self.createFrame()

    def setInternetConnection(self, status: STATUS):
        self.icon.setPixmap(QPixmap(":/Icons/online.svg" if status == STATUS.OnLine else ":/Icons/offline.svg"))
        self.text.setText("Accès internet" if status == STATUS.OnLine else "Pas d'accès internet")

    def setDatabaseConnection(self, status: STATUS):
        self.icon.setPixmap(QPixmap(":/Icons/database_connected.svg" if status == STATUS.OnLine else ":/Icons/database_not_connected.svg"))
        self.text.setText("Connection réussie" if status == STATUS.OnLine else "Accès refusé")        

    
    def createFrame(self) -> QFrame:
        frame = QFrame(self)
        frame.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        frame.setStyleSheet("background-color: none; border: none;")

        Layout = QHBoxLayout()
        Layout.setContentsMargins(0, 0, 0, 0)
        frame.setLayout(Layout)

        self.icon = QLabel(self)
        self.icon.setStyleSheet("background-color: none; border-left: none;")
        self.icon.setScaledContents(True)
        self.icon.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        Layout.addWidget(self.icon)

        self.text = QLabel(self)
        self.text.setStyleSheet(f"background-color: none; border-left: none; color: {Statusbar.textColor}")
        self.text.setFont(QFont('Calibri', fitValueToScreen(value=12), QFont.Normal, False))
        self.text.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        Layout.addWidget(self.text)

        self.addPermanentWidget(frame)

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
class EmptyPage(QFrame):
    """
    # This class implements an empty page to inform that there is no data or that it is under maintenance.

    ## Methods

    ####  EmptyPage(title: str, imagePath: str, text: str) -> QFrame

    *Constructs an empty page with the given title, image and text*

    #### emptyPageWithButton(textButton: str, secondText: str) -> QFrame

    *Constructs an empty page whith a button to add data*
    """

    def __init__(self, title: str, imagePath: str, text: str):
        super().__init__()

        self.setFrameShape(QFrame.NoFrame)
        self.setStyleSheet("background-color: none; border: none;")
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.frameLayout = QVBoxLayout()
        self.setLayout(self.frameLayout)

        self.header = Header(self, self.frameLayout, title)
        self.frameLayout.setAlignment(self.header, Qt.AlignTop)

        self.imageLayout = QHBoxLayout()
        self.frameLayout.addLayout(self.imageLayout)
        self.frameLayout.setAlignment(self.imageLayout, Qt.AlignCenter)

        self.image = QLabel(self)
        self.image.setPixmap(QPixmap(imagePath))
        self.image.setScaledContents(True)
        self.image.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.image.setStyleSheet("background-color: none; border: none;")
        self.imageLayout.addWidget(self.image)

        self.label = QLabel(self)
        self.label.setText(text)
        self.label.setFont(QFont("Montserrat", fitValueToScreen(value=20), QFont.Medium))
        self.label.setStyleSheet("QLabel { color: black; background: none; border: none;}")
        self.label.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.frameLayout.addWidget(self.label)
        self.frameLayout.setAlignment(self.label, Qt.AlignCenter)

        self.frameLayout.addStretch()

    def emptyPageWithButton(self, textButton: str, secondText: str) -> QFrame:
        self.header.headerWithButton(textButton)

        self.textLayout = QHBoxLayout()
        self.frameLayout.addLayout(self.textLayout)
        self.frameLayout.setAlignment(self.textLayout, Qt.AlignCenter)

        self.textLayout.addStretch(1)
        
        self.secondLabel = QLabel(self)
        self.secondLabel.setText(secondText)
        self.secondLabel.setFont(QFont("Montserrat", fitValueToScreen(value=20), QFont.Medium))
        self.secondLabel.setStyleSheet("QLabel { color: black; background: none; border: none;}")
        self.secondLabel.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.textLayout.addWidget(self.secondLabel)

        self.button = StandardButton(self, self.textLayout, 45, 45).ButtonWithoutText()

        self.textLayout.addStretch(1)

        self.frameLayout.addStretch(2)

        return self

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
def PopUp(title: str, message: str, icon: QMessageBox.Icon) -> QMessageBox:
    box_error = QMessageBox()
    box_error.setWindowIcon(QIcon(":/Pictures/icon.png"))
    box_error.setIcon(icon)
    box_error.setWindowTitle(title)
    box_error.setText(message)
    box_error.exec()

    return box_error

def closeApp(deconnection: bool) -> QMessageBox:
    box = QMessageBox()
    box.setWindowTitle("Voulez-vous vraiment terminer votre session ?" if deconnection else "Fermeture de l'application")
    box.setWindowIcon(QIcon(":/Pictures/icon.png"))
    box.setIcon(QMessageBox.Question)
    box.setText("Souhaitez-vous fermer l'application ?")
    acceptButton = box.addButton("Oui", QMessageBox.AcceptRole)
    rejectButton = box.addButton("Non", QMessageBox.RejectRole)

    acceptButton.clicked.connect(box.accept)
    rejectButton.clicked.connect(box.reject)

    return box



