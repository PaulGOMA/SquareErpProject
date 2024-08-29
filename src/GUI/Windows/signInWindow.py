#coding:utf-8

import sys
sys.path.append("..")

from PySide6.QtWidgets import QDialog, QHBoxLayout,\
    QFrame, QVBoxLayout, QLabel, QSizePolicy, QMessageBox
from PySide6.QtGui import QPixmap, QFont, QIcon
    
from PySide6.QtCore import Qt, Slot

from GUI.Components.components import entryField, setBackgroundImage,\
    StandardButton
from GUI.Components.widgets import PopUp
from Utils.enumeration import SIZE, ERROR_TITLE
from Utils.responsiveLayout import fitSizeToScreen, fitValueToScreen,\
    centerWindow, fitWindowToScreen
from Utils.checkField import *
from Utils.errors import error
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

        self.firstentryname = entryField(parent=self.rightFrame, Layout=self.nameLayout)
        
        self.lastName = self.firstentryname.entryname(True)
        self.lastName.lineEdit.textChanged.connect(lambda text : self.addToList(0, text))
    
        self.secondentryname = entryField(parent=self.rightFrame, Layout=self.nameLayout)

        self.firstName = self.secondentryname.entryname(False)
        self.firstName.lineEdit.textChanged.connect(lambda text : self.addToList(1, text))

        self.rightLayout.addStretch(1)

        self.coordinateLayout = QHBoxLayout()
        self.rightLayout.addLayout(self.coordinateLayout)

        self.mailentryfield = entryField(parent=self.rightFrame, Layout=self.coordinateLayout)
        
        self.mail = self.mailentryfield.entrymail(SIZE.Short)
        self.mail.lineEdit.textChanged.connect(lambda text : self.addToList(2, text))

        self.phoneentryfield = entryField(parent=self.rightFrame, Layout=self.coordinateLayout)

        self.phone = self.phoneentryfield.entrynumber()
        self.phone.lineEdit.textChanged.connect(lambda text : self.addToList(3, text))

        self.rightLayout.addStretch(1)

        self.firstpasswordLayout = QHBoxLayout()
        self.rightLayout.addLayout(self.firstpasswordLayout)

        self.firstpassword = entryField(parent=self.rightFrame, Layout=self.firstpasswordLayout)

        self.password = self.firstpassword.entrypassword(False)
        self.password.lineEdit.textChanged.connect(lambda text : self.addToList(4, text))

        self.rightLayout.addStretch(1)

        self.secondpasswordLayout = QHBoxLayout()
        self.rightLayout.addLayout(self.secondpasswordLayout)

        self.secondpassword = entryField(parent=self.rightFrame, Layout=self.secondpasswordLayout)

        self.confirmPassword = self.secondpassword.entrypassword(True)
        self.confirmPassword.lineEdit.textChanged.connect(lambda text : self.addToList(5, text))

        self.rightLayout.addStretch(1)

        self.buttonLayout = QHBoxLayout()
        self.rightLayout.addLayout(self.buttonLayout)
        self.button = StandardButton(parent=self.rightFrame, Layout=self.buttonLayout, Width=346, Height=38).connectionButton()
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

        self.textButton = StandardButton(parent=self.rightFrame, Layout=self.textLayout).bareButton("Connectez-vous")

        self.textLayout.addStretch()

        self.rightLayout.addStretch(1)


        self.show()


    @Slot()
    def addToList(self, index: int, text: str):
        self.dataList[index] = text



