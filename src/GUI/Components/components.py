"""
    # This file contains all the functions
    # required to create the componants used in the application, 
    # such as buttons, search bars, etc.
"""

import sys
sys.path.append("..")

from PySide6.QtWidgets import QWidget, QHBoxLayout, QStyle, \
    QPushButton, QBoxLayout, QSizePolicy, QFrame, QLineEdit, \
    QLabel, QVBoxLayout, QComboBox, QStyledItemDelegate, \
    QTableView, QAbstractItemView, QButtonGroup, QCheckBox,\
    QFormLayout, QListWidgetItem, QListWidget
from PySide6.QtGui import QIcon, QFont, Qt, QPixmap, QColor, QPalette,\
    QBrush
from PySide6.QtCore import QAbstractTableModel

from Utils.enumeration import MESSAGE_FILE_TYPE as TYPE, PROGRESS,\
    CONNEXION_STATUS as STATUS, SIZE

from Utils.responsiveLayout import fitSizeToScreen, fitValueToScreen

from Assets import icons


class CustomListWidgetDelegate(QStyledItemDelegate):
    def paint(self, painter, option, index):
        option.state &= ~QStyle.State_HasFocus
        super().paint(painter, option, index)

# ::::::::Buttons::::::::::::: #

# Add new element button
def addButtonWithoutText(parent: QWidget, layout: QBoxLayout) -> QPushButton:
    button = QPushButton(parent)
    button.setIcon(QIcon(":/Icons/plus.svg"))
    button.setFlat(True)
    button.setFixedSize(fitSizeToScreen(width=44, height=44))
    button.setStyleSheet(
        """
        QPushButton {background-color: #5234A5;border: none;}
        QPushButton:pressed {background-color: #44317e; text-decoration: underline;}
        """
    )
    layout.addWidget(button)
    return button


def addButtonWithText(parent: QWidget, layout: QBoxLayout, text: str) -> QPushButton:
    button = QPushButton(QIcon(":/Icons/plus.svg"), text, parent)
    button.setFlat(True)
    button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
    button.setFont(QFont("Montserrat", fitValueToScreen(value=11), QFont.DemiBold))
    button.setLayoutDirection(Qt.RightToLeft)
    button.setStyleSheet(
        f"""
        QPushButton {{background-color: #5234a5; color: white; border: none; 
            padding-top: {fitValueToScreen(value=10)}px; padding-right: {fitValueToScreen(value=20)}px; padding-bottom: {fitValueToScreen(value=10)}px; padding-left: {fitValueToScreen(value=20)}px;}}
        QPushButton:pressed {{background-color: #44317e; color: white;}}
        """
    )
    layout.addWidget(button)
    return button

# Validate button
def validateButton(parent: QWidget, layout: QBoxLayout) -> QPushButton:
    button = QPushButton(QIcon(":/Icons/validate.svg"), "Valider ", parent)
    button.setFlat(True)
    button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
    button.setFont(QFont("Montserrat", fitValueToScreen(value=11), QFont.DemiBold))
    button.setLayoutDirection(Qt.RightToLeft)
    button.setStyleSheet(
        f"""
        QPushButton {{background-color: #5234a5; color: white; border: none; 
            padding-top: {fitValueToScreen(value=10)}px; padding-right: {fitValueToScreen(value=20)}px; padding-bottom: {fitValueToScreen(value=10)}px; padding-left: {fitValueToScreen(value=20)}px;}}
        QPushButton:pressed {{background-color: #44317e; color: white;}}
        """
    )
    layout.addWidget(button)
    return button

# Side bar button
def sidebarButton(parent: QWidget, text: str, uncheckedIconPath: str, checkedIconPath: str, layout: QBoxLayout, group: QButtonGroup) -> QPushButton:
    button = QPushButton(QIcon(uncheckedIconPath), text, parent)
    button.setFlat(True)
    button.setCheckable(True)
    button.setMaximumWidth(fitSizeToScreen(width=186, height=None))
    button.setFixedHeight(fitSizeToScreen(width=None, height=51))
    button.setFont(QFont("Montserrat", fitValueToScreen(value=14), QFont.Normal))
    button.setStyleSheet(
        f"""
        QPushButton {{
            background-color: none; 
            text-align: left;
            color: #CAC9FC;
            border: none;
            padding-left: {fitValueToScreen(value=12)}px;}}
        QPushButton:checked, QPushButton:hover {{
            icon: url({checkedIconPath});
            border-left: {fitValueToScreen(value=3)}px solid white;
            background-color: #ACA8F9; 
            color: white;}}
        """
    )
    group.addButton(button)
    layout.addWidget(button)
    return button

def sidebarButtonForReport(parent: QWidget, text: str, layout: QBoxLayout, group: QButtonGroup) -> QPushButton:
    button = QPushButton(text, parent)
    button.setFlat(True)
    button.setCheckable(True)
    button.setMaximumWidth(fitSizeToScreen(width=205, height=None))
    button.setFixedHeight(fitSizeToScreen(width=None, height=58))
    button.setFont(QFont("Montserrat", fitValueToScreen(value=14), QFont.Medium))
    button.setStyleSheet(
        f"""
        QPushButton {{
            background-color: none; 
            text-align: left;
            color: #5234a5;
            border: none;
            padding-left: {fitValueToScreen(value=16)}px;}}
        QPushButton:checked, QPushButton:hover {{
            border-left: {fitValueToScreen(value=3)}px solid #5234a5;
            background-color: #ACA8F9; 
            color: white;}}
        """
    )
    group.addButton(button)
    layout.addWidget(button)
    return button

# title bar buttons
def closeWindowButton(parent: QWidget, layout: QBoxLayout) -> QPushButton:
    button = QPushButton(parent)
    button.setIcon(QIcon(":/Icons/unchecked_close.svg"))
    button.setFlat(True)
    button.setFixedSize(fitSizeToScreen(width=45, height=45))
    button.setStyleSheet(
        """
        QPushButton {background-color: none; border: none;}
        QPushButton:pressed, QPushButton:hover {
            background-color: #E81123;
            icon: url(":/Icons/checked_close.svg");
        }
        """
    )
    layout.addWidget(button)
    return button

def resizeWindowButton(parent: QWidget, layout: QBoxLayout) -> QPushButton:
    button = QPushButton(parent)
    button.setIcon(QIcon(":/Icons/unchecked_resize.svg"))
    button.setFlat(True)
    button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
    button.setCheckable(True)
    button.setFixedSize(fitSizeToScreen(width=45, height=45))
    button.setStyleSheet(
        """
        QPushButton {background-color: none; border: none;}
        QPushButton:hover {background-color: #EFEFFE; border: none;}
        QPushButton:checked {icon: url(":/Icons/checked_resize.svg");}
        """
    )
    layout.addWidget(button)
    return button

def minimizeWindowButton(parent: QWidget, layout: QBoxLayout) -> QPushButton:
    button = QPushButton(parent)
    button.setIcon(QIcon(":/Icons/minimize.svg"))
    button.setFlat(True)
    button.setFixedSize(fitSizeToScreen(width=45, height=45))
    button.setStyleSheet(
        """
        QPushButton {background-color: none; border: none;}
        QPushButton:hover {background-color: #EFEFFE; border: none;}
        """
    )
    layout.addWidget(button)
    return button

# Connection button
def connectionButton(parent: QWidget, layout: QBoxLayout) -> QPushButton:
    button = QPushButton(parent)
    button.setText("Valider")
    button.setFixedSize(fitSizeToScreen(width=346, height=38))
    button.setFlat(True)
    button.setStyleSheet(
        """
        QPushButton {background-color: #5234A5;border: none;}
        QPushButton:pressed {background-color: #44317e;}
        """
    )
    button.setFont(QFont("Montserrat", fitValueToScreen(value=16), QFont.DemiBold))

    layout.addWidget(button)
    return button

# Button without background and border
def bareButton(parent: QWidget, layout: QBoxLayout, text: str) -> QPushButton:
    button = QPushButton(parent)
    button.setText(text)
    button.setFlat(True)
    button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
    button.setFont(QFont("Montserrat", fitValueToScreen(value=10), QFont.Medium))
    button.setStyleSheet(
        """
        QPushButton {color: #8676F3;border: none;}
        QPushButton:pressed {color: #744be0;}
        """
    )

    layout.addWidget(button)
    return button

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# ::::::::text entry field::::::::::::: #

# Search bar 
def searchbar(parent: QWidget, layout: QBoxLayout, text: str) -> QFrame:
    frame = QFrame(parent)
    frame.setFixedSize(fitSizeToScreen(width=204, height=52))
    frame.setStyleSheet(f"QFrame {{background-color: transparent; border: {fitValueToScreen(value=3)}px solid #e1e2fe;}}")

    frame_layout = QHBoxLayout()
    frame.setLayout(frame_layout)

    button = QPushButton(frame)
    button.setObjectName("button")
    button.setFlat(True)
    button.setIcon(QIcon(":/Icons/search.svg"))
    button.setIconSize(fitSizeToScreen(width=26, height=22))
    button.setStyleSheet("QPushButton:pressed {icon: url(':/Icons/search_clicked.svg')}")
    frame_layout.addWidget(button)

    frame_layout.addStretch()

    line_edit = QLineEdit(frame)
    line_edit.setObjectName("line_edit")
    line_edit.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
    line_edit.setPlaceholderText(text)
    line_edit.setFrame(QFrame.NoFrame)
    line_edit.setStyleSheet("background-color: transparent; color: #3d3d3d;")
    line_edit.setFont(QFont("Montserrat", fitValueToScreen(value=11), QFont.Normal))
    frame_layout.addWidget(line_edit)

    layout.addWidget(frame)
    return frame


def searchbarForNavbar(parent: QWidget, layout: QBoxLayout) -> QFrame:
    frame = QFrame(parent)
    frame.setFixedSize(fitSizeToScreen(width=424, height=40))
    frame.setStyleSheet(f"QFrame {{background-color: transparent; border: {fitValueToScreen(value=2)}px solid #e1e2fe;}}")

    frame_layout = QHBoxLayout()
    frame.setLayout(frame_layout)

    line_edit = QLineEdit(frame)
    line_edit.setObjectName("line_edit")
    line_edit.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
    line_edit.setPlaceholderText("Recherchez...")
    line_edit.setFrame(QFrame.NoFrame)
    line_edit.setStyleSheet("background-color: transparent; color: #3d3d3d;")
    line_edit.setFont(QFont("Montserrat", fitValueToScreen(value=10), QFont.Normal))
    frame_layout.addWidget(line_edit)

    frame_layout.addStretch()

    button = QPushButton(frame)
    button.setObjectName("button")
    button.setFlat(True)
    button.setIcon(QIcon(":/Icons/search.svg"))
    button.setStyleSheet("QPushButton:pressed {icon: url(':/Icons/search_clicked.svg')}")
    frame_layout.addWidget(button)

    layout.addWidget(frame)
    return frame

# text entry field for login screens
def entryField(parent: QWidget, layout: QBoxLayout, icon: str, placehoder: str, size: SIZE) -> QFrame:
    frame = QFrame(parent)
    frame.setFixedHeight(fitSizeToScreen(width=None, height=38))
    frame.setFixedWidth(fitSizeToScreen(width=163, height=None) if size == SIZE.Short else fitSizeToScreen(width=346, height=None))
    frame.setStyleSheet(f"QFrame {{border-bottom: {fitValueToScreen(value=1)}px solid #8676F3; background-color: transparent; padding: 0px;}}")

    frame_layout = QHBoxLayout()
    frame_layout.setContentsMargins(0, 0, 0, fitValueToScreen(value=4))
    frame.setLayout(frame_layout)

    label = QLabel(frame)
    label.setPixmap(QPixmap(icon))
    label.setFrameShape(QFrame.NoFrame)
    label.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
    label.setStyleSheet("background: none; border: none;")
    label.setScaledContents(True)
    frame_layout.addWidget(label)

    line_edit = QLineEdit(frame)
    line_edit.setObjectName("line_edit")
    line_edit.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
    line_edit.setPlaceholderText(placehoder)
    line_edit.setFrame(QFrame.NoFrame)
    line_edit.setStyleSheet("background-color: transparent; color: #3d3d3d;")
    line_edit.setFont(QFont("Montserrat", fitValueToScreen(value=10), QFont.Normal))
    frame_layout.addWidget(line_edit)

    frame_layout.addStretch()

    layout.addWidget(frame)
    return frame

def passwordEntryField(parent: QWidget, layout: QBoxLayout, placehoder: str) -> QFrame:
    frame = QFrame(parent)
    frame.setFixedSize(fitSizeToScreen(width=346, height=38))
    frame.setStyleSheet(f"QFrame {{border-bottom: {fitValueToScreen(value=1)}px solid #8676F3; background-color: transparent; padding: 0px;}}")

    frame_layout = QHBoxLayout()
    frame_layout.setContentsMargins(0, 0, 0, fitValueToScreen(value=6))
    frame.setLayout(frame_layout)

    label = QLabel(frame)
    label.setPixmap(QPixmap(":/Icons/lock.svg"))
    label.setFrameShape(QFrame.NoFrame)
    label.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
    label.setStyleSheet("background: none; border: none;")
    label.setScaledContents(True)
    frame_layout.addWidget(label)

    line_edit = QLineEdit(frame)
    line_edit.setObjectName("line_edit")
    line_edit.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
    line_edit.setPlaceholderText(placehoder)
    line_edit.setFrame(QFrame.NoFrame)
    line_edit.setStyleSheet("background-color: transparent; color: #3d3d3d;")
    line_edit.setFont(QFont("Montserrat", fitValueToScreen(value=10), QFont.Normal))
    frame_layout.addWidget(line_edit)

    button = QPushButton(frame)
    button.setObjectName("button")
    button.setFlat(True)
    button.setCheckable(True)
    button.setIcon(QIcon(":/Icons/eye_opened.svg"))
    button.setStyleSheet("QPushButton:checked {icon: url(':/Icons/eye_closed.svg')}")
    frame_layout.addWidget(button)

    layout.addWidget(frame)
    return frame

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# ::::::::progress::::::::::::: #
def progress(parent: QWidget, layout: QBoxLayout, progress: PROGRESS) -> QFrame:
    frame = QFrame(parent)
    frame.setFixedSize(fitSizeToScreen(width=214, height=41))
    
    frame_layout = QHBoxLayout()
    frame.setLayout(frame_layout)

    icon = QLabel(frame)
    frame_layout.addWidget(icon)

    frame_layout.addStretch(1)

    label = QLabel(frame)
    label.setFont(QFont('Calibri', fitValueToScreen(value=12), QFont.DemiBold, True))
    label.setStyleSheet("color: #4F4F4F")
    frame_layout.addWidget(label)

    if progress == PROGRESS.NotScheduled:
        icon.setPixmap(QPixmap(":/Icons/not_scheduled.svg") )
        frame.setStyleSheet("QFrame{background-color: #F2D0D0}")
        label.setText("NON - PROGRAMME")
    elif progress == PROGRESS.Scheduled:
        icon.setPixmap(QPixmap(":/Icons/scheduled.svg"))
        frame.setStyleSheet("QFrame{background-color: #F4E4AC}")
        label.setText("PROGRAMME")
    elif progress == PROGRESS.InProgress:
        icon.setPixmap(QPixmap(":/Icons/in_progress.svg"))
        frame.setStyleSheet("QFrame{background-color: #B6F4AC}")
        label.setText("EN COURS")
    elif progress == PROGRESS.Finished:
        icon.setPixmap(QPixmap(":/Icons/finished.svg"))
        frame.setStyleSheet("QFrame{background-color: #ACE7F4}")
        label.setText("TERMINE")

    frame_layout.addStretch(1)

    button = QPushButton(frame)
    button.setObjectName("button")
    button.setFlat(True)
    button.setIcon(QIcon(":/Icons/cross_status.svg"))
    button.setStyleSheet("QPushButton:pressed {icon: url(':/Icons/cross_status_clicked.svg')}")
    frame_layout.addWidget(button)

    layout.addWidget(frame)
    return frame

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# ::::::::display file::::::::::::: #

# File to send/download by message
def displayFileInsideMessage(parent: QWidget, layout: QBoxLayout, filename: str, size: int, type: TYPE) -> QFrame:
    frame = QFrame(parent)
    frame.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
    frame.setStyleSheet(
        f"""
            QFrame {{border : {fitValueToScreen(value=1)}px solid #7c7c7c; background-color : transparent;}}
            QFrame:hover {{background-color : #E1E2FE;}}
        """ 
        if type.value else 
        f"""
            QFrame {{border : {fitValueToScreen(value=1)}px solid #656565; background-color : transparent;}}
            QFrame:hover {{background-color : #E1E2FE;}}
        """
    )
    frame.setToolTip(filename)

    frame_layout = QHBoxLayout()
    frame.setLayout(frame_layout)

    icon = QLabel(frame)
    icon.setStyleSheet("border: none;")
    split_file = filename.split(".")
    file_format = split_file[-1]
    if file_format == 'pdf':
        icon.setPixmap(QPixmap(":/Icons/pdf_file.svg"))
    elif file_format == 'txt':
        icon.setPixmap(QPixmap(":/Icons/txt.svg"))
    elif file_format in ["zip", "7z"]:
        icon.setPixmap(QPixmap(":/Icons/zip.svg"))
    elif file_format in ["png", "jpg", "bmp", "webp", "svg"]:
        icon.setPixmap(QPixmap(":/Icons/image.svg"))
    elif file_format in ["mp3", "wav", "ogg"]:
        icon.setPixmap(QPixmap(":/Icons/audio.svg"))
    elif file_format in ["mp4", "mov", "wmv", "webm", "avi"]:
        icon.setPixmap(QPixmap(":/Icons/video.svg"))
    elif file_format in ["doc", "docx"]:
        icon.setPixmap(QPixmap(":/Icons/doc_file.svg"))
    else:
        icon.setPixmap(QPixmap(":/Icons/unknown_file.svg"))

    frame_layout.addWidget(icon)

    frame_layout.addStretch(1)

    file_name = QLabel(frame)
    file_name.setFont(QFont('Calibri', fitValueToScreen(value=12), QFont.Normal, False))
    file_name.setStyleSheet("QLabel{color : #7c7c7c; border: none;}")
    if len(filename) > 6:
        name = filename[0:3] + "..."
        file_name.setText(name)
    else:
        file_name.setText(filename)

    frame_layout.addWidget(file_name)

    file_size = QLabel(frame)
    file_size.setFont(QFont('Calibri', fitValueToScreen(value=10), QFont.Bold, False))
    file_size.setStyleSheet("color: #656565; border: none;")

    if 1 <= len(str(size)) <= 2:
        file_size.setText(f"{size} o")
    elif 3 <= len(str(size)) <= 5:
        value = size / 1024
        file_size.setText(f"{value: .2f} Ko")
    elif 6 <= len(str(size)) <= 7:
        value = size / 1048576
        file_size.setText(f"{value: .2f} Mo")
    else:
        file_size.setText("!!")

    frame_layout.addWidget(file_size) 

    frame_layout.addStretch(1)

    button = QPushButton(frame)
    button.setObjectName("button")
    button.setFlat(True)
    button.setIcon(QIcon(":/Icons/close_file.svg" if type.value else "Icons/download_file_icon.svg"))
    button.setStyleSheet("QPushButton:pressed {icon: url(':/Icons/close_file_clicked.svg')}" if type.value else "QPushButton:pressed {icon: url('Icons/download_file_icon_clicked.svg')}")
    frame_layout.addWidget(button)
    
    layout.addWidget(frame)
    return frame

# display report
def displayReport(parent: QWidget, layout: QBoxLayout, filename: str, size: int) -> QFrame:
    frame = QFrame(parent)
    frame.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
    frame.setStyleSheet(
        """
            QFrame {border : none; background-color : transparent;}
            QFrame:hover {background-color : #E1E2FE;}
        """ 
    )
    frame.setToolTip(filename)

    frame_layout = QHBoxLayout()
    frame.setLayout(frame_layout)

    frame_layout.addStretch(1)

    first_layout = QVBoxLayout()
    frame_layout.addLayout(first_layout)

    icon = QLabel(frame)
    icon.setStyleSheet("border: none;")
    split_file = filename.split(".")
    file_format = split_file[1]
    if file_format == 'pdf':
        icon.setPixmap(QPixmap(":/Icons/pdf_report.svg"))
    elif file_format in ["doc", "docx"]:
        icon.setPixmap(QPixmap(":/Icons/doc_report.svg"))
    else:
        icon.setPixmap(QPixmap(":/Icons/unknown_report.svg"))

    icon_layout = QHBoxLayout()
    first_layout.addLayout(icon_layout)
    icon_layout.addStretch(1)
    icon_layout.addWidget(icon)
    icon_layout.addStretch(1)
    first_layout.addStretch(1)

    file_name = QLabel(frame)
    file_name.setFont(QFont('Calibri', fitValueToScreen(value=16), QFont.Bold, True))
    file_name.setStyleSheet("QLabel{color : #7c7c7c; border: none;}")
    if len(filename) > 12:
        name = filename[0:9] + "..."
        file_name.setText(name)
    else:
        file_name.setText(filename)

    file_name_layout = QHBoxLayout()
    file_name_layout.addStretch(1)
    file_name_layout.addWidget(file_name)
    file_name_layout.addStretch(1)
    first_layout.addLayout(file_name_layout)
    first_layout.addStretch(1)

    file_size = QLabel(frame)
    file_size.setFont(QFont('Calibri', fitValueToScreen(value=16), QFont.Bold, False))
    file_size.setStyleSheet("color: #656565; border: none;")

    if 1 <= len(str(size)) <= 2:
        file_size.setText(f"{size} o")
    elif 3 <= len(str(size)) <= 5:
        value = size / 1024
        file_size.setText(f"{value: .2f} Ko")
    elif 6 <= len(str(size)) <= 7:
        value = size / 1048576
        file_size.setText(f"{value: .2f} Mo")
    else:
        file_size.setText("!!")

    file_size_layout = QHBoxLayout()
    file_size_layout.addStretch(1)
    file_size_layout.addWidget(file_size) 
    file_size_layout.addStretch(1)
    first_layout.addLayout(file_size_layout)

    second_layout = QVBoxLayout()
    frame_layout.addLayout(second_layout)

    button = QPushButton(frame)
    button.setObjectName("button")
    button.setFlat(True)
    button.setIcon(QIcon(":/Icons/close_report.svg"))
    button.setStyleSheet("QPushButton:pressed {icon: url(':/Icons/close_report_clicked.svg')}")
    second_layout.addWidget(button)

    second_layout.addStretch()
    frame_layout.addStretch(1)
    
    layout.addWidget(frame)
    return frame

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# ::::::::display combo box::::::::::::: #

#Customize combo box
class CustomComboboxDelegate(QStyledItemDelegate):
    def paint(self, painter, option, index):
        rect = option.rect.adjusted(fitValueToScreen(value=16), 0, 0, 0)

        painter.setFont(QFont('Calibri', fitValueToScreen(value=14), QFont.Medium, False))
        if option.state & QStyle.State_Selected:
            painter.fillRect(option.rect, "#ACA8F9")
            painter.setPen(QColor("#ffffff"))  
        else:
            painter.setPen(option.palette.text().color())

        painter.drawText(rect, Qt.AlignLeft, index.data())

def combobox(parent: QWidget, layout: QBoxLayout, items: list) -> QComboBox:
    combo = QComboBox(parent)
    combo.addItems(items)
    combo.setFont(QFont('Calibri', fitValueToScreen(value=14), QFont.Medium, False))
    combo.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
    combo.setItemDelegate(CustomComboboxDelegate())
    combo.setStyleSheet(
        f"""
            QComboBox {{
                background-color: #ffffff;
                border: {fitValueToScreen(value=2)}px solid #3d3d3d;
                padding: {fitValueToScreen(value=8)}px {fitValueToScreen(value=76)}px {fitValueToScreen(value=8)}px {fitValueToScreen(value=16)}px;
                color: #3d3d3d;
            }}
            QComboBox:on {{
                border-color: #ACA8F9;
            }}
            QComboBox:down-arrow {{
                image: url(:/Icons/down_arrow.svg);
                margin-right: {fitValueToScreen(value=16)}px; 
            }}
            QComboBox:down-arrow:on {{
                image: url(:/Icons/down_arrow_on.svg);
            }}
            QComboBox::drop-down {{
                border: none;
            }}
            QComboBox QAbstractItemView {{
                background-color: white;
                color: #3d3d3d;
                border: {fitValueToScreen(value=2)}px solid #3d3d3d;
            }}
        """
    )

    layout.addWidget(combo)
    return combo

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# ::::::::display table view::::::::::::: #

# Setting up the data manager
class CustomTableModel(QAbstractTableModel):
    def __init__(self, data):
        super(CustomTableModel, self).__init__()
        self._data = data

    def data(self, index, role):
        if role == Qt.DisplayRole:
            return self._data[index.row()][index.column()]

    def rowCount(self, index):
        return len(self._data)

    def columnCount(self, index):
        return len(self._data[0]) if self._data else 0
    

def displayTable(parent: QWidget, layout: QBoxLayout, model: CustomTableModel) -> QTableView:
    table = QTableView(parent)
    table.setModel(model)
    table.setItemDelegate(CustomListWidgetDelegate(table))
    table.setFont(QFont('Calibri', fitValueToScreen(value=14), QFont.Medium, False))
    table.setGridStyle(Qt.NoPen)
    table.setSelectionMode(QAbstractItemView.SingleSelection)
    table.setSelectionBehavior(QAbstractItemView.SelectRows)
    table.setStyleSheet(
        """
            QTableView {
                background-color: #ffffff;
                color: #3d3d3d;                
                selection-color: #ffffff;
                selection-background-color: #E1E2FE;
                border: none;
            }
            QHeaderView:section{
                background-color: #5234A5;
            }
            QTableView::item:selected{
                background-color: #E1E2FE;
                color: #5234A5;
                border: none;
            }
        """
    )

    layout.addWidget(table)
    return table

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# ::::::::separator::::::::::::: #
def separator(parent: QWidget, layout: QBoxLayout, color: str) -> QFrame:
    frame = QFrame(parent)
    frame.setFrameShape(QFrame.Shape.HLine if type(layout) == QVBoxLayout else QFrame.Shape.VLine)
    frame.setFrameShadow(QFrame.Shadow.Plain)
    frame.setStyleSheet(f"border-top: 1px solid {color}")

    layout.addWidget(frame)
    return frame

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# ::::::::user::::::::::::: #
def user(parent: QWidget, layout: QBoxLayout, username: str, usermail: str) -> QFrame:
    frame = QFrame(parent)
    frame.setFrameShape(QFrame.NoFrame)
    frame.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
    frame.setStyleSheet("background-color: none;")

    frameLayout = QVBoxLayout()
    frameLayout.setContentsMargins(0, 0, 0, 0)
    frame.setLayout(frameLayout)

    font = QFont('Calibri', fitValueToScreen(value=12), QFont.Normal, False)

    name = QLabel(frame)
    name.setText(username)
    name.setFont(font)
    name.setStyleSheet("color: #525252;")
    name.setObjectName("name")
    frameLayout.addWidget(name)

    mail = QLabel(frame)
    mail.setText(usermail)
    mail.setFont(font)
    mail.setStyleSheet("color: #525252;")
    mail.setObjectName("mail")
    frameLayout.addWidget(mail)

    layout.addWidget(frame)
    return frame

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# ::::::::attendance status::::::::::::: #
def attendanceStatus(parent: QWidget, layout: QBoxLayout, status: STATUS) -> QLabel:
    label = QLabel(parent)
    label.setFrameShape(QFrame.NoFrame)
    label.setScaledContents(True)
    label.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
    label.setPixmap(QPixmap(":/Icons/online.svg" if status == STATUS.OnLine else ":/Icons/offline.svg"))

    layout.addWidget(label)
    return label

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# ::::::::display check box::::::::::::: #

# check box for login screen
def loginCheckbox(parent: QWidget, layout: QBoxLayout) -> QCheckBox:
    check = QCheckBox("Se souvenir de moi", parent)
    check.setFont(QFont('Calibri', fitValueToScreen(value=14), QFont.Normal, False))
    check.setStyleSheet(
        f"""
            QCheckBox {{
                spacing: {fitValueToScreen(value=18)}px;
                color: black;
            }}
            QCheckBox::indicator {{
                width: {fitValueToScreen(value=20)}px;
                height: {fitValueToScreen(value=20)}px;
                border: {fitValueToScreen(value=2)}px solid #a8a8a8;
            }}
            QCheckBox::indicator:hover {{
                border-color: #e1e1fe;
            }}
            QCheckBox::indicator:checked {{
                background-color: none;
                border: none;
                image: url(':/Icons/checkbox.svg')
            }}
        """
    )

    layout.addWidget(check)
    return check

# Set background image
def setBackgroundImage(widget: QWidget, imagePath: str) -> None:
    pixmap = QPixmap(imagePath)
    palette = QPalette()
    palette.setBrush(QPalette.Window, QBrush(pixmap.scaled(widget.size(), Qt.IgnoreAspectRatio, Qt.SmoothTransformation)))
    widget.setPalette(palette)
    widget.setAutoFillBackground(True)

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# ::::::::display contact::::::::::::: #

# contact acronym
def contactAcronym(parent: QWidget, layout: QBoxLayout, fName: str, lName: str, size: SIZE) -> QFrame:
    frame = QFrame(parent)
    frame.setFixedSize(fitSizeToScreen(width=72, height=72) if size == SIZE.Long else fitSizeToScreen(width=48, height=48))
    frame.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
    frame.setStyleSheet(
        f"""
            background-color: #5234A5; 
            border-radius: {fitValueToScreen(value=36)}px; 
            border: {fitValueToScreen(value=2)}px solid #525252;

        """ if size == SIZE.Long else 
        f"""
            background-color: #5234A5; 
            color: white; 
            border-radius: {fitValueToScreen(value=24)}px; 
            border: {fitValueToScreen(value=2)}px solid #525252;

        """)
    
    frameLayout = QHBoxLayout()
    frame.setLayout(frameLayout)
    
    label = QLabel(frame)
    label.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
    label.setText((fName[0] + lName[0]).upper())
    label.setFont(QFont('Calibri', fitValueToScreen(value=28) if size == SIZE.Long else fitValueToScreen(value=16) , QFont.Medium, False))
    label.setStyleSheet(" background-color: none; color: white; border: none;")

    frameLayout.addWidget(label)
    frameLayout.setAlignment(label, Qt.AlignCenter)
    layout.addWidget(frame)
    return frame

# contact details
def contactDetails(parent: QWidget, layout: QBoxLayout, mail: str, phone: str, job: str, field: str) -> QFrame:
    frame = QFrame(parent)
    frame.setFrameShape(QFrame.NoFrame)
    frame.setStyleSheet("background-color: none; border: none;")
    frame.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

    frameLayout = QFormLayout()
    frameLayout.setHorizontalSpacing(fitValueToScreen(value=16))
    frameLayout.setContentsMargins(0, 0, 0, 0)
    frame.setLayout(frameLayout)

    font_title = QFont('Calibri', fitValueToScreen(value=16), QFont.Medium, False)
    font_content = QFont('Calibri', fitValueToScreen(value=14), QFont.Medium, True)

    mail_icon = QLabel(frame)
    mail_icon.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
    mail_icon.setScaledContents(True)
    mail_icon.setPixmap(QPixmap(":/Icons/mail_contact.svg"))

    mail_layout = QVBoxLayout()
    mail_layout.setContentsMargins(0, 0, 0, 0)

    mail_title = QLabel(frame)
    mail_title.setText("Adresse mail")
    mail_title.setFont(font_title)
    mail_title.setStyleSheet("background-color: none; color: black; border: none;")
    mail_layout.addWidget(mail_title)

    mail_content = QLabel(frame)
    mail_content.setText(mail)
    mail_content.setFont(font_content)
    mail_content.setStyleSheet("background-color: none; color: #5d5d5d; border: none;")
    mail_layout.addWidget(mail_content)

    frameLayout.addRow(mail_icon, mail_layout)

    phone_icon = QLabel(frame)
    phone_icon.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
    phone_icon.setScaledContents(True)
    phone_icon.setPixmap(QPixmap(":/Icons/phone_contact.svg"))

    phone_layout = QVBoxLayout()
    phone_layout.setContentsMargins(0, 0, 0, 0)

    phone_title = QLabel(frame)
    phone_title.setText("Adresse phone")
    phone_title.setFont(font_title)
    phone_title.setStyleSheet("background-color: none; color: black; border: none;")
    phone_layout.addWidget(phone_title)

    phone_content = QLabel(frame)
    phone_content.setText(phone)
    phone_content.setFont(font_content)
    phone_content.setStyleSheet("background-color: none; color: #5d5d5d; border: none;")
    phone_layout.addWidget(phone_content)

    frameLayout.addRow(phone_icon, phone_layout)

    job_icon = QLabel(frame)
    job_icon.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
    job_icon.setScaledContents(True)
    job_icon.setPixmap(QPixmap(":/Icons/job_contact.svg"))

    job_layout = QVBoxLayout()
    job_layout.setContentsMargins(0, 0, 0, 0)

    job_title = QLabel(frame)
    job_title.setText("Poste")
    job_title.setFont(font_title)
    job_title.setStyleSheet("background-color: none; color: black; border: none;")
    job_layout.addWidget(job_title)

    job_content = QLabel(frame)
    job_content.setText(job)
    job_content.setFont(font_content)
    job_content.setStyleSheet("background-color: none; color: #5d5d5d; border: none;")
    job_layout.addWidget(job_content)

    frameLayout.addRow(job_icon, job_layout)

    field_icon = QLabel(frame)
    field_icon.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
    field_icon.setScaledContents(True)
    field_icon.setPixmap(QPixmap(":/Icons/field_contact.svg"))

    field_layout = QVBoxLayout()
    field_layout.setContentsMargins(0, 0, 0, 0)

    field_title = QLabel(frame)
    field_title.setText("Adresse field")
    field_title.setFont(font_title)
    field_title.setStyleSheet("background-color: none; color: black; border: none;")
    field_layout.addWidget(field_title)

    field_content = QLabel(frame)
    field_content.setText(field)
    field_content.setFont(font_content)
    field_content.setStyleSheet("background-color: none; color: #5d5d5d; border: none;")
    field_layout.addWidget(field_content)

    frameLayout.addRow(field_icon, field_layout)

    layout.addWidget(frame)
    return frame

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# ::::::::display list view::::::::::::: #

def listWidget(parent: QWidget, layout: QBoxLayout) -> QListWidget:
    list = QListWidget(parent)
    list.setItemDelegate(CustomListWidgetDelegate(list))
    list.setStyleSheet(
        f"""
            QListWidget::item {{
                border: {fitValueToScreen(value=1)}px solid transparent;
                background-color: transparent;
            }}
            QListWidget::item:hover {{
                background-color: #E1E2FE;
            }}
            QListWidget::item:selected {{
                border-left: {fitValueToScreen(value=3)}px solid #5234a5;
                background-color: #E1E2FE;
            }}
        """
    )

    layout.addWidget(list)

    return list

def messageItem(parent: QListWidget, fName: str, lName: str, txt: str) -> None:
    frame = QFrame()
    frame.setFrameShape(QFrame.NoFrame)
    frame.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
    frame.setStyleSheet("background-color: none; border: none;")
    
    frameLayout = QHBoxLayout()
    frame.setLayout(frameLayout)

    contactAcronym(parent=frame, layout=frameLayout, fName=fName, lName=lName, size=SIZE.Short)

    frameLayout.addStretch(1)

    contentLayout = QVBoxLayout()
    contentLayout.setContentsMargins(0, 0, 0, 0)
    frameLayout.addLayout(contentLayout)

    contactName = QLabel(frame)
    contactName.setText(f"{fName.capitalize() + " " + lName.upper()}")
    contactName.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
    contactName.setFont(QFont("Montserrat", fitValueToScreen(value=10), QFont.DemiBold))
    contactName.setStyleSheet("background-color: none; border: none; color: #3d3d3d")
    contentLayout.addWidget(contactName)

    text = QLabel(frame)
    text.setText(txt)
    text.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
    text.setFont(QFont("Montserrat", fitValueToScreen(value=10), QFont.Normal))
    text.setStyleSheet("background-color: none; border: none; color: #3d3d3d")
    contentLayout.addWidget(text)

    frameLayout.addStretch(4)

    item = QListWidgetItem(parent)
    item.setSizeHint(frame.sizeHint())

    parent.setItemWidget(item, frame)
