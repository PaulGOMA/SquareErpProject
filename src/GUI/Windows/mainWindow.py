import sys
sys.path.append("..")

from PySide6.QtWidgets import QMainWindow, QWidget, QHBoxLayout,\
    QVBoxLayout, QAbstractButton, QSizePolicy
from PySide6.QtCore import Qt, Slot, QPoint

from Utils.responsiveLayout import centerWindow
from Utils.enumeration import CONNEXION_STATUS as STATUS
from Utils.worker import WorkerWithConnexionStatus, WorkerWithString
from GUI.Components.widgets import Sidebar, TitleBar, Statusbar
from GUI.Pages.pageManager import PagerManager
from Handler.internet import InternetManager
from Handler.threads import ThreadManager
from Handler.users import UserManager
from Assets import pictures


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.oldPos = None
        self.resizing = False

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

        self.sidebar = Sidebar(parent=self.centralArea, Layout=self.rootLayout)
        self.rootLayout.setAlignment(self.sidebar, Qt.AlignLeft)
        self.sidebar.dashboard.setChecked(True)

        self.mainLayout = QVBoxLayout()
        self.rootLayout.addLayout(self.mainLayout)
        self.mainLayout.setContentsMargins(0, 0, 0, 0)
        self.mainLayout.setSpacing(0)

        self.titleBar = TitleBar(parent=self.centralArea, Layout=self.mainLayout) 
        self.titleBar.notification.clicked.connect(self.switchToMessagePage)


        self.pages = PagerManager(self.mainLayout)
        self.pages.setCurrentIndex(0)

        self.groupbutton = self.sidebar.groupbutton
        self.groupbutton.buttonClicked.connect(self.displayPage)

        self.statusbar = Statusbar()
        self.setStatusBar(self.statusbar)

        self.WorkerIconConnection = WorkerWithConnexionStatus(Target=self.getConnexionState)
        self.WorkerIconConnection.updatePageSignal.connect(self.statusbar.setInternetConnection) 
        self.ThreadManager.addThread(target=self.WorkerIconConnection.run, label="internetConnection", useStopevent=True)
        self.ThreadManager.startThreadByLabel(label="internetConnection")

        self.WorkerDatabaseConnection = WorkerWithConnexionStatus(Target=UserManager.checkDatabaseConnection)
        self.WorkerDatabaseConnection.updatePageSignal.connect(self.statusbar.setDatabaseConnection) 
        self.ThreadManager.addThread(target=self.WorkerDatabaseConnection.run, label="databaseConnection", useStopevent=True)
        self.ThreadManager.startThreadByLabel(label="databaseConnection")        

        self.WorkerIconNotification = WorkerWithConnexionStatus(Target=UserManager.getMessageNotify)
        self.WorkerIconNotification.updatePageSignal.connect(self.titleBar.setNotification) 
        self.ThreadManager.addThread(target=self.WorkerIconNotification.run, label="notification", useStopevent=True)
        self.ThreadManager.startThreadByLabel(label="notification")

        self.WorkerUsername = WorkerWithString(Target=UserManager.getUsername)
        self.WorkerUsername.updatePageSignal.connect(self.setUsername)
        self.ThreadManager.addThread(target=self.WorkerUsername.run, label="Username", useStopevent=True)
        self.ThreadManager.startThreadByLabel(label="Username")

        self.showMaximized()

    def switchToMessagePage(self):
        self.pages.setCurrentIndex(5)
        self.sidebar.message.setChecked(True)


    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.oldPos = event.position().toPoint()
            if self.isOnEdge(event.position().toPoint()):
                self.resizing = True

    def mouseMoveEvent(self, event):
        if not self.oldPos:
            return
        if self.resizing:
            self.resizeWindow(event)
        else:
            delta = QPoint(event.position().toPoint() - self.oldPos)
            self.move(self.pos() + delta)

    def mouseReleaseEvent(self, event):
        self.oldPos = None
        self.resizing = False

    def isOnEdge(self, pos):
        margin = 10
        rect = self.rect()
        return pos.x() < margin or pos.x() > rect.width() - margin or pos.y() < margin or pos.y() > rect.height() - margin
    
    def resizeWindow(self, event):
        delta = event.position().toPoint() - self.oldPos
        new_width = self.width() + delta.x()
        new_height = self.height() + delta.y()
        self.setFixedSize(new_width, new_height)
        self.oldPos = event.position().toPoint()

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
        if sender.checkedId() != 7:
            self.pages.setCurrentIndex(sender.checkedId())





