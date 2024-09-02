import sys
sys.path.append("..")

from PySide6.QtWidgets import QFrame, QWidget, QBoxLayout, QSizePolicy,\
    QHBoxLayout, QLabel, QVBoxLayout, QPushButton
from PySide6.QtGui import QFont, QIcon, QPixmap
from PySide6.QtCore import Qt

from Utils.enumeration import CONTACT_ACRONYM_SIZE as ACRONYM_SIZE
from Utils.responsiveLayout import fitSizeToScreen, fitValueToScreen
from GUI.Components.components import separator
from Assets import icons

class Contact(QFrame):

    def __init__(self, parent: QWidget, Layout: QBoxLayout, user: list):
        super().__init__(parent)

        self.Layout = Layout

        self.name : str = user[0]
        self.mail : str = user[1]
        self.number : str = user[2]
        self.post : str = user[3]
        self.field : str = user[4]

        Layout.addWidget(self)

    def contactAcronym(self, scale: ACRONYM_SIZE) -> QFrame:
        frame = QFrame()
        size = scale.value

        if scale == ACRONYM_SIZE.Large:
            borderSize = 3
            fontSize = scale.value // 3
        elif scale == ACRONYM_SIZE.Medium:
            borderSize = 2
            fontSize = 12
        elif scale == ACRONYM_SIZE.Small:
            borderSize = 1
            fontSize = 9

        borderRadius = size // 2

        frame.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        frame.setFixedSize(fitSizeToScreen(width=size, height=size))
        frame.setStyleSheet(
            f"""
                background-color: #5234A5; 
                border-radius: {fitValueToScreen(value=borderRadius)}px; 
                border: {fitValueToScreen(value=borderSize)}px solid #525252;
            """)

        frameLayout = QHBoxLayout()
        frame.setLayout(frameLayout)

        li = self.name.split(" ")
        fName = li[0]
        lName = li[-1]

        label = QLabel(frame)
        label.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        label.setText((fName[0] + lName[0]).upper())
        label.setFont(QFont('Calibri', fitValueToScreen(value=fontSize), QFont.DemiBold, False))
        label.setStyleSheet(" background-color: none; color: white; border: none;")

        frameLayout.addWidget(label)
        frameLayout.setAlignment(label, Qt.AlignCenter)
        return frame

    def contactDetails(self) -> QFrame:
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        self.setFrameShape(QFrame.NoFrame)
        self.setStyleSheet("background-color: white;")

        frameLayout = QVBoxLayout()
        self.setLayout(frameLayout)

        frameLayout.addStretch(2)

        useracronym = self.contactAcronym(ACRONYM_SIZE.Large)
        frameLayout.addWidget(useracronym)
        frameLayout.setAlignment(useracronym, Qt.AlignCenter)

        username = QLabel(self)
        username.setText(self.name.upper())
        username.setFont(QFont("Montserrat", fitValueToScreen(value=18), QFont.Medium))
        username.setStyleSheet("background-color: none; border: none; color: #3d3d3d")
        frameLayout.addWidget(username)
        frameLayout.setAlignment(username, Qt.AlignCenter)

        userjob = QLabel(self)
        userjob.setText(self.post)
        userjob.setFont(QFont("Montserrat", fitValueToScreen(value=13), QFont.Medium, True))
        userjob.setStyleSheet("background-color: none; border: none; color: #989898")
        frameLayout.addWidget(userjob)
        frameLayout.setAlignment(userjob, Qt.AlignCenter)

        frameLayout.addStretch(1)

        separator(frameLayout, "#888888")

        frameLayout.addStretch(1)

        title = QLabel(self)
        title.setText("Détails du contact")
        title.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        title.setFont(QFont("Montserrat", fitValueToScreen(value=20), QFont.Medium))
        title.setStyleSheet("background-color: none; border: none; color: #3d3d3d")
        frameLayout.addWidget(title)

        usermail = elementContactDetails(self, frameLayout, ":/Icons/mail_contact.svg", "Adresse mail", self.mail)
        frameLayout.addWidget(usermail)

        userphone = elementContactDetails(self, frameLayout, ":/Icons/phone_contact.svg", "Telephone", self.number)
        frameLayout.addWidget(userphone)

        userpost = elementContactDetails(self, frameLayout, ":/Icons/job_contact.svg", "Poste", self.post)
        frameLayout.addWidget(userpost)

        userfield = elementContactDetails(self, frameLayout, ":/Icons/field_contact.svg", "Secteur", self.field)
        frameLayout.addWidget(userfield)

        frameLayout.addStretch(4)

        return self


    def contactCard(self) -> QFrame:
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.setStyleSheet(
            f"""
                QFrame {{border : {fitValueToScreen(value=1)}px solid #DCDCDC; background-color : transparent;}}
                QFrame:hover {{background-color : #E1E2FE;}}
            """ 
        )

        frameLayout = QHBoxLayout()
        self.setLayout(frameLayout)

        acronym = self.contactAcronym(ACRONYM_SIZE.Small)
        frameLayout.addWidget(acronym)

        li = self.name.split(" ")
        fName = li[0].capitalize()
        lName = li[-1].upper()

        username = QLabel(self)
        username.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        username.setStyleSheet("background-color: none; border: none; color: #3d3d3d;")
        username.setText(f"{fName} {lName}")
        username.setFont(QFont("Montserrat", fitValueToScreen(value=10), QFont.DemiBold))
        frameLayout.addWidget(username)

        self.Closebutton = QPushButton(self)
        self.Closebutton.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.Closebutton.setFlat(True)
        self.Closebutton.setIcon(QIcon(":/Icons/close_file.svg"))
        self.Closebutton.setStyleSheet(
            """
                QPushButton{
                    background-color: transparent;
                    border: none;
                }
                QPushButton:pressed {
                    icon: url(':/Icons/close_file_clicked.svg');
                    background-color: transparent;
                    border: none;
                }
            """
        )

        frameLayout.addWidget(self.Closebutton)

        return self
    
    def contactBar(self) -> QFrame:
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.setStyleSheet("background-color: white;")

        frameLayout = QHBoxLayout()
        self.setLayout(frameLayout)
        frameLayout.setContentsMargins(fitValueToScreen(12), fitValueToScreen(12), fitValueToScreen(12), fitValueToScreen(12))

        acronym = self.contactAcronym(ACRONYM_SIZE.Medium)
        frameLayout.addWidget(acronym)

        li = self.name.split(" ")
        fName = li[0].capitalize()
        lName = li[-1].upper()

        username = QLabel(self)
        username.setStyleSheet("background-color: none; border: none; color: #3d3d3d;")
        username.setText(f"{fName} {lName}")
        username.setFont(QFont("Montserrat", fitValueToScreen(value=13), QFont.DemiBold))
        frameLayout.addWidget(username)

        frameLayout.addStretch()

        return self
    


def elementContactDetails(parent: QWidget, Layout: QBoxLayout, path: str, title: str, content: str) -> QFrame:
    frame = QFrame(parent)
    frame.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
    frame.setStyleSheet("background-color: none; border: none;")

    frameLayout = QHBoxLayout()
    frameLayout.setContentsMargins(0, 0, 0, 0)
    frame.setLayout(frameLayout)

    icon = QLabel(frame)
    icon.setPixmap(QPixmap(path))
    icon.setScaledContents(True)
    icon.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
    icon.setStyleSheet("background-color: none; border: none;")
    frameLayout.addWidget(icon)

    textLayout = QVBoxLayout()
    textLayout.setSpacing(0)
    frameLayout.addLayout(textLayout)

    titleLabel = QLabel(title, frame)
    titleLabel.setFont(QFont('Calibri', fitValueToScreen(value=16), QFont.Medium, False))
    titleLabel.setStyleSheet("background-color: none; color: black; border: none;")
    titleLabel.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
    textLayout.addWidget(titleLabel)

    titleContent = QLabel(content, frame)
    titleContent.setFont(QFont('Calibri', fitValueToScreen(value=14), QFont.Medium, True))
    titleContent.setStyleSheet("background-color: none; color: #5d5d5d; border: none;")
    titleContent.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
    textLayout.addWidget(titleContent)

    Layout.addWidget(frame)

    return frame

