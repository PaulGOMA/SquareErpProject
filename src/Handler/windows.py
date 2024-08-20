import sys
sys.path.append("..")

from PySide6.QtWidgets import QApplication

class WindowManager:
    def __init__(self):
        self.app = QApplication(sys.argv)  # Une seule instance d'application
        self.current_window = None
        self.window_classes = []  # Liste des classes de fenêtres
        self.current_index = -1

    def run(self):
        if self.window_classes:  # Assurer qu'il y a des fenêtres à afficher
            self.set_current_index(0)  # Afficher la première fenêtre
            sys.exit(self.app.exec())  # Lancer la boucle d'événements

    def set_current_index(self, new_index, exit=True):
        if 0 <= new_index < len(self.window_classes):  # Vérifier que l'index est valide
            if self.current_window:
                self.current_window.close() if exit else self.current_window.hide()  # Fermer la fenêtre courante
            self.current_index = new_index
            self.current_window = self.window_classes[self.current_index]()  # Créer une nouvelle instance de la fenêtre
            #self.current_window.show()  # Afficher la nouvelle fenêtre

    def get_current_index(self):
        return self.current_index

    def add_window(self, window_class):
        self.window_classes.append(window_class)

