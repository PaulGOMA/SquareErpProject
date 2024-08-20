import sys
sys.path.append("..")

import time

from PySide6.QtCore import QObject, Signal

class Worker_with_int(QObject):
    update_page_signal = Signal(int)
    def __init__(self, Target=None):
        super().__init__()
        self.Target = Target
    def run(self, stop_event):
        while stop_event is None or not stop_event.is_set():
            self.update_page_signal.emit(self.Target())
            time.sleep(1)


class Worker_with_string(QObject):
    update_page_signal = Signal(str)

    def __init__(self, Target=None):
        super().__init__()
        self.Target = Target

    def run(self, stop_event):
        while stop_event is None or not stop_event.is_set():
            self.update_page_signal.emit(self.Target())
            time.sleep(1)

class Worker_with_list(QObject):
    update_page_signal = Signal(list)

    def __init__(self, Target=None):
        super().__init__()
        self.Target = Target

    def run(self, stop_event):
        while stop_event is None or not stop_event.is_set():
            self.update_page_signal.emit(self.Target())
            time.sleep(1)