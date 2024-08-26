import sys
sys.path.append("..")

import time

from PySide6.QtCore import QObject, Signal

from Utils.enumeration import CONNEXION_STATUS as STATUS

class WorkerWithInt(QObject):
    updatePageSignal = Signal(int)
    def __init__(self, Target=None):
        super().__init__()
        self.Target = Target
    def run(self, stop_event):
        while stop_event is None or not stop_event.is_set():
            self.updatePageSignal.emit(self.Target())
            time.sleep(1)


class WorkerWithString(QObject):
    updatePageSignal = Signal(str)

    def __init__(self, Target=None):
        super().__init__()
        self.Target = Target

    def run(self, stop_event):
        while stop_event is None or not stop_event.is_set():
            self.updatePageSignal.emit(self.Target())
            time.sleep(1)

class WorkerWithList(QObject):
    updatePageSignal = Signal(list)

    def __init__(self, Target=None):
        super().__init__()
        self.Target = Target

    def run(self, stop_event):
        while stop_event is None or not stop_event.is_set():
            self.updatePageSignal.emit(self.Target())
            time.sleep(1)

class WorkerWithConnexionStatus(QObject):
    updatePageSignal = Signal(STATUS)

    def __init__(self, Target=None):
        super().__init__()
        self.Target = Target

    def run(self, stop_event):
        while stop_event is None or not stop_event.is_set():
            self.updatePageSignal.emit(self.Target())
            time.sleep(1)