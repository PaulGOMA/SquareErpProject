#coding:utf-8

import sys
sys.path.append("..")

from PySide6.QtWidgets import QDialog, QApplication, QHBoxLayout,\
    QFrame, QVBoxLayout, QLabel, QSizePolicy
from PySide6.QtGui import QPixmap, QFont 
from PySide6.QtCore import Qt

from GUI.Screens.resolution import centerWindow
from GUI.Components.components import shortEntryField, passwordEntryField,\
    connectionButton, bareButton
from Utils.enumeration import SIZE

from Assets import icons, pictures

class SignInScreen(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("SQUARE erp - page d'inscription")
        self.setFixedSize(896, 563)
        centerWindow(self)

        # ::::::::Design ui window::::::::::::: #

        self.mainLayout = QHBoxLayout()
        self.mainLayout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.mainLayout)

        self.leftFrame = QFrame(self)
        self.mainLayout.addWidget(self.leftFrame)
        self.leftFrame.setFixedSize(448, 563)
        self.leftFrame.setFrameShape(QFrame.NoFrame)
        self.leftFrame.setStyleSheet("background-image: url(':/Pictures/background_login.png');")
        
        self.leftLayout = QVBoxLayout()
        self.leftFrame.setLayout(self.leftLayout)
        self.leftLayout.setAlignment(Qt.AlignCenter)

        self.leftLayout.addStretch(1)

        self.logoLayout = QHBoxLayout()
        self.leftLayout.addLayout(self.logoLayout)
        self.logo = QLabel(self.leftFrame)
        self.logo.setFixedSize(80, 80)
        self.logo.setPixmap(QPixmap(":/Pictures/logo.png"))
        self.logo.setScaledContents(True)
        self.logo.setStyleSheet("QLabel { background: none; border: none;}")
        self.logo.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        
        self.logoLayout.addWidget(self.logo)

        self.text = QLabel(self.leftFrame)
        self.text.setText("Bienvenue")
        self.text.setFont(QFont("Montserrat", 40, QFont.Bold))
        self.text.setStyleSheet("QLabel { color: white; background: none; border: none;}")
        self.text.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.leftLayout.addWidget(self.text)
        self.leftLayout.addStretch(1)

        self.mainLayout.setSpacing(0)

        self.rightFrame = QFrame(self)
        self.mainLayout.addWidget(self.rightFrame)
        self.rightFrame.setFixedSize(448, 563)
        self.rightFrame.setFrameShape(QFrame.NoFrame)
        self.rightFrame.setStyleSheet("background-color: white; padding-left: 16px; padding-right: 16px;")

        self.rightLayout = QVBoxLayout()
        self.rightFrame.setLayout(self.rightLayout)

        self.rightLayout.addStretch(3)

        self.titleLayout = QHBoxLayout()
        self.rightLayout.addLayout(self.titleLayout)
        
        self.title = QLabel(self.rightFrame)
        self.titleLayout.addWidget(self.title)
        self.title.setText("Créez votre compte")
        self.title.setFont(QFont("Calibri", 20, QFont.Bold))
        self.title.setStyleSheet("QLabel { color: #5234A5; background: none; border: none;}")
        self.title.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        self.titleLayout.addStretch()

        self.rightLayout.addStretch(2)
        
        self.nameLayout = QHBoxLayout()
        self.rightLayout.addLayout(self.nameLayout)
        
        shortEntryField(parent=self.rightFrame, layout=self.nameLayout, icon=":/Icons/user.svg", placehoder="Nom", size=SIZE.Short)
        shortEntryField(parent=self.rightFrame, layout=self.nameLayout, icon=":/Icons/user.svg", placehoder="Prénom", size=SIZE.Short)

        self.rightLayout.addStretch(1)

        self.coordinateLayout = QHBoxLayout()
        self.rightLayout.addLayout(self.coordinateLayout)
        
        shortEntryField(parent=self.rightFrame, layout=self.coordinateLayout, icon=":/Icons/mail.svg", placehoder="Adresse mail", size=SIZE.Short)
        shortEntryField(parent=self.rightFrame, layout=self.coordinateLayout, icon=":/Icons/phone.svg", placehoder="Téléphone", size=SIZE.Short)

        self.rightLayout.addStretch(1)

        self.firstpasswordLayout = QHBoxLayout()
        self.rightLayout.addLayout(self.firstpasswordLayout)

        passwordEntryField(parent=self.rightFrame, layout=self.firstpasswordLayout, placehoder="Créer un mot de passe")

        self.rightLayout.addStretch(1)

        self.secondpasswordLayout = QHBoxLayout()
        self.rightLayout.addLayout(self.secondpasswordLayout)
        passwordEntryField(parent=self.rightFrame, layout=self.secondpasswordLayout, placehoder="Confirmez votre mot de passe")

        self.rightLayout.addStretch(1)

        self.buttonLayout = QHBoxLayout()
        self.rightLayout.addLayout(self.buttonLayout)
        connectionButton(parent=self.rightFrame, layout=self.buttonLayout)

        self.rightLayout.addStretch(1)

        self.textLayout = QHBoxLayout()
        self.rightLayout.addLayout(self.textLayout)

        self.text = QLabel(self.rightFrame)
        self.textLayout.addWidget(self.text)
        self.text.setText("Vous avez déjà un compte ?")
        self.text.setStyleSheet("background-color: none; color: black; border: none;")
        self.text.setFont(QFont("Montserrat", 10, QFont.Normal))
        self.text.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        bareButton(parent=self.rightFrame, layout=self.textLayout, text="Connectez-vous")

        self.textLayout.addStretch()

        self.rightLayout.addStretch(1)

        self.show()


# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     w = SignInScreen()
#     w.show()
#     sys.exit(app.exec())