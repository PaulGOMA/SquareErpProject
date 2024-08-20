import sys
sys.path.append("..")

from PySide6.QtWidgets import QMainWindow, QWidget, QHBoxLayout,\
    QVBoxLayout, QButtonGroup, QAbstractButton,\
    QPushButton, QSizePolicy
from PySide6.QtCore import Qt, Slot

from Utils.responsiveLayout import centerWindow, getResolutions
from Utils.enumeration import CONNEXION_STATUS as STATUS
from GUI.Components.widgets import sidebar, titlebar, closeApp
from GUI.Pages.pageManager import stackPage
from Assets import pictures


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        centerWindow(self)

        self.centralArea = QWidget()
        self.setCentralWidget(self.centralArea)
        self.centralArea.setStyleSheet("background-color: #f6f6f6")

        self.rootLayout = QHBoxLayout()
        self.centralArea.setLayout(self.rootLayout)
        self.rootLayout.setContentsMargins(0, 0, 0, 0)
        self.rootLayout.setSpacing(0)

        self.sidebar = sidebar(parent=self.centralArea, layout=self.rootLayout)
        self.rootLayout.setAlignment(self.sidebar, Qt.AlignLeft)

        self.mainLayout = QVBoxLayout()
        self.rootLayout.addLayout(self.mainLayout)
        self.mainLayout.setContentsMargins(0, 0, 0, 0)
        self.mainLayout.setSpacing(0)

        self.titlebar = titlebar(parent=self.centralArea, layout=self.mainLayout, connexionstatus=STATUS.OffLine, name="Paul GOMA", mail="paulgoma07@gmail.com")
        self.mainLayout.setAlignment(self.titlebar, Qt.AlignTop)

        self.closeButton = self.titlebar.findChild(QPushButton, "closeButton", Qt.FindDirectChildrenOnly)
        self.closeButton.clicked.connect(self.closeApp)

        self.hideScreen = self.titlebar.findChild(QPushButton, "minimizeButton", Qt.FindDirectChildrenOnly)
        self.hideScreen.clicked.connect(self.showMinimized)

        self.resizeButton = self.titlebar.findChild(QPushButton, "resizeButton", Qt.FindDirectChildrenOnly)
        self.resizeButton.toggled.connect(self.resizeWindow)

        self.pages = stackPage(layout=self.mainLayout)
        self.pages.setCurrentIndex(0)

        self.groupbutton = self.sidebar.findChild(QButtonGroup, "groupbutton", Qt.FindDirectChildrenOnly)
        self.groupbutton.buttonClicked.connect(self.displayPage)

        self.show()


    @Slot()
    def displayPage(self, button: QAbstractButton):
        sender = self.sender()
        print(sender.checkedId())
        if sender.checkedId() != 7:
            self.pages.setCurrentIndex(sender.checkedId())
        else:
            print("sortie de l'application")

    @Slot()
    def closeApp(self):
        dialog = closeApp()
        if dialog.exec():
            self.close()

    @Slot()
    def resizeWindow(self, checked: bool):
        if checked:
            self.showNormal()
        else:
            self.showMaximized()    



