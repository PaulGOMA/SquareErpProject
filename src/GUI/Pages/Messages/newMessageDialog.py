import sys
sys.path.append("..")

from PySide6.QtCore import Qt, Slot
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QDialog, QVBoxLayout, QFrame, QHBoxLayout,\
    QLabel, QSizePolicy, QStyle, QScrollArea, QBoxLayout, QPushButton

from GUI.Pages.Messages.contact import Contact
from GUI.Components.components import TitleBarButton, combobox
from GUI.Components.widgets import MessageInputField, closeSession
from Utils.enumeration import CLOSING_SESSION_INFORMATION as SESSION
from Utils.responsiveLayout import centerWindow, fitValueToScreen, fitSizeToScreen

class NewMessage(QDialog):

    def __init__(self):
        super().__init__()

        self.setFixedWidth(fitSizeToScreen(width=596, height=None))
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.setStyleSheet("background-color: white;")
        centerWindow(self)

        self.frameLayout = QVBoxLayout()
        self.frameLayout.setContentsMargins(0, 0, 0, 0)
        self.frameLayout.setAlignment(Qt.AlignLeft)
        self.setLayout(self.frameLayout)

        header = QFrame(self)
        header.setFrameShape(QFrame.NoFrame)
        header.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        header.setStyleSheet(f"background-color: transparent; border: {fitValueToScreen(value=1)}px solid #DCDCDC")
        self.frameLayout.addWidget(header)
        self.frameLayout.setAlignment(header, Qt.AlignTop)

        headerLayout = QHBoxLayout()
        headerLayout.setContentsMargins(fitValueToScreen(value=16), 0, 0, 0)
        header.setLayout(headerLayout)

        title = QLabel("Nouveau message", header)
        title.setFont(QFont("Montserrat", fitValueToScreen(value=11), QFont.DemiBold))
        title.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        title.setStyleSheet("background-color: none; border: none; color: #5234A5")
        headerLayout.addWidget(title)

        headerLayout.addStretch()

        self.closeButton = TitleBarButton(header, headerLayout, True)
        self.closeButton.setFixedSize(fitSizeToScreen(width=30, height=30))
        self.closeButton.setIcon(self.style().standardIcon(QStyle.SP_TitleBarCloseButton))
        self.closeButton.clicked.connect(self.closeApp)
        headerLayout.addWidget(self.closeButton)

        self.frameLayout.addStretch(1)

        contactArea = QVBoxLayout()
        contactArea.setContentsMargins(fitValueToScreen(value=16), fitValueToScreen(value=16), fitValueToScreen(value=16), fitValueToScreen(value=16))
        contactArea.setSpacing(fitValueToScreen(value=16))
        contactArea.setAlignment(Qt.AlignLeft)
        self.frameLayout.addLayout(contactArea)

        contactLabel = QLabel("Selectionner un contact", self)
        contactLabel.setFont(QFont("Montserrat", fitValueToScreen(value=12), QFont.DemiBold))
        contactLabel.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        contactLabel.setStyleSheet(f"background-color: none; border: none; color: #3D3D3D;")
        contactArea.addWidget(contactLabel)

        self.contactFrame = QFrame(self)
        self.contactFrame.setStyleSheet("background-color: white; border: none;")
        self.contactFrame.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.contactLayout = QHBoxLayout()
        self.contactLayout.setDirection(QBoxLayout.LeftToRight)
        self.contactFrame.setLayout(self.contactLayout)

        self.scrollArea = QScrollArea()
        self.scrollArea.setWidget(self.contactFrame)
        self.scrollArea.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setStyleSheet(f"background-color: transparent; border: none;")
        contactArea.addWidget(self.scrollArea)

        if self.contactLayout.count() == 0:
            self.scrollArea.setHidden(True)
        else:
            self.scrollArea.setHidden(False)

        li = []

        self.combo = combobox(self, contactArea, li)

        self.frameLayout.addStretch(1)

        self.messageBox = MessageInputField(self, self.frameLayout)

        self.show()

    @Slot()
    def closeApp(self):
        dialog = closeSession(SESSION.MessageBox)
        if dialog.exec():
            self.close()






