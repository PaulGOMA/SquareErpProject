from enum import Enum

class MESSAGE_FILE_TYPE(Enum):
    Download = 0
    Send  = 1

class PROGRESS(Enum):
    NotScheduled = 0
    Scheduled = 1
    InProgress = 2
    Finished = 3