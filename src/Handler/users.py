import sys
sys.path.append("..")

from Handler.internet import InternetManager
from Handler.databaseConnector import MySQLConnector

# ::::::::::::::::::::::::::::::: class pour la gestion du user en cours ::::::::::::::::::::::::::::::::::::::::
class UsersManager:
    def __init__(self):
        self._email = None
        self._password = None
        self.InternetManager = InternetManager()
        self.MySQLConnector = MySQLConnector('localhost', 'genius_database',self._email, self._password)
        self.MySQLConnector.set_authentification(True)

# ::::::::::::::::::::::::::: Gestion Users :::::::::::::::::::::::::::::::::::::::::::::::::::::::
    def get_user_name(self) -> str:
        if self.InternetManager.is_internet_accès() and self.InternetManager.is_wifi_connected():
            self.MySQLConnector.set_user(self._email)
            self.MySQLConnector.set_password(self._password)
            try:
                self.MySQLConnector.connect()
                return self.MySQLConnector.execute_query("SELECT get_user_name()")[0][0]
            except:
                return 'Accès refusé'
        else:
            return 'Hors ligne'

    def get_message_notify(self) -> int:
        if self.InternetManager.is_internet_accès() and self.InternetManager.is_wifi_connected():
            self.MySQLConnector.set_user(self._email)
            self.MySQLConnector.set_password(self._password)
            try:
                self.MySQLConnector.connect()
                return self.MySQLConnector.execute_query("SELECT Check_notification()")[0][0]
            except:
                return -1
        else:
            return -1

    def get_update(self) -> int:
        print(1)
        return 1

# ::::::::::::::::::::::::::: Accesseur :::::::::::::::::::::::::::::::::::::::::::::::::::::::
    @property
    def email(self):
        return self._email

    @property
    def password(self):
        return self._password

    @email.setter
    def email(self, value):
        self._email = value

    @password.setter
    def password(self, value):
        self._password = value

# ::::::::::::::::::::: Varible à utilisation global ::::::::::::::::::::::::::::::::::::::::::
UserManager = UsersManager()