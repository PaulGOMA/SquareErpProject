"""
    # This file contains all the custom constants used in the application.
"""

from enum import Enum

class MESSAGE_FILE_TYPE(Enum):
    Download = 0
    Send  = 1

class PROGRESS(Enum):
    NotScheduled = 0
    Scheduled = 1
    InProgress = 2
    Finished = 3

class CONNEXION_STATUS(Enum):
    OffLine = 0
    OnLine = 1

class SIZE(Enum):
    Short = 0
    Long = 1

class ERROR_TITLE(Enum):
    SelectedFileError = "Erreur de fichier sélectionné"
    DataEntryError = "Erreur de donnée saisie"
    InscriptionError = "Erreur d'inscription de l'utilisateur"
    FileSystemError = "Erreur du système de fichier"
    ServerConnectionError = "Erreur de connexion au serveur"
    AccountRecoveryError = "Erreur de récupération du compte"
    InternetConnectionError = "Erreur de connecxion de internet"