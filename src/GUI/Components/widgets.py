"""
    # This file contains all main headers and bars used commonly in the application
"""

import sys
sys.path.append("..")

import os


from PySide6.QtWidgets import QFrame, QWidget, QBoxLayout,\
    QSizePolicy, QHBoxLayout, QLabel, QVBoxLayout, QButtonGroup,\
    QMessageBox, QStyle, QStatusBar, QPushButton, QTextEdit, QScrollArea,\
    QFileDialog
from PySide6.QtGui import QFont, QPalette, QColor, QPixmap, QIcon,\
    QTextCharFormat
from PySide6.QtCore import Qt, Slot

from GUI.Components.components import StandardButton,\
    separator, SearchBar,attendanceStatus, user,\
    TitleBarButton, GroupButton,\
    ToolbarButtonForMessage, DisplayFile
from Utils.enumeration import CONNEXION_STATUS as STATUS, SIZE, ERROR_TITLE,\
    MESSAGE_FILE_TYPE as TYPE, CLOSING_SESSION_INFORMATION as SESSION
from Utils.responsiveLayout import fitValueToScreen, fitSizeToScreen
from Utils.errors import error


from Assets import icons, pictures

# ::::::::BAR::::::::::::: #

class Header(QFrame):
    """
    # This class implements standard header used in the application.

    ## Class attribute

    ( *color* ) backgroundColor : *str*
    ( *color* ) textColor : *str*
    
    ## Methods

    ####  Header(parent: QWidget, Layout: QBoxLayout, text: str) -> QFrame

    *Constructs an header with the given parent, layout and text*

    #### headerWithButton(textButton: str=None) -> QFrame

    *Constructs an header whith a button*

    #### headerforDialogBox(self) -> QFrame

    *Constructs a dialog box header*
    """

    #Class attribute
    backgroundColor = "white"
    textColor = "#5234a5"
    secondTextColor = "#989898"
    borderColor = "#DCDCDC"
    ButtonColor = "#E81123"

    def __init__(self, parent: QWidget, Layout: QBoxLayout, text: str):
        super().__init__(parent)

        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.setStyleSheet(f"background-color: {Header.backgroundColor};")

        self.frameLayout = QHBoxLayout()
        self.setLayout(self.frameLayout)
        self.frameLayout.setContentsMargins(fitValueToScreen(12), fitValueToScreen(12), fitValueToScreen(12), fitValueToScreen(12))  

        self.title = QLabel(self)
        self.title.setText(text)
        self.title.setFont(QFont("Montserrat", fitValueToScreen(14), QFont.DemiBold))
        palette = self.title.palette()
        palette.setColor(QPalette.WindowText, QColor(Header.textColor))
        self.title.setPalette(palette)
        self.frameLayout.addWidget(self.title)  

        self.frameLayout.addStretch()   

        Layout.addWidget(self)

    def headerWithButton(self, textButton: str=None) -> QFrame:
        self.frameLayout.addStretch() 
        self.button = StandardButton(self, self.frameLayout).ButtonWithText(textButton)

        return self
    
    def headerforDialogBox(self) -> QFrame:
        self.setStyleSheet(f"background-color: {Header.backgroundColor}; border-bottom: {fitValueToScreen(value=1)}px solid {Header.borderColor}")
        self.frameLayout.setContentsMargins(fitValueToScreen(12), 0, 0, 0)
        self.frameLayout.addStretch()

        self.button = QPushButton(self)
        self.button.setFlat(True)
        self.button.setFixedSize(fitSizeToScreen(width=30, height=30))
        self.button.setIcon(self.style().standardIcon(QStyle.SP_TitleBarCloseButton))
        self.button.setStyleSheet(
            f"""
            QPushButton {{background-color: none; border: none;}}
            QPushButton:hover {{background-color: {Header.ButtonColor}; border: none;}}
            """
        )

        return self


class Sidebar(QFrame):
    """
    # This class is used to create the application's side bar
    """

    # Class attribute
    backgroundColor = "#5234A5"
    separatorColor = "white"

    def __init__(self, parent: QWidget, Layout: QBoxLayout):
        super().__init__(parent)

        self.setFixedWidth(fitSizeToScreen(width=186, height=None))
        self.setStyleSheet(f"background-color: {Sidebar.backgroundColor};")
        self.setFrameShape(QFrame.NoFrame)
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)

        self.frameLayout = QVBoxLayout()
        self.setLayout(self.frameLayout)
        self.frameLayout.setContentsMargins(0, fitValueToScreen(24), 0, 0)
        self.frameLayout.setSpacing(0)

        self.logo = QLabel(self)
        self.logo.setPixmap(QPixmap(":/Pictures/full_logo.png"))
        self.logo.setScaledContents(True)
        self.logo.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.logo.setFixedSize(fitSizeToScreen(width=140, height=50))
        self.frameLayout.addWidget(self.logo)
        self.frameLayout.setAlignment(self.logo, Qt.AlignHCenter) 

        self.groupbutton = QButtonGroup(self)
        self.groupbutton.setObjectName("groupbutton")
        self.groupbutton.setExclusive(True)

        self.frameLayout.addStretch(3)

        self.dashboard = GroupButton(self, "Dashboard", self.frameLayout, self.groupbutton, 0).sidebarButton(uncheckedIconPath=":/Icons/unchecked_dashboard.svg", checkedIconPath=":/Icons/checked_dashboard.svg")
        self.report = GroupButton(self, "Rapport", self.frameLayout, self.groupbutton, 1).sidebarButton(uncheckedIconPath=":/Icons/unchecked_reporting.svg", checkedIconPath=":/Icons/checked_reporting.svg")
        self.tracking = GroupButton(self, "Suivi", self.frameLayout, self.groupbutton, 2).sidebarButton(uncheckedIconPath=":/Icons/unchecked_collection.svg", checkedIconPath=":/Icons/checked_collection.svg")
        self.location = GroupButton(self, "Site", self.frameLayout, self.groupbutton, 3).sidebarButton(uncheckedIconPath=":/Icons/unchecked_map.svg", checkedIconPath=":/Icons/checked_map.svg")
        self.graph = GroupButton(self, "Analyse", self.frameLayout, self.groupbutton, 4).sidebarButton(uncheckedIconPath=":/Icons/unchecked_tracking.svg", checkedIconPath=":/Icons/checked_tracking.svg")

        self.frameLayout.addStretch(4)

        separator(self.frameLayout, Sidebar.separatorColor)

        self.message = GroupButton(self, "Message", self.frameLayout, self.groupbutton, 5).sidebarButton(uncheckedIconPath=":/Icons/unchecked_message.svg", checkedIconPath=":/Icons/checked_message.svg")
        self.admin = GroupButton(self, "Administration", self.frameLayout, self.groupbutton, 6).sidebarButton(uncheckedIconPath=":/Icons/unchecked_admin.svg", checkedIconPath=":/Icons/checked_admin.svg")
        self.logOut = GroupButton(self, "Déconnexion", self.frameLayout, self.groupbutton, 7).sidebarButton(uncheckedIconPath=":/Icons/unchecked_logout.svg", checkedIconPath=":/Icons/checked_logout.svg")

        self.frameLayout.addStretch(2)

        Layout.addWidget(self)


class TitleBar(QFrame):
    """
    # This class is used to create the application's title bar
    """

    # Class attribute
    background = "white"
    

    def __init__(self, parent: QWidget, Layout: QBoxLayout):
        super().__init__(parent)

        self.name = "Paul Goma"
        self.mail = "Paulgoma07@gmail.com"
        

        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.setFrameShape(QFrame.NoFrame)
        self.setStyleSheet(f"background-color: {TitleBar.background};")

        self.frameLayout = QHBoxLayout()
        self.frameLayout.setContentsMargins(fitValueToScreen(32), 0, 0, 0) 
        self.setLayout(self.frameLayout)

        self.searchbar = SearchBar(self, self.frameLayout).searchbarForTitleBar()

        self.frameLayout.addStretch(12)

        self.notification = TitleBarButton(self, self.frameLayout)
        self.notification.setIconSize(fitSizeToScreen(25, 29))
        self.notification.setIcon(QIcon(":/Icons/not_notified_icon.svg"))

        self.frameLayout.addStretch(1)

        self.status = attendanceStatus(self, self.frameLayout)
        self.frameLayout.addStretch(1)
        self.user = user(self, self.frameLayout, self.name, self.mail)
        self.frameLayout.addStretch(1)

        self.hideButton  = TitleBarButton(self, self.frameLayout)
        self.hideButton.setIcon(self.style().standardIcon(QStyle.SP_TitleBarMinButton))
        self.hideButton.clicked.connect(parent.parent().showMinimized)
        self.resizeButton  = TitleBarButton(self, self.frameLayout)
        self.resizeButton.setIcon(self.style().standardIcon(QStyle.SP_TitleBarMaxButton))
        self.resizeButton.clicked.connect(self.resizeWindow)
        self.closeButton  = TitleBarButton(self, self.frameLayout, True)
        self.closeButton.setIcon(self.style().standardIcon(QStyle.SP_TitleBarCloseButton))
        self.closeButton.clicked.connect(self.closeApp)

        self.Layout = Layout
        self.Layout.addWidget(self)
    
    @Slot()
    def setNotification(self, number: int):
        if number == 0:
            self.notification.setIcon(QIcon(":/Icons/not_notified_icon.svg"))
        elif number > 0:
            self.notification.setIcon(QIcon(":/Icons/notified_icon.svg"))

    @Slot()
    def setStatus(self, status: STATUS) -> QLabel:
        self.status.setPixmap(QPixmap(":/Icons/online.svg" if status == STATUS.OnLine else ":/Icons/offline.svg"))

    @Slot()
    def closeApp(self):
        dialog = closeSession(SESSION.Application)
        if dialog.exec():
            self.parent().parent().close()


    @Slot()
    def resizeWindow(self): 
        if self.parent().parent().isMaximized():
            self.resizeButton.setIcon(self.style().standardIcon(QStyle.SP_TitleBarNormalButton))
            self.parent().parent().showNormal()
        else:
            self.resizeButton.setIcon(self.style().standardIcon(QStyle.SP_TitleBarMaxButton))
            self.parent().parent().showMaximized() 

class Statusbar(QStatusBar):
    """
    This class is used to create the application's status bar
    """

    # Class attributes
    backgroundColor = "white"
    borderColor = "#f6f6f6"
    textColor = "#525252"

    def __init__(self):
        super().__init__()

        self.setStyleSheet(f"background-color: {Statusbar.backgroundColor}; padding-right: {fitValueToScreen(value=10)}px;")

        self.internetAccess = self.createFrame()
        self.databaseAccess = self.createFrame()

    def setInternetConnection(self, status: STATUS):
        self.icon.setPixmap(QPixmap(":/Icons/online.svg" if status == STATUS.OnLine else ":/Icons/offline.svg"))
        self.text.setText("Accès internet" if status == STATUS.OnLine else "Pas d'accès internet")


    def setDatabaseConnection(self, status: STATUS):
        self.icon.setPixmap(QPixmap(":/Icons/database_connected.svg" if status == STATUS.OnLine else ":/Icons/database_not_connected.svg"))
        self.text.setText("Connection établie" if status == STATUS.OnLine else "Accès refusé")
        self.databaseAccess = self.createFrame()        

    
    def createFrame(self) -> QFrame:
        frame = QFrame(self)
        frame.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        frame.setStyleSheet("background-color: none; border: none;")

        Layout = QHBoxLayout()
        Layout.setContentsMargins(0, 0, 0, 0)
        frame.setLayout(Layout)

        self.icon = QLabel(frame)
        self.icon.setStyleSheet("background-color: none; border-left: none;")
        self.icon.setScaledContents(True)
        self.icon.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        Layout.addWidget(self.icon)

        self.text = QLabel(frame)
        self.text.setStyleSheet(f"background-color: none; border-left: none; color: {Statusbar.textColor}")
        self.text.setFont(QFont('Calibri', fitValueToScreen(value=12), QFont.Normal, False))
        self.text.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        Layout.addWidget(self.text)

        self.addPermanentWidget(frame)

        return frame

# ::::::::Pages::::::::::::: #
class EmptyPage(QFrame):
    """
    # This class implements an empty page to inform that there is no data or that it is under maintenance.

    ## Methods

    ####  EmptyPage(title: str, imagePath: str, text: str) -> QFrame

    *Constructs an empty page with the given title, image and text*

    #### emptyPageWithButton(textButton: str, secondText: str) -> QFrame

    *Constructs an empty page whith a button to add data*
    """

    def __init__(self, title: str, imagePath: str, text: str):
        super().__init__()

        self.setFrameShape(QFrame.NoFrame)
        self.setStyleSheet("background-color: none; border: none;")
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.frameLayout = QVBoxLayout()
        self.setLayout(self.frameLayout)

        self.header = Header(self, self.frameLayout, title)
        self.frameLayout.setAlignment(self.header, Qt.AlignTop)

        self.imageLayout = QHBoxLayout()
        self.frameLayout.addLayout(self.imageLayout)
        self.frameLayout.setAlignment(self.imageLayout, Qt.AlignCenter)

        self.image = QLabel(self)
        self.image.setPixmap(QPixmap(imagePath))
        self.image.setScaledContents(True)
        self.image.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.image.setStyleSheet("background-color: none; border: none;")
        self.imageLayout.addWidget(self.image)

        self.label = QLabel(self)
        self.label.setText(text)
        self.label.setFont(QFont("Montserrat", fitValueToScreen(value=20), QFont.Medium))
        self.label.setStyleSheet("QLabel { color: black; background: none; border: none;}")
        self.label.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.frameLayout.addWidget(self.label)
        self.frameLayout.setAlignment(self.label, Qt.AlignCenter)

        self.frameLayout.addStretch()

    def emptyPageWithButton(self, textButton: str, secondText: str) -> QFrame:
        self.header.headerWithButton(textButton)

        self.textLayout = QHBoxLayout()
        self.frameLayout.addLayout(self.textLayout)
        self.frameLayout.setAlignment(self.textLayout, Qt.AlignCenter)

        self.textLayout.addStretch(1)
        
        self.secondLabel = QLabel(self)
        self.secondLabel.setText(secondText)
        self.secondLabel.setFont(QFont("Montserrat", fitValueToScreen(value=20), QFont.Medium))
        self.secondLabel.setStyleSheet("QLabel { color: black; background: none; border: none;}")
        self.secondLabel.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.textLayout.addWidget(self.secondLabel)

        self.button = StandardButton(self, self.textLayout, 45, 45).ButtonWithoutText()

        self.textLayout.addStretch(1)

        self.frameLayout.addStretch(2)

        return self


# ::::::::Pop up::::::::::::: #
def PopUp(title: str, message: str, icon: QMessageBox.Icon) -> QMessageBox:
    box_error = QMessageBox()
    box_error.setWindowIcon(QIcon(":/Pictures/icon.png"))
    box_error.setIcon(icon)
    box_error.setWindowTitle(title)
    box_error.setText(message)
    box_error.exec()

    return box_error

def closeSession(session: SESSION) -> QMessageBox:
    box = QMessageBox()
    box.setWindowTitle(session.value[0])
    box.setWindowIcon(QIcon(":/Pictures/icon.png"))
    box.setIcon(QMessageBox.Question)
    box.setText(session.value[1])
    acceptButton = box.addButton("Oui", QMessageBox.AcceptRole)
    rejectButton = box.addButton("Non", QMessageBox.RejectRole)

    acceptButton.clicked.connect(box.accept)
    rejectButton.clicked.connect(box.reject)

    return box

class MessageInputField(QFrame):


    # Class attribute
    backgroundColor = "white"
    borderColor = "#DCDCDC"
    separatorColor = "black"

    def __init__(self, parent: QWidget, Layout: QBoxLayout):
        super().__init__(parent)

        # List of files attached to the message
        self.files_to_send = []

        # ::::::::Creating the main frame1 of the text input field and its layout::::::::::::: #
        self.setStyleSheet(f"QFrame{{background-color: {MessageInputField.backgroundColor}; border: {fitValueToScreen(value=2)}px solid {MessageInputField.borderColor};}}")
        self.setFixedHeight(fitSizeToScreen(width=None, height=300))
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        # Adding its layout
        self.frameLayout = QVBoxLayout()
        self.frameLayout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.frameLayout)

        # ::::::::Creating the toolbar and its items::::::::::::: #
        self.toolbar = QFrame(self)
        self.toolbar.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.toolbar.setStyleSheet(f"background-color: {MessageInputField.borderColor};")
        self.frameLayout.addWidget(self.toolbar)
        self.frameLayout.setAlignment(self.toolbar, Qt.AlignTop)

        # Adding its layout
        self.toolbarLayout = QHBoxLayout()
        self.toolbarLayout.setContentsMargins(fitValueToScreen(value=2), fitValueToScreen(value=2), fitValueToScreen(value=2), fitValueToScreen(value=2))
        self.toolbar.setLayout(self.toolbarLayout)

        self.toolbarButton = ToolbarButtonForMessage(self.toolbar, self.toolbarLayout)

        # Adding the button to make text or selected text bold
        self.bold_button = ToolbarButtonForMessage(self.toolbar, self.toolbarLayout).textButton("G", True, False, False)
        self.bold_button.toggled.connect(self.setTextBold)
        self.toolbarLayout.addWidget(self.bold_button)

        # Adding the separator
        separator(self.toolbarLayout, MessageInputField.separatorColor)

        # Adding the button to italicize text or selected text
        self.italic_button = ToolbarButtonForMessage(self.toolbar, self.toolbarLayout).textButton("I", False, True, False)
        self.italic_button.toggled.connect(self.setTextItalic)
        self.toolbarLayout.addWidget(self.italic_button)

        # Adding the separator
        separator(self.toolbarLayout, MessageInputField.separatorColor)

        # Adding the button to underline text or selected text
        self.underline_button = ToolbarButtonForMessage(self.toolbar, self.toolbarLayout).textButton("S", False, False, True)
        self.underline_button.toggled.connect(self.setTextUnderline)
        self.toolbarLayout.addWidget(self.underline_button)

        # Adding the separator
        separator(self.toolbarLayout, MessageInputField.separatorColor)

        self.toolbarLayout.addStretch()

        # Adding the button to join a file
        self.file_button = ToolbarButtonForMessage(self.toolbar, self.toolbarLayout).iconButton(":/Icons/attachement_unclicked.svg", ":/Icons/attachement_clicked.svg", True)
        self.file_button.clicked.connect(self.selectFile)
        self.toolbarLayout.addWidget(self.file_button)

        # Adding the separator
        separator(self.toolbarLayout, MessageInputField.separatorColor)

        # Adding the button to clear the text input field
        self.clear_button =ToolbarButtonForMessage(self.toolbar, self.toolbarLayout).iconButton(":/Icons/bin_unclicked.svg", ":/Icons/bin_clicked.svg", False)
        self.clear_button.clicked.connect(self.clearTextField)
        self.toolbarLayout.addWidget(self.clear_button)

        # ::::::::Creating the text input field frame1::::::::::::: #
        self.inputField = QTextEdit(self)
        self.inputField.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.inputField.setStyleSheet(
            f"""
                background-color: #ffffff;
                color: #000000;
                selection-color: #ffffff;
                selection-background-color: #8676f3;
                border: none;
            """
        )
        self.inputField.textChanged.connect(self.enableSendButton)
        self.frameLayout.addWidget(self.inputField)

        # Set the default font
        self.default_font = QFont('Century Gothic', 12)
        self.inputField.setCurrentFont(self.default_font)

        # Activate button at start of input
        self.inputField.textChanged.connect(self.enableButton)

        # ::::::::Creating the footer frame1::::::::::::: #

        self.footerFrame = QFrame(self)
        self.footerFrame.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.footerFrame.setStyleSheet("background-color: none; border: none;")
        self.footerFrame.setFixedHeight(90)
        self.footerLayout = QHBoxLayout()
        self.footerFrame.setLayout(self.footerLayout)

        self.frameLayout.addWidget(self.footerFrame)
        self.frameLayout.setAlignment(self.footerFrame, Qt.AlignBottom)

        # ::::::::Create the selected files frame1 layout::::::::::::: #
        self.file_frame = QFrame(self.footerFrame)
        self.file_frame.setStyleSheet("background-color: white;")
        self.file_layout = QHBoxLayout()
        self.file_layout.setDirection(QBoxLayout.LeftToRight)
        self.file_frame.setLayout(self.file_layout)

        # Add the Scroll area
        self.Scroll = QScrollArea()
        self.Scroll.setWidget(self.file_frame)
        self.Scroll.setWidgetResizable(True)
        self.Scroll.setStyleSheet("background-color: none; ")
        self.footerLayout.addWidget(self.Scroll)

        # Add the message send button
        self.sendButton = StandardButton(self.footerFrame, self.footerLayout).sendButton()
        self.enableSendButton()

        Layout.addWidget(self)

    @Slot()
    def enableButton(self):
        self.bold_button.setEnabled(True)
        self.italic_button.setEnabled(True)
        self.underline_button.setEnabled(True)
        self.clear_button.setEnabled(True)

    @Slot()
    def setTextBold(self, checked: bool):
        cursor = self.inputField.textCursor()
        new_format = QTextCharFormat()
        new_format.setFontWeight(QFont.Bold if checked else QFont.Normal)
        self.inputField.setFontWeight(QFont.Bold if checked else QFont.Normal)

        current_format = cursor.charFormat().fontWeight()
        if cursor.hasSelection() and current_format == QFont.Normal:
            cursor.mergeCharFormat(new_format)
            self.inputField.setTextCursor(cursor)

    @Slot()
    def setTextItalic(self, checked: bool):

        cursor = self.inputField.textCursor()
        new_format = QTextCharFormat()
        new_format.setFontItalic(True if checked else False)
        self.inputField.setFontItalic(True if checked else False)

        current_format = cursor.charFormat().fontItalic()
        if cursor.hasSelection() and current_format:
            cursor.mergeCharFormat(new_format)
            self.inputField.setTextCursor(cursor)

    @Slot()
    def setTextUnderline(self, checked: bool):

        cursor = self.inputField.textCursor()
        new_format = QTextCharFormat()
        new_format.setFontUnderline(True if checked else False)
        self.inputField.setFontUnderline(True if checked else False)

        current_format = cursor.charFormat().fontUnderline()
        if cursor.hasSelection() and current_format:
            cursor.mergeCharFormat(new_format)
            self.inputField.setTextCursor(cursor)

    @Slot()
    def clearTextField(self):
        if self.inputField.document().isEmpty() is False:
            self.inputField.clear()
            self.bold_button.setChecked(False)
            self.italic_button.setChecked(False)
            self.underline_button.setChecked(False)

    @Slot()
    def selectFile(self):

        self.dialog = QFileDialog(self)
        self.dialog.setFileMode(QFileDialog.ExistingFile)
        self.dialog.setNameFilter("Tous les fichiers (*)")
        self.dialog.setViewMode(QFileDialog.Detail)

        # Création du repertoire de fichiers
        if self.dialog.exec():
            try:
                filenames = self.dialog.selectedFiles()
                size = os.path.getsize(filenames[0])

                if size > 10485760:
                    raise error(ERROR_TITLE.SelectedFileError.value, "Le fichier sélectionné est trop grand")

                if filenames[0] in self.files_to_send:
                    raise error(ERROR_TITLE.SelectedFileError.value, "Le fichier a déjà été sélectionné")

                if len(self.files_to_send) != 0:
                    files_size = []
                    for file in self.files_to_send:
                        s = os.path.getsize(file)
                        files_size.append(s)
                    files_size.append(size)
                    if sum(files_size) > 10485760:
                        raise error(ERROR_TITLE.SelectedFileError.value, "La taille des fichiers sélectionnés est trop grande")
            except error as e:
                PopUp(title=str(e.title), message=str(e.message), icon=QMessageBox.Critical)
            except OSError:
                PopUp(title=ERROR_TITLE.SelectedFileError.value, message="Le fichier sélectionné n'existe pas ou est innaccéssible", icon=QMessageBox.Critical)
            else:
                self.files_to_send.append(filenames[0])
                self.enableSendButton()
                self.file = DisplayFile(self, self.file_layout, filenames[0], size)
                self.file.fileForMessage(TYPE.Send)
                self.file.button.clicked.connect(self.removeFile)

    @Slot()
    def removeFile(self):
        # Recovery of the object that triggered the signal
        sender = self.sender()
        # retrieve its parent object, which is the frame
        selected_frame = sender.parent()
        # Remove the frame from file_Layout 
        selected_frame.deleteLater()
        # Remove the selected file from the list of selected files
        if selected_frame.absPath in self.files_to_send:
            self.files_to_send.remove(selected_frame.absPath)
            self.enableSendButton()

    def enableSendButton(self):
        text = self.inputField.toPlainText()
        if len(self.files_to_send) == 0 and text == "":
            self.sendButton.setDisabled(True)
        else:
            self.sendButton.setDisabled(False)
        
        return self.sendButton



