import sys
sys.path.append("..")

# ::::::::error due to selected file::::::::::::: #
class SelectedFileError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message
        self.title = "Erreur de fichier sélectionné"

# ::::::::error triggered by incorrect data entry::::::::::::: #
class DataEntryError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message
        self.title = "Erreur de donnée saisie"
