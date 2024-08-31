import sys
sys.path.append("..")

from PySide6.QtWidgets import QFrame, QWidget, QBoxLayout



class Contact(QFrame):
    

    def __init__(self, parent: QWidget, Layout: QBoxLayout):
        super().__init__(parent)

        