import sys
sys.path.append("..")

from Utils.enumeration import ERROR_TITLE

class error(Exception):
    def __init__(self, title: ERROR_TITLE, message: str):
        super().__init__(message)
        self.message = message
        self.title = title