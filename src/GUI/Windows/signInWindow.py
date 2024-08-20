#coding:utf-8

import sys
sys.path.append("..")

from PySide6.QtWidgets import QDialog, QHBoxLayout,\
    QFrame, QVBoxLayout, QLabel, QSizePolicy, QLineEdit
from PySide6.QtGui import QPixmap, QFont, QIcon
    
from PySide6.QtCore import Qt, Slot

from GUI.Components.components import entryField, passwordEntryField,\
    connectionButton, bareButton, setBackgroundImage
from GUI.Components.widgets import display_message_error
from Utils.enumeration import SIZE
from Utils.responsiveLayout import fitSizeToScreen, fitValueToScreen,\
    centerWindow, fitWindowToScreen
from Utils.checkField import *

from Assets import icons, pictures

class SignInWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Inscription")
        self.setFixedSize(fitWindowToScreen(width=896, height=563))
        self.setWindowIcon(QIcon(":/Pictures/icon.png"))
        centerWindow(self)

        self.dataList = [''] * 6

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

        self.text = QLabel(self.leftFrame)
        self.text.setText("Bienvenue")
        self.text.setFont(QFont("Montserrat", fitValueToScreen(value=35), QFont.Bold))
        self.text.setStyleSheet("QLabel { color: white; background: none; border: none;}")
        self.text.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.leftLayout.addWidget(self.text)
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
        self.title.setText("Créez votre compte")
        self.title.setFont(QFont("Calibri", fitValueToScreen(value=20), QFont.Bold))
        self.title.setStyleSheet("QLabel { color: #5234A5; background: none; border: none;}")
        self.title.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        self.titleLayout.addStretch()

        self.rightLayout.addStretch(2)
        
        self.nameLayout = QHBoxLayout()
        self.rightLayout.addLayout(self.nameLayout)
        
        self.lastName = entryField(parent=self.rightFrame, layout=self.nameLayout, icon=":/Icons/user.svg", placehoder="Nom", size=SIZE.Short, regex=r"^[a-zA-Z'-]*$", maxLength=15)
        self.lastName_lineEdit = self.lastName.findChild(QLineEdit, "line_edit", Qt.FindDirectChildrenOnly)
        self.lastName_lineEdit.textChanged.connect(lambda text : self.addToList(0, text))
    
        self.firstName = entryField(parent=self.rightFrame, layout=self.nameLayout, icon=":/Icons/user.svg", placehoder="Prénom", size=SIZE.Short, regex=r"^[a-zA-Z'-]*$", maxLength=25)
        self.firstName_lineEdit = self.firstName.findChild(QLineEdit, "line_edit", Qt.FindDirectChildrenOnly)
        self.firstName_lineEdit.textChanged.connect(lambda text : self.addToList(1, text))

        self.rightLayout.addStretch(1)

        self.coordinateLayout = QHBoxLayout()
        self.rightLayout.addLayout(self.coordinateLayout)
        
        self.mail = entryField(parent=self.rightFrame, layout=self.coordinateLayout, icon=":/Icons/mail.svg", placehoder="Adresse mail", size=SIZE.Short, regex=r"^[a-zA-Z0-9!#$%&'*+/=?^_`{|}~.-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", maxLength=100)
        self.mail_lineEdit = self.mail.findChild(QLineEdit, "line_edit", Qt.FindDirectChildrenOnly)
        self.mail_lineEdit.textChanged.connect(lambda text : self.addToList(2, text))

        self.phone = entryField(parent=self.rightFrame, layout=self.coordinateLayout, icon=":/Icons/phone.svg", placehoder="Téléphone", size=SIZE.Short, regex=r"^\+?[0-9]{1,20}$", maxLength=30)
        self.phone_lineEdit = self.phone.findChild(QLineEdit, "line_edit", Qt.FindDirectChildrenOnly)
        self.phone_lineEdit.textChanged.connect(lambda text : self.addToList(3, text))

        self.rightLayout.addStretch(1)

        self.firstpasswordLayout = QHBoxLayout()
        self.rightLayout.addLayout(self.firstpasswordLayout)

        self.password = passwordEntryField(parent=self.rightFrame, layout=self.firstpasswordLayout, placehoder="Créer un mot de passe")
        self.password_lineEdit = self.password.findChild(QLineEdit, "line_edit", Qt.FindDirectChildrenOnly)
        self.password_lineEdit.textChanged.connect(lambda text : self.addToList(4, text))

        self.rightLayout.addStretch(1)

        self.secondpasswordLayout = QHBoxLayout()
        self.rightLayout.addLayout(self.secondpasswordLayout)

        self.confirmPassword = passwordEntryField(parent=self.rightFrame, layout=self.secondpasswordLayout, placehoder="Confirmez votre mot de passe")
        self.confirmPassword_lineEdit = self.confirmPassword.findChild(QLineEdit, "line_edit", Qt.FindDirectChildrenOnly)
        self.confirmPassword_lineEdit.textChanged.connect(lambda text : self.addToList(5, text))

        self.rightLayout.addStretch(1)

        self.buttonLayout = QHBoxLayout()
        self.rightLayout.addLayout(self.buttonLayout)
        self.button = connectionButton(parent=self.rightFrame, layout=self.buttonLayout)
        self.button.clicked.connect(self.checkDataEntry)

        self.rightLayout.addStretch(1)

        self.textLayout = QHBoxLayout()
        self.rightLayout.addLayout(self.textLayout)

        self.text = QLabel(self.rightFrame)
        self.textLayout.addWidget(self.text)
        self.text.setText("Vous avez déjà un compte ?")
        self.text.setStyleSheet("background-color: none; color: black; border: none;")
        self.text.setFont(QFont("Montserrat", fitValueToScreen(value=10), QFont.Normal))
        self.text.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        self.textButton = bareButton(parent=self.rightFrame, layout=self.textLayout, text="Connectez-vous")

        self.textLayout.addStretch()

        self.rightLayout.addStretch(1)


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
            display_message_error(title=str(e.title), message=str(e.message))
        else:
            print("Tous les champs sont corrects")

