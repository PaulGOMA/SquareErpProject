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
    QTableView, QAbstractItemView, QButtonGroup, QCheckBox
from PySide6.QtGui import QIcon, QFont, Qt, QPixmap, QColor
from PySide6.QtCore import QSize, QAbstractTableModel

from Utils.enumeration import MESSAGE_FILE_TYPE as TYPE, PROGRESS,\
    CONNEXION_STATUS as STATUS, SIZE

from Assets import icons


# ::::::::Buttons::::::::::::: #

# Add new element button
def addButtonWithoutText(parent: QWidget, layout: QBoxLayout) -> QPushButton:
    button = QPushButton(parent)
    button.setIcon(QIcon(":/Icons/plus.svg"))
    button.setFlat(True)
    button.setFixedSize(44, 44)
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
    button.setFont(QFont("Montserrat", 11, QFont.DemiBold))
    button.setLayoutDirection(Qt.RightToLeft)
    button.setStyleSheet(
        """
        QPushButton {background-color: #5234a5; color: white; border: none; 
            padding-top: 10px; padding-right: 20px; padding-bottom: 10px; padding-left: 20px;}
        QPushButton:pressed {background-color: #44317e; color: white;}
        """
    )
    layout.addWidget(button)
    return button

# Validate button
def validateButton(parent: QWidget, layout: QBoxLayout) -> QPushButton:
    button = QPushButton(QIcon(":/Icons/validate.svg"), "Valider ", parent)
    button.setFlat(True)
    button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
    button.setFont(QFont("Montserrat", 11, QFont.DemiBold))
    button.setLayoutDirection(Qt.RightToLeft)
    button.setStyleSheet(
        """
        QPushButton {background-color: #5234a5; color: white; border: none; 
            padding-top: 10px; padding-right: 20px; padding-bottom: 10px; padding-left: 20px;}
        QPushButton:pressed {background-color: #44317e; color: white;}
        """
    )
    layout.addWidget(button)
    return button

# Side bar button
def sidebarButton(parent: QWidget, text: str, uncheckedIconPath: str, checkedIconPath: str, layout: QBoxLayout, group: QButtonGroup) -> QPushButton:
    button = QPushButton(QIcon(uncheckedIconPath), text, parent)
    button.setFlat(True)
    button.setCheckable(True)
    button.setMaximumWidth(186)
    button.setFixedHeight(51)
    button.setFont(QFont("Montserrat", 14, QFont.Normal))
    button.setStyleSheet(
        f"""
        QPushButton {{
            background-color: none; 
            text-align: left;
            color: #CAC9FC;
            border: none;
            padding-left: 12px;}}
        QPushButton:checked, QPushButton:hover {{
            icon: url({checkedIconPath});
            border-left: 3px solid white;
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
    button.setMaximumWidth(205)
    button.setFixedHeight(58)
    button.setFont(QFont("Montserrat", 14, QFont.Medium))
    button.setStyleSheet(
        f"""
        QPushButton {{
            background-color: none; 
            text-align: left;
            color: #5234a5;
            border: none;
            padding-left: 16px;}}
        QPushButton:checked, QPushButton:hover {{
            border-left: 3px solid #5234a5;
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
    button.setFixedSize(45, 45)
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
    button.setFixedSize(45, 45)
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
    button.setFixedSize(45, 45)
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
    button.setFixedSize(346, 38)
    button.setFlat(True)
    button.setStyleSheet(
        """
        QPushButton {background-color: #5234A5;border: none;}
        QPushButton:pressed {background-color: #44317e;}
        """
    )
    button.setFont(QFont("Montserrat", 16, QFont.DemiBold))

    layout.addWidget(button)
    return button

# Button without background and border
def bareButton(parent: QWidget, layout: QBoxLayout, text: str) -> QPushButton:
    button = QPushButton(parent)
    button.setText(text)
    button.setFlat(True)
    button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
    button.setFont(QFont("Montserrat", 10, QFont.Medium))
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
    frame.setFixedSize(240, 52)
    frame.setStyleSheet("QFrame {background-color: transparent; border: 3px solid #e1e2fe;}")

    frame_layout = QHBoxLayout()
    frame.setLayout(frame_layout)

    button = QPushButton(frame)
    button.setObjectName("button")
    button.setFlat(True)
    button.setIcon(QIcon(":/Icons/search.svg"))
    button.setIconSize(QSize(26, 22))
    button.setStyleSheet("QPushButton:pressed {icon: url(':/Icons/search_clicked.svg')}")
    frame_layout.addWidget(button)

    frame_layout.addStretch()

    line_edit = QLineEdit(frame)
    line_edit.setObjectName("line_edit")
    line_edit.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
    line_edit.setPlaceholderText(text)
    line_edit.setFrame(QFrame.NoFrame)
    line_edit.setStyleSheet("background-color: transparent; color: #3d3d3d;")
    line_edit.setFont(QFont("Montserrat", 11, QFont.Normal))
    frame_layout.addWidget(line_edit)

    layout.addWidget(frame)
    return frame


def searchbarForNavbar(parent: QWidget, layout: QBoxLayout) -> QFrame:
    frame = QFrame(parent)
    frame.setFixedSize(424, 40)
    frame.setStyleSheet("QFrame {background-color: transparent; border: 2px solid #e1e2fe;}")

    frame_layout = QHBoxLayout()
    frame.setLayout(frame_layout)

    line_edit = QLineEdit(frame)
    line_edit.setObjectName("line_edit")
    line_edit.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
    line_edit.setPlaceholderText("Recherchez...")
    line_edit.setFrame(QFrame.NoFrame)
    line_edit.setStyleSheet("background-color: transparent; color: #3d3d3d;")
    line_edit.setFont(QFont("Montserrat", 8, QFont.Normal))
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
def shortEntryField(parent: QWidget, layout: QBoxLayout, icon: str, placehoder: str, size: SIZE) -> QFrame:
    frame = QFrame(parent)
    frame.setFixedHeight(38)
    frame.setFixedWidth(163 if size == SIZE.Short else 346)
    frame.setStyleSheet("QFrame {border-bottom: 1px solid #8676F3; background-color: transparent; padding: 0px;}")

    frame_layout = QHBoxLayout()
    frame_layout.setContentsMargins(0, 0, 0, 4)
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
    line_edit.setFont(QFont("Montserrat", 10, QFont.Normal))
    frame_layout.addWidget(line_edit)

    frame_layout.addStretch()

    layout.addWidget(frame)
    return frame

def passwordEntryField(parent: QWidget, layout: QBoxLayout, placehoder: str) -> QFrame:
    frame = QFrame(parent)
    frame.setFixedSize(346, 38)
    frame.setStyleSheet("QFrame {border-bottom: 1px solid #8676F3; background-color: transparent; padding: 0px;}")

    frame_layout = QHBoxLayout()
    frame_layout.setContentsMargins(0, 0, 0, 6)
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
    line_edit.setFont(QFont("Montserrat", 10, QFont.Normal))
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
    frame.setFixedSize(214, 41)
    
    frame_layout = QHBoxLayout()
    frame.setLayout(frame_layout)

    icon = QLabel(frame)
    frame_layout.addWidget(icon)

    frame_layout.addStretch(1)

    label = QLabel(frame)
    label.setFont(QFont('Calibri', 12, QFont.DemiBold, True))
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
        """
            QFrame {border : 1px solid #7c7c7c; background-color : transparent;}
            QFrame:hover {background-color : #E1E2FE;}
        """ 
        if type.value else 
        """
            QFrame {border : 1px solid #656565; background-color : transparent;}
            QFrame:hover {background-color : #E1E2FE;}
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
    file_name.setFont(QFont('Calibri', 12, QFont.Normal, False))
    file_name.setStyleSheet("QLabel{color : #7c7c7c; border: none;}")
    if len(filename) > 6:
        name = filename[0:3] + "..."
        file_name.setText(name)
    else:
        file_name.setText(filename)

    frame_layout.addWidget(file_name)

    file_size = QLabel(frame)
    file_size.setFont(QFont('Calibri', 10, QFont.Bold, False))
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
    file_name.setFont(QFont('Calibri', 16, QFont.Bold, True))
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
    file_size.setFont(QFont('Calibri', 16, QFont.Bold, False))
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
        rect = option.rect.adjusted(16, 0, 0, 0)

        painter.setFont(QFont('Calibri', 14, QFont.Medium, False))
        if option.state & QStyle.State_Selected:
            painter.fillRect(option.rect, "#ACA8F9")
            painter.setPen(QColor("#ffffff"))  
        else:
            painter.setPen(option.palette.text().color())

        painter.drawText(rect, Qt.AlignLeft, index.data())

def combobox(parent: QWidget, layout: QBoxLayout, items: list) -> QComboBox:
    combo = QComboBox(parent)
    combo.addItems(items)
    combo.setFont(QFont('Calibri', 14, QFont.Medium, False))
    combo.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
    combo.setItemDelegate(CustomComboboxDelegate())
    combo.setStyleSheet(
        """
            QComboBox {
                background-color: #ffffff;
                border: 2px solid #3d3d3d;
                padding: 8px 76px 8px 16px;
                color: #3d3d3d;
            }
            QComboBox:on {
                border-color: #ACA8F9;
            }
            QComboBox:down-arrow {
                image: url(:/Icons/down_arrow.svg);
                margin-right: 16px; 
            }
            QComboBox:down-arrow:on {
                image: url(:/Icons/down_arrow_on.svg);
            }
            QComboBox::drop-down {
                border: none;
            }
            QComboBox QAbstractItemView {
                background-color: white;
                color: #3d3d3d;
                border: 2px solid #3d3d3d;
            }
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
    table.setFont(QFont('Calibri', 14, QFont.Medium, False))
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
            }
            QHeaderView:section{
                background-color: #744BE0;
            }
            QTableView::item:selected{
                background-color: #E1E2FE;
                border: 1px solid #E1E2FE;
            }
        """
    )

    layout.addWidget(table)
    return table

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# ::::::::separator::::::::::::: #
def separator(parent: QWidget, layout: QBoxLayout) -> QFrame:
    frame = QFrame(parent)
    frame.setFrameShape(QFrame.Shape.HLine)
    frame.setFrameShadow(QFrame.Shadow.Plain)

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

    font = QFont('Calibri', 12, QFont.Normal, False)

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
    check.setFont(QFont('Calibri', 14, QFont.Normal, False))
    check.setStyleSheet(
        """
            QCheckBox {
                spacing: 18px;
                color: black;
            }
            QCheckBox::indicator {
                width: 20px;
                height: 20px;
                border: 2px solid #a8a8a8;
            }
            QCheckBox::indicator:hover {
                border-color: #e1e1fe;
            }
            QCheckBox::indicator:checked {
                background-color: none;
                border: none;
                image: url(':/Icons/checkbox.svg')
            }
        """
    )

    layout.addWidget(check)
    return check