import sys 
sys.path.append("..")

from PySide6.QtWidgets import QMessageBox
from PySide6.QtCore import QTimer

from Utils.enumeration import CLOSING_SESSION_INFORMATION as SESSION
from Utils.checkField import *
from GUI.Components.widgets import PopUp, closeSession
from Handler.appDirectory import FileManager
from Handler.users import UserManager
from Handler.windows import WindowManager
from Handler.internet import InternetManager
from Handler.encryptions import EncryptionManager
from Handler.databaseConnector import MySQLConnector


class SetUp():
    def __init__(self):
        
        self.MySQLConnector = MySQLConnector('localhost', 'genius_database', 'root', '')
        self.EncryptionManager = EncryptionManager()
        self.timer = QTimer()
        self.InternetManager = InternetManager()
        self.WindowManager = WindowManager()
        self.FileManager = FileManager()


    def Deconnexion(self):
        dialog = closeSession(SESSION.Deconnexion)
        if dialog.exec():
            dialog.accept()
            self.WindowManager.setCurrentIndex(1)
            self.WindowManager.current_window.button.clicked.connect(lambda: self.Login(
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
