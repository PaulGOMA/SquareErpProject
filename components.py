"""
    # This file contains all the functions
    # required to create the componants used in the application, 
    # such as buttons, search bars, etc.
"""

from PySide6.QtWidgets import QWidget, QHBoxLayout, QPushButton, QBoxLayout, QSizePolicy, QFrame, QLineEdit, QLabel, QVBoxLayout, QComboBox, QStyledItemDelegate, QStyle
from PySide6.QtGui import QIcon, QFont, Qt, QPixmap, QColor
from PySide6.QtCore import QSize
from enumeration import MESSAGE_FILE_TYPE as TYPE, PROGRESS


# ::::::::Buttons::::::::::::: #

# Add new element button
def add_button_without_text(parent: QWidget, layout: QBoxLayout) -> QPushButton:
    button = QPushButton(parent)
    button.setIcon(QIcon("Icons/big_plus_icon.svg"))
    button.setFlat(True)
    button.setFixedSize(44, 44)
    button.setStyleSheet(
        """
        QPushButton {background-color: #744BE0;border: none;}
        QPushButton:pressed {background-color: #52349f;}
        """
    )
    layout.addWidget(button)
    return button


def add_button_with_text(parent: QWidget, layout: QBoxLayout, text: str) -> QPushButton:
    button = QPushButton(QIcon("Icons/big_plus_icon.svg"), text, parent)
    button.setFlat(True)
    button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
    button.setFont(QFont("Montserrat", 11, QFont.DemiBold))
    button.setLayoutDirection(Qt.RightToLeft)
    button.setStyleSheet(
        """
        QPushButton {background-color: #744BE0; color: white; border: none; 
            padding-top: 10px; padding-right: 20px; padding-bottom: 10px; padding-left: 20px;}
        QPushButton:pressed {background-color: #52349f; color: white;}
        """
    )
    layout.addWidget(button)
    return button

# Validate button
def validate_button(parent: QWidget, layout: QBoxLayout) -> QPushButton:
    button = QPushButton(QIcon("Icons/validate_icon_button.svg"), "Valider ", parent)
    button.setFlat(True)
    button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
    button.setFont(QFont("Montserrat", 11, QFont.DemiBold))
    button.setLayoutDirection(Qt.RightToLeft)
    button.setStyleSheet(
        """
        QPushButton {background-color: #744BE0; color: white; border: none; 
            padding-top: 10px; padding-right: 20px; padding-bottom: 10px; padding-left: 20px;}
        QPushButton:pressed {background-color: #52349f; color: white;}
        """
    )
    layout.addWidget(button)
    return button

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# ::::::::text input line::::::::::::: #

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
    button.setIcon(QIcon("Icons/search_icon.svg"))
    button.setIconSize(QSize(26, 22))
    button.setStyleSheet("QPushButton:pressed {icon: url('Icons/search_icon_clicked.svg')}")
    frame_layout.addWidget(button)

    frame_layout.addStretch()

    line_edit = QLineEdit(frame)
    line_edit.setObjectName("line_edit")
    line_edit.setFixedWidth(175)
    line_edit.setPlaceholderText(text)
    line_edit.setFrame(QFrame.NoFrame)
    line_edit.setStyleSheet("background-color: transparent; color: #3d3d3d;")
    line_edit.setFont(QFont("Montserrat", 11, QFont.Normal))
    frame_layout.addWidget(line_edit)

    layout.addWidget(frame)
    return frame


def searchbar_for_navbar(parent: QWidget, layout: QBoxLayout) -> QFrame:
    frame = QFrame(parent)
    frame.setFixedSize(424, 52)
    frame.setStyleSheet("QFrame {background-color: transparent; border: 3px solid #e1e2fe;}")

    frame_layout = QHBoxLayout()
    frame.setLayout(frame_layout)

    line_edit = QLineEdit(frame)
    line_edit.setObjectName("line_edit")
    line_edit.setFixedWidth(350)
    line_edit.setPlaceholderText("Recherchez...")
    line_edit.setFrame(QFrame.NoFrame)
    line_edit.setStyleSheet("background-color: transparent; color: #3d3d3d;")
    line_edit.setFont(QFont("Montserrat", 11, QFont.Normal))
    frame_layout.addWidget(line_edit)

    frame_layout.addStretch()

    button = QPushButton(frame)
    button.setObjectName("button")
    button.setFlat(True)
    button.setIcon(QIcon("Icons/search_icon.svg"))
    button.setIconSize(QSize(26, 22))
    button.setStyleSheet("QPushButton:pressed {icon: url('Icons/search_icon_clicked.svg')}")
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
        icon.setPixmap(QPixmap("Icons/not_scheduled_icon.svg") )
        frame.setStyleSheet("QFrame{background-color: #F2D0D0}")
        label.setText("NON - PROGRAMME")
    elif progress == PROGRESS.Scheduled:
        icon.setPixmap(QPixmap("Icons/scheduled_icon.svg"))
        frame.setStyleSheet("QFrame{background-color: #F4E4AC}")
        label.setText("PROGRAMME")
    elif progress == PROGRESS.InProgress:
        icon.setPixmap(QPixmap("Icons/in_progress_icon.svg"))
        frame.setStyleSheet("QFrame{background-color: #B6F4AC}")
        label.setText("EN COURS")
    elif progress == PROGRESS.Finished:
        icon.setPixmap(QPixmap("Icons/finished_icon.svg"))
        frame.setStyleSheet("QFrame{background-color: #ACE7F4}")
        label.setText("TERMINE")

    frame_layout.addStretch(1)

    button = QPushButton(frame)
    button.setObjectName("button")
    button.setFlat(True)
    button.setIcon(QIcon("Icons/cross_icon_status.svg"))
    button.setStyleSheet("QPushButton:pressed {icon: url('Icons/cross_icon_status_clicked.svg')}")
    frame_layout.addWidget(button)

    layout.addWidget(frame)
    return frame

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# ::::::::display file::::::::::::: #

# File to send/download by message
def display_file_inside_message(parent: QWidget, layout: QBoxLayout, filename: str, size: int, type: TYPE) -> QFrame:
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
        icon.setPixmap(QPixmap("Icons/pdf_file_icon.svg"))
    elif file_format == 'txt':
        icon.setPixmap(QPixmap("Icons/txt_file_icon.svg"))
    elif file_format in ["zip", "7z"]:
        icon.setPixmap(QPixmap("Icons/zip_file_icon.svg"))
    elif file_format in ["png", "jpg", "bmp", "webp", "svg"]:
        icon.setPixmap(QPixmap("Icons/image_file_icon.svg"))
    elif file_format in ["mp3", "wav", "ogg"]:
        icon.setPixmap(QPixmap("Icons/audio_file_icon.svg"))
    elif file_format in ["mp4", "mov", "wmv", "webm", "avi"]:
        icon.setPixmap(QPixmap("Icons/video_file_icon.svg"))
    elif file_format in ["doc", "docx"]:
        icon.setPixmap(QPixmap("Icons/doc_file_icon.svg"))
    else:
        icon.setPixmap(QPixmap("Icons/unknown_file_icon.svg"))

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
    button.setIcon(QIcon("Icons/close_file_to_send.svg" if type.value else "Icons/download_file_icon.svg"))
    button.setStyleSheet("QPushButton:pressed {icon: url('Icons/close_file_to_send_clicked.svg')}" if type.value else "QPushButton:pressed {icon: url('Icons/download_file_icon_clicked.svg')}")
    frame_layout.addWidget(button)
    
    layout.addWidget(frame)
    return frame

# display report
def display_report(parent: QWidget, layout: QBoxLayout, filename: str, size: int) -> QFrame:
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
        icon.setPixmap(QPixmap("Icons/pdf_report_icon.svg"))
    elif file_format in ["doc", "docx"]:
        icon.setPixmap(QPixmap("Icons/doc_report_icon.svg"))
    else:
        icon.setPixmap(QPixmap("Icons/unknown_report_icon.svg"))

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
    button.setIcon(QIcon("Icons/close_report_icon.svg"))
    button.setStyleSheet("QPushButton:pressed {icon: url('Icons/close_report_icon_clicked.svg')}")
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
                image: url(Icons/down_arrow_icon.svg);
                margin-right: 16px; 
            }
            QComboBox:down-arrow:on {
                image: url(Icons/down_arrow_icon_on.svg);
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
# ::::::::display combo box::::::::::::: #