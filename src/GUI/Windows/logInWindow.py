#coding:utf-8

import sys
sys.path.append("..")

from PySide6.QtWidgets import QDialog, QHBoxLayout,\
    QFrame, QVBoxLayout, QLabel, QSizePolicy, QMessageBox
from PySide6.QtGui import QPixmap, QFont, QIcon 
from PySide6.QtCore import Qt, Slot

from GUI.Components.components import entryField, StandardButton, \
    loginCheckbox, setBackgroundImage
from GUI.Components.widgets import PopUp
from Utils.enumeration import SIZE, ERROR_TITLE
from Utils.responsiveLayout import centerWindow, \
    fitSizeToScreen, fitValueToScreen, fitWindowToScreen
from Utils.errors import error
from Utils.checkField import *


from Assets import pictures

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

        self.entrymail = entryField(parent=self.rightFrame, Layout=self.nameLayout)
        
        self.mail = self.entrymail.entrymail(SIZE.Long)
        self.mail.lineEdit.textChanged.connect(lambda text : self.addToList(0, text))

        self.rightLayout.addStretch(1)

        self.passwordLayout = QHBoxLayout()
        self.rightLayout.addLayout(self.passwordLayout)

        self.entrypassword = entryField(parent=self.rightFrame, Layout=self.passwordLayout)

        self.password = self.entrypassword.entrypassword(False)
        self.password.lineEdit.textChanged.connect(lambda text : self.addToList(1, text))

        self.rightLayout.addStretch(1)

        self.textLayout = QHBoxLayout()
        self.rightLayout.addLayout(self.textLayout)

        self.checkbox = loginCheckbox(parent=self.rightFrame, layout=self.textLayout)

        self.textLayout.addStretch()

        self.barebutton = StandardButton(parent=self.rightFrame, Layout=self.textLayout).bareButton("Mot de passe oublié ?")

        self.rightLayout.addStretch(1)

        self.buttonLayout = QHBoxLayout()
        self.rightLayout.addLayout(self.buttonLayout)
        self.button = StandardButton(parent=self.rightFrame, Layout=self.buttonLayout, Width=346, Height=38).connectionButton()

        self.rightLayout.addStretch(3)

        self.show()


    @Slot()
    def addToList(self, index: int, text: str):
        self.dataList[index] = text
