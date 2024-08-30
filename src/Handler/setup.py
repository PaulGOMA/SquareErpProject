import sys 
sys.path.append("..")

from PySide6.QtWidgets import QMessageBox
from PySide6.QtCore import QTimer

from Handler.encryptions import EncryptionManager
from Handler.databaseConnector import MySQLConnector
from Utils.checkField import *
from GUI.Components.widgets import PopUp, closeApp
from Handler.appDirectory import FileManager
from Handler.users import UserManager
from Handler.windows import WindowManager
from Handler.internet import InternetManager


class SetUp():
    def __init__(self):
        
        self.MySQLConnector = MySQLConnector('localhost', 'genius_database', 'root', '')
        self.EncryptionManager = EncryptionManager()
        self.timer = QTimer()
        self.InternetManager = InternetManager()
        self.WindowManager = WindowManager()
        self.FileManager = FileManager()


    def Deconnexion(self):
        dialog = closeApp(deconnection=True)
        if dialog.exec():
            dialog.accept()
            self.WindowManager.setCurrentIndex(1)
            self.WindowManager.current_window.Push_button.clicked.connect(lambda: self.Login(
                self.WindowManager.current_window.dataList))

    def Inscription_from_new_user(self, List: list):
        surname = List[0]
        name = List[1]
        email = List[2]
        number = List[3]
        password = List[4] 
        conf_pwd = List[5]


        #generer les clés de chiffrement
        key = self.EncryptionManager.generate_key()

        try:
            # Vérifier que tous les champs sont remplis
            check_all_fields_filled(List)

            # Vérifier le format de l'email
            check_email_format(email)

            # Vérifier le format du numéro de téléphone (par exemple, uniquement chiffres)
            check_phone_format(number)

            # Vérifier que les mots de passe correspondent
            check_passwords_match(password, conf_pwd)

            # Vérifier que la taille du mot de passe est supérieure à 6 caractères
            check_password_length(password)

            # Vérifier que le mot de passe est différent du nom
            check_password_differs_from_name(password, name, surname)

            # Vérifier que le mot de passe contient au moins une majuscule, une lettre et un chiffre
            check_password_complexity(password)

            if not self.MySQLConnector.connect():
                Result = self.MySQLConnector.execute_procedure('new_user',
                                ((name+' '+surname), password, email.lower(), number, self.EncryptionManager.Encode(self.EncryptionManager.key), self.EncryptionManager.Encode(key)))
                if Result:
                    raise error(ERROR_TITLE.InscriptionError.value, "Échec lors de l'inscription")
                else:
                    if self.FileManager.init_directory():
                        self.FileManager.write_file(file_path=self.FileManager.central_path + "/Users/" + email.lower() + '.log',
                                            lines=[(self.EncryptionManager.hash_element(password)), ], mode='w')
                        self.EncryptionManager.set_key(self.EncryptionManager.primary_key)
                        self.FileManager.write_file(file_path=self.FileManager.central_path + "/Acces/Encryptionkey.log",
                                            lines=[(self.EncryptionManager.encrypt_key(self.EncryptionManager.key)), ], mode='w')
                        # fin et sortie
                        PopUp("Succes" ,"Inscription réussie", QMessageBox.Information)
                        UserManager.email = email.lower()
                        UserManager.password = password
                        self.WindowManager.setCurrentIndex(3)
                        self.WindowManager.current_window.sidebar.logOut.clicked.connect(lambda: self.Deconnexion())
                    else:
                        raise error(ERROR_TITLE.FileSystemError.value, "Échec de la création des fichiers en \nraison d'une erreur du système de fichiers. \nVeuillez réessayer ou contacter le support technique.")
            else:
                raise error(ERROR_TITLE.DataEntryError.value, "problème de connexion au serveur.\nVeuillez réessayer ultérieurement.")
        except error as e:
            PopUp(title=str(e.title), message=str(e.message), icon=QMessageBox.Critical)


    def Login(self, List: list, create=False):
        email = List[0]
        password = List[1]

        try:
            # Vérifier que tous les champs sont remplis
            check_all_fields_filled(List)

            # Vérifier le format de l'email
            check_email_format(email)

            self.MySQLConnector.set_user(email.lower())
            self.MySQLConnector.set_password(password)
            self.MySQLConnector.set_authentification(True)
            if not self.MySQLConnector.connect() or (self.FileManager.check_file_existence(file_path=self.FileManager.central_path+"/Users/"+(email.lower())+'.log') and self.EncryptionManager.compare_hash(password,self.FileManager.read_file(file_path=self.FileManager.central_path + "/Users/" +(email.lower())+'.log', mode='r')[0])):
                # configuration Incription depuis la database
                if create:
                    Result = self.MySQLConnector.execute_query("SELECT get_user_encryption_key()")
                    if Result:
                        raise error(ERROR_TITLE.AccountRecoveryError.value, "Échec lors de la recuperation du compte")

                    if not self.FileManager.init_directory():
                        raise error("Erreur lors de la creation des fichiers", icon_type="warning")
                    
                    self.EncryptionManager.set_key(self.EncryptionManager.primary_key)
                    self.FileManager.write_file(file_path=self.FileManager.central_path + "/Acces/Encryptionkey.log",
                                            lines=[(self.EncryptionManager.encrypt_key(self.EncryptionManager.Decode(Result[0][0]))),], mode='w')

                # :::::::::::::::::: Configuration normal ::::::::::::::::::::::::::::::::::::
                if self.WindowManager.current_window.checkbox.isChecked():
                    self.FileManager.write_file(file_path=self.FileManager.central_path + "/Users/" + email.lower() + '.log',
                                            lines=[(self.EncryptionManager.hash_element(password)), ], mode='w')
                UserManager.email = email.lower()
                UserManager.password = password
                self.WindowManager.setCurrentIndex(3)
                self.WindowManager.current_window.sidebar.logOut.clicked.connect(lambda: self.Deconnexion())

            elif not self.InternetManager.isInternetAcces() and not self.InternetManager.isWifiConnected():
                raise error(ERROR_TITLE.InternetConnectionError.value ,"Aucune connexion Internet détectée.")

            else:
                raise error(ERROR_TITLE.DataEntryError.value ,"Adresse email ou mot de passe incorrect.\n Veuillez réessayer.")
        except error as e:
            PopUp(title=str(e.title), message=str(e.message), icon=QMessageBox.Critical)


    def Inscription_from_old_user(self):
        self.WindowManager.setCurrentIndex(1)
        self.WindowManager.current_window.button.clicked.connect(lambda: self.Login(
            self.WindowManager.current_window.dataList, True))
        

    def chooseConnection(self):
        if self.FileManager.check_directory_existence(self.FileManager.central_path):
            self.WindowManager.setCurrentIndex(1)
            # self.WindowManager.current_window.forgot_label.mousePressEvent = lambda event: Forgot_pwd()
            self.WindowManager.current_window.button.clicked.connect(lambda: self.Login(
            self.WindowManager.current_window.dataList))
        else:
            self.WindowManager.setCurrentIndex(2)
            self.WindowManager.current_window.textButton.clicked.connect(lambda: self.Inscription_from_old_user()) 
            self.WindowManager.current_window.button.clicked.connect(lambda: self.Inscription_from_new_user(
            self.WindowManager.current_window.dataList))
        self.timer.stop()


"""
MySQLConnector = MySQLConnector('localhost', 'genius_database', 'root', '')
EncryptionManager = EncryptionManager()
choose_connection = QTimer()
InternetManager = InternetManager()
WindowManager = WindowManager()
FileManager = FileManager()


def Deconnexion():
    dialog = closeApp(deconnection=True)
    if dialog.exec():
        dialog.accept()
        WindowManager.setCurrentIndex(1)
        WindowManager.current_window.Push_button.clicked.connect(lambda: Login(
            WindowManager.current_window.dataList))
        # WindowManager.current_window.forgot_label.mousePressEvent = lambda event: Forgot_pwd()


def Inscription_from_new_user(List: list):
    surname = List[0]
    name = List[1]
    email = List[2]
    number = List[3]
    password = List[4] 
    conf_pwd = List[5]


    #generer les clés de chiffrement
    key = EncryptionManager.generate_key()

    try:
        # Vérifier que tous les champs sont remplis
        check_all_fields_filled(List)

        # Vérifier le format de l'email
        check_email_format(email)

        # Vérifier le format du numéro de téléphone (par exemple, uniquement chiffres)
        check_phone_format(number)

        # Vérifier que les mots de passe correspondent
        check_passwords_match(password, conf_pwd)

        # Vérifier que la taille du mot de passe est supérieure à 6 caractères
        check_password_length(password)

        # Vérifier que le mot de passe est différent du nom
        check_password_differs_from_name(password, name)

        # Vérifier que le mot de passe contient au moins une majuscule, une lettre et un chiffre
        check_password_complexity(password)

        if not MySQLConnector.connect():
            Result = MySQLConnector.execute_procedure('new_user',
                            ((name+' '+surname), password, email.lower(), number, EncryptionManager.Encode(EncryptionManager.key), EncryptionManager.Encode(key)))
            if Result:
                raise error(ERROR_TITLE.InscriptionError.value, "Échec lors de l'inscription")
            else:
                if FileManager.init_directory():
                    FileManager.write_file(file_path=FileManager.central_path + "/Users/" + email.lower() + '.log',
                                        lines=[(EncryptionManager.hash_element(password)), ], mode='w')
                    EncryptionManager.set_key(EncryptionManager.primary_key)
                    FileManager.write_file(file_path=FileManager.central_path + "/Acces/Encryptionkey.log",
                                        lines=[(EncryptionManager.encrypt_key(EncryptionManager.key)), ], mode='w')
                    # fin et sortie
                    PopUp("Succes" ,"Inscription réussie", QMessageBox.Information)
                    UserManager.email = email.lower()
                    UserManager.password = password
                    WindowManager.setCurrentIndex(3)
                    WindowManager.current_window.sidebar.logOut.clicked.connect(lambda: Deconnexion())
                else:
                    raise error(ERROR_TITLE.FileSystemError.value, "Échec de la création des fichiers en \nraison d'une erreur du système de fichiers. \nVeuillez réessayer ou contacter le support technique.")
        else:
            raise error(ERROR_TITLE.DataEntryError.value, "problème de connexion au serveur.\nVeuillez réessayer ultérieurement.")
    except error as e:
        PopUp(title=str(e.title), message=str(e.message), icon=QMessageBox.Critical)


# Fonction pour pouvoir acceder a son appli
def Login(List: list, create=False):

    email = List[0]
    password = List[1]

    try:
        # Vérifier que tous les champs sont remplis
        check_all_fields_filled(List)

        # Vérifier le format de l'email
        check_email_format(email)

        MySQLConnector.set_user(email.lower())
        MySQLConnector.set_password(password)
        MySQLConnector.set_authentification(True)
        if not MySQLConnector.connect() or (FileManager.check_file_existence(file_path=FileManager.central_path+"/Users/"+(email.lower())+'.log') and EncryptionManager.compare_hash(password,FileManager.read_file(file_path=FileManager.central_path + "/Users/" +(email.lower())+'.log', mode='r')[0])):
            # configuration Incription depuis la database
            if create:
                Result = MySQLConnector.execute_query("SELECT get_user_encryption_key()")
                if Result:
                    raise error(ERROR_TITLE.AccountRecoveryError.value, "Échec lors de la recuperation du compte")

                if not FileManager.init_directory():
                    raise error("Erreur lors de la creation des fichiers", icon_type="warning")
                
                EncryptionManager.set_key(EncryptionManager.primary_key)
                FileManager.write_file(file_path=FileManager.central_path + "/Acces/Encryptionkey.log",
                                        lines=[(EncryptionManager.encrypt_key(EncryptionManager.Decode(Result[0][0]))),], mode='w')

            # :::::::::::::::::: Configuration normal ::::::::::::::::::::::::::::::::::::
            if WindowManager.current_window.checkbox.isChecked():
                FileManager.write_file(file_path=FileManager.central_path + "/Users/" + email.lower() + '.log',
                                        lines=[(EncryptionManager.hash_element(password)), ], mode='w')
            UserManager.email = email.lower()
            UserManager.password = password
            WindowManager.setCurrentIndex(3)
            WindowManager.current_window.sidebar.logOut.clicked.connect(lambda: Deconnexion())

        elif not InternetManager.isInternetAcces() and not InternetManager.isWifiConnected():
            raise error(ERROR_TITLE.InternetConnectionError.value ,"Aucune connexion Internet détectée.")

        else:
            raise error(ERROR_TITLE.DataEntryError.value ,"Adresse email ou mot de passe incorrect.\n Veuillez réessayer.")
    except error as e:
        PopUp(title=str(e.title), message=str(e.message), icon=QMessageBox.Critical)


def Inscription_from_old_user():
    WindowManager.setCurrentIndex(1)
    WindowManager.current_window.button.clicked.connect(lambda: Login(
        WindowManager.current_window.dataList, True))
    # WindowManager.current_window.forgot_label.mousePressEvent = lambda event: Forgot_pwd()


# Fonction de démarrage
def chooseConnection():
    if FileManager.check_directory_existence(FileManager.central_path):
        WindowManager.setCurrentIndex(1)
        # WindowManager.current_window.forgot_label.mousePressEvent = lambda event: Forgot_pwd()
        WindowManager.current_window.button.clicked.connect(lambda: Login(
        WindowManager.current_window.dataList))
    else:
        WindowManager.setCurrentIndex(2)
        WindowManager.current_window.textButton.clicked.connect(lambda: Inscription_from_old_user()) 
        WindowManager.current_window.button.clicked.connect(lambda: Inscription_from_new_user(
        WindowManager.current_window.dataList))
    choose_connection.stop()
"""