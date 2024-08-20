#coding:utf-8

import sys
sys.path.append("..")

from PySide6.QtWidgets import QDialog, QHBoxLayout,\
    QFrame, QVBoxLayout, QLabel, QSizePolicy, QLineEdit
from PySide6.QtGui import QPixmap, QFont, QIcon 
from PySide6.QtCore import Qt, Slot

from GUI.Components.components import entryField, passwordEntryField,\
    connectionButton, bareButton, loginCheckbox, setBackgroundImage
from GUI.Components.widgets import displayMessageError
from Utils.enumeration import SIZE
from Utils.responsiveLayout import centerWindow, fitSizeToScreen, fitValueToScreen, fitWindowToScreen

from Utils.checkField import *


from Assets import icons, pictures

class LogInWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Connexion")
        self.setFixedSize(fitWindowToScreen(width=896, height=563))
        self.setWindowIcon(QIcon(":/Pictures/icon.png"))
        centerWindow(self)

        self.dataList = [''] * 2

        # ::::::::Design ui window::::::::::::: #

        self.mainLayout = QHBoxLayout()
        self.mainLayout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.mainLayout)

        self.leftFrame = QFrame(self)
        self.mainLayout.addWidget(self.leftFrame)
        self.leftFrame.setFixedSize(fitSizeToScreen(width=448, height=563))
        self.leftFrame.setFrameShape(QFrame.NoFrame)

        setBackgroundImage(widget=self.leftFrame, imagePath=':/Pictures/background_login.png')

        self.leftLayout = QVBoxLayout()
        self.leftFrame.setLayout(self.leftLayout)
        self.leftLayout.setAlignment(Qt.AlignCenter)

        self.leftLayout.addStretch(1)

        self.logoLayout = QHBoxLayout()
        self.leftLayout.addLayout(self.logoLayout)
        self.logo = QLabel(self.leftFrame)
        self.logo.setFixedSize(fitSizeToScreen(width=80, height=80))
        self.logo.setPixmap(QPixmap(":/Pictures/logo.png"))
        self.logo.setScaledContents(True)
        self.logo.setStyleSheet("QLabel { background: none; border: none;}")
        self.logo.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        
        self.logoLayout.addWidget(self.logo)

        self.firstText = QLabel(self.leftFrame)
        self.firstText.setText("Heureux")
        self.firstText.setFont(QFont("Montserrat", fitValueToScreen(value=20), QFont.Medium))
        self.firstText.setStyleSheet("QLabel { color: white; background: none; border: none;}")
        self.firstText.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.leftLayout.addWidget(self.firstText)
        self.leftLayout.setAlignment(self.firstText, Qt.AlignCenter)

        self.secondText = QLabel(self.leftFrame)
        self.secondText.setText("de vous revoir")
        self.secondText.setFont(QFont("Montserrat", fitValueToScreen(value=35), QFont.Bold))
        self.secondText.setStyleSheet("QLabel { color: white; background: none; border: none;}")
        self.secondText.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.leftLayout.addWidget(self.secondText)
        self.leftLayout.setAlignment(self.secondText, Qt.AlignCenter)
        self.leftLayout.addStretch(1)

        self.mainLayout.setSpacing(0)

        self.rightFrame = QFrame(self)
        self.mainLayout.addWidget(self.rightFrame)
        self.rightFrame.setFixedSize(fitSizeToScreen(width=448, height=563))
        self.rightFrame.setFrameShape(QFrame.NoFrame)
        self.rightFrame.setStyleSheet(f"background-color: white; padding-left: {fitValueToScreen(value=16)}px; padding-right: {fitValueToScreen(value=16)}px;")

        self.rightLayout = QVBoxLayout()
        self.rightFrame.setLayout(self.rightLayout)

        self.rightLayout.addStretch(3)

        self.titleLayout = QHBoxLayout()
        self.rightLayout.addLayout(self.titleLayout)
        
        self.title = QLabel(self.rightFrame)
        self.titleLayout.addWidget(self.title)
        self.title.setText("Connectez vous")
        self.title.setFont(QFont("Calibri", fitValueToScreen(value=20), QFont.Bold))
        self.title.setStyleSheet("QLabel { color: #5234A5; background: none; border: none;}")
        self.title.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        self.titleLayout.addStretch()

        self.rightLayout.addStretch(1)
        
        self.nameLayout = QHBoxLayout()
        self.rightLayout.addLayout(self.nameLayout)
        
        self.mail = entryField(parent=self.rightFrame, layout=self.nameLayout, icon=":/Icons/mail.svg", placehoder="Email ID", size=SIZE.Long, regex=r"^[a-zA-Z0-9!#$%&'*+/=?^_`{|}~.-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", maxLength=100)
        self.mail_lineEdit = self.mail.findChild(QLineEdit, "line_edit", Qt.FindDirectChildrenOnly)
        self.mail_lineEdit.textChanged.connect(lambda text : self.addToList(0, text))

        self.rightLayout.addStretch(1)

        self.passwordLayout = QHBoxLayout()
        self.rightLayout.addLayout(self.passwordLayout)

        self.password = passwordEntryField(parent=self.rightFrame, layout=self.passwordLayout, placehoder="Mot de passe")
        self.password_lineEdit = self.password.findChild(QLineEdit, "line_edit", Qt.FindDirectChildrenOnly)
        self.password_lineEdit.textChanged.connect(lambda text : self.addToList(1, text))

        self.rightLayout.addStretch(1)

        self.textLayout = QHBoxLayout()
        self.rightLayout.addLayout(self.textLayout)

        loginCheckbox(parent=self.rightFrame, layout=self.textLayout)

        self.textLayout.addStretch()

        bareButton(parent=self.rightFrame, layout=self.textLayout, text="Mot de passe oublié ?")

        self.rightLayout.addStretch(1)

        self.buttonLayout = QHBoxLayout()
        self.rightLayout.addLayout(self.buttonLayout)
        connectionButton(parent=self.rightFrame, layout=self.buttonLayout)

        self.rightLayout.addStretch(3)

        self.show()


    @Slot()
    def addToList(self, index: int, text: str):
        self.dataList[index] = text

    @Slot()
    def checkDataEntry(self):
        try:
            check_all_fields_filled(li=self.dataList)
            if self.dataList[0] or self.dataList[1] or self.dataList[2] or self.dataList[3] or self.dataList[4] or self.dataList[5] == "":
                raise DataEntryError("Veuillez remplir tous les champs")
            check_email_format(email=self.dataList[2])
            check_phone_format(number=self.dataList[3])
            check_password_complexity(password=self.dataList[4])
            check_password_differs_from_name(password=self.dataList[4], fName=self.dataList[1], lName=self.dataList[0])
            check_password_length(password=self.dataList[4])
            check_passwords_match(password=self.dataList[4], conf_pwd=self.dataList[5])
        except DataEntryError as e :
            displayMessageError(title=str(e.title), message=str(e.message))
        else:
            print("Tous les champs sont corrects")