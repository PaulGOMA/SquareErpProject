import sys
sys.path.append("..")

from PySide6.QtWidgets import QFrame, QWidget, QBoxLayout, QSizePolicy,\
    QHBoxLayout, QLabel, QVBoxLayout, QPushButton
from PySide6.QtGui import QFont, QIcon
from PySide6.QtCore import Qt

from Utils.enumeration import CONTACT_ACRONYM_SIZE as SIZE
from Utils.responsiveLayout import fitSizeToScreen, fitValueToScreen
from GUI.Components.components import elementContactDetails, separator

class Contact(QFrame):

    def __init__(self, parent: QWidget, Layout: QBoxLayout, user: list):
        super().__init__(parent)

        self.Layout = Layout

        self.name : str = user[0]
        self.mail : str = user[1]
        self.number : str = user[2]
        self.post : str = user[4]
        self.field : str = user[5]

        Layout.addWidget(self)

    def contactAcronym(self, scale: SIZE) -> QFrame:

        size = scale.value

        fontSize = scale.value // 3

        if scale == SIZE.Large:
            borderSize = 3
        elif scale == SIZE.Medium:
            borderSize = 2
        elif scale == SIZE.Small:
            borderSize = 1

        borderRadius = size // 2

        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.setFixedSize(fitSizeToScreen(width=size, height=size))
        self.setStyleSheet(
            f"""
                background-color: #5234A5; 
                border-radius: {fitValueToScreen(value=borderRadius)}px; 
                border: {fitValueToScreen(value=borderSize)}px solid #525252;
            """)

        frameLayout = QHBoxLayout()
        self.setLayout(frameLayout)

        li = self.name.split(" ")
        fName = li[0]
        lName = li[-1]

        label = QLabel(self)
        label.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        label.setText((fName[0] + lName[0]).upper())
        label.setFont(QFont('Calibri', fitValueToScreen(value=fontSize), QFont.Medium, False))
        label.setStyleSheet(" background-color: none; color: white; border: none;")

        frameLayout.addWidget(label)
        frameLayout.setAlignment(label, Qt.AlignCenter)
        return self

    def contactDetails(self) -> QFrame:
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        self.setStyleSheet("background-color: white; border: none;")

        frameLayout = QVBoxLayout()
        self.setLayout(frameLayout)

        frameLayout.addStretch(2)

        useracronym = self.contactAcronym(SIZE.Large)
        frameLayout.addWidget(useracronym)
        frameLayout.setAlignment(useracronym, Qt.AlignCenter)

        username = QLabel(self)
        username.setText(self.name.upper())
        username.setFont(QFont("Montserrat", fitValueToScreen(value=24), QFont.Medium))
        username.setStyleSheet("background-color: none; border: none; color: #3d3d3d")
        frameLayout.addWidget(username)
        frameLayout.setAlignment(username, Qt.AlignCenter)

        userjob = QLabel(self)
        userjob.setText(self.post)
        userjob.setFont(QFont("Montserrat", fitValueToScreen(value=13), QFont.Medium, True))
        userjob.setStyleSheet("background-color: none; border: none; color: #989898")
        frameLayout.addWidget(userjob)
        frameLayout.setAlignment(userjob, Qt.AlignCenter)

        separator(frameLayout, "#888888")

        title = QLabel(self)
        title.setText("Détails du contact")
        title.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        title.setFont(QFont("Montserrat", fitValueToScreen(value=20), QFont.Medium))
        title.setStyleSheet("background-color: none; border: none; color: #3d3d3d")
        frameLayout.addWidget(title)

        frameLayout.addStretch(1)

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
        self.setStyleSheet(
            f"""
                QFrame {{border : {fitValueToScreen(value=1)}px solid #DCDCDC; background-color : transparent;}}
                QFrame:hover {{background-color : #E1E2FE;}}
            """ 
        )

        frameLayout = QHBoxLayout()
        self.setLayout(frameLayout)

        acronym = self.contactAcronym(SIZE.Small)
        frameLayout.addWidget(acronym)

        username = QLabel(self)
        username.setStyleSheet("background-color: none; border: none; color: #3d3d3d;")
        username.setText(self.name)
        username.setFont(QFont("Montserrat", fitValueToScreen(value=10), QFont.Medium))

        self.Closebutton = QPushButton(self)
        self.Closebutton.setFlat(True)
        self.button.setIcon(QIcon(":/Icons/close_file.svg"))
        self.Closebutton.setStyleSheet(
            """
                QPushButton{
                    background-color: transparent;
                    border: none;
                }
                QPushButton:pressed {
                    icon: "url(':/Icons/close_file_clicked.svg')";
                    background-color: transparent;
                    border: none;
                }
            """
        )

        frameLayout.addWidget(self.Closebutton)

        return self
    
    def messageBar(self) -> QFrame:
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.setStyleSheet("background-color: white;")

        frameLayout = QHBoxLayout()
        self.setLayout(frameLayout)
        frameLayout.setContentsMargins(fitValueToScreen(12), fitValueToScreen(12), fitValueToScreen(12), fitValueToScreen(12))

        acronym = self.contactAcronym(SIZE.Medium)
        frameLayout.addWidget(acronym)

        username = QLabel(self)
        username.setStyleSheet("background-color: none; border: none; color: #3d3d3d;")
        username.setText(self.name)
        username.setFont(QFont("Montserrat", fitValueToScreen(value=13), QFont.DemiBold))

        frameLayout.addStretch()

        return self
