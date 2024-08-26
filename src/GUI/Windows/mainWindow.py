import sys
sys.path.append("..")

from PySide6.QtWidgets import QMainWindow, QWidget, QHBoxLayout,\
    QVBoxLayout, QButtonGroup, QAbstractButton,\
    QPushButton, QSizePolicy, QLabel
from PySide6.QtCore import Qt, Slot

from Utils.responsiveLayout import centerWindow
from Utils.enumeration import CONNEXION_STATUS as STATUS
from Utils.worker import WorkerWithConnexionStatus, WorkerWithString
from GUI.Components.widgets import sidebar, closeApp, TitleBar
from GUI.Pages.pageManager import stackPage
from Handler.internet import InternetManager
from Handler.threads import ThreadManager
from Handler.users import UserManager
from Assets import pictures


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.InternetManager = InternetManager()
        self.ThreadManager = ThreadManager()


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

        self.titleBar = TitleBar(parent=self.centralArea, Layout=self.mainLayout)

        self.WorkerIconConnection = WorkerWithConnexionStatus(Target=self.getConnexionState)
        self.WorkerIconConnection.updatePageSignal.connect(self.titleBar.attendanceStatus) 
        self.ThreadManager.addThread(target=self.WorkerIconConnection.run, label="internetConnection", useStopevent=True)
        self.ThreadManager.startThreadByLabel(label="internetConnection")

        self.WorkerUsername = WorkerWithString(Target=UserManager.getUsername)
        self.WorkerUsername.updatePageSignal.connect(self.setUsername)
        self.ThreadManager.addThread(target=self.WorkerUsername.run, label="Username", useStopevent=True)
        self.ThreadManager.startThreadByLabel(label="Username")
        
        self.hideButton = self.titleBar.hideButton
        self.hideButton.clicked.connect(self.showMinimized)
        self.titleBar.resizeButton.toggled.connect(self.resizeWindow)
        self.titleBar.closeButton.clicked.connect(self.closeApp)

        self.pages = stackPage(layout=self.mainLayout)
        self.pages.setCurrentIndex(0)

        self.groupbutton = self.sidebar.findChild(QButtonGroup, "groupbutton", Qt.FindDirectChildrenOnly)
        self.groupbutton.buttonClicked.connect(self.displayPage)

        self.show()

    @Slot()
    def getConnexionState(self) -> STATUS:
        if self.InternetManager.isInternetAcces() and self.InternetManager.isWifiConnected():
            return STATUS.OnLine
        else:
            return STATUS.OffLine
        
    
    @Slot()
    def setUsername(self) -> None:
        self.titleBar.name = UserManager.email

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



