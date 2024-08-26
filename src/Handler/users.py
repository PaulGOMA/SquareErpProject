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
    def getUsername(self) -> str:
        if self.InternetManager.isInternetAcces() and self.InternetManager.isWifiConnected():
            self.MySQLConnector.set_user(self._email)
            self.MySQLConnector.set_password(self._password)
            try:
                self.MySQLConnector.connect()
                return self.MySQLConnector.execute_query("SELECT getUserName()")[0][0]
            except:
                return 'Accès refusé'
        else:
            return 'Hors ligne'

    def getMessageNotify(self) -> int:
        if self.InternetManager.isInternetAcces() and self.InternetManager.isWifiConnected():
            self.MySQLConnector.set_user(self._email)
            self.MySQLConnector.set_password(self._password)
            try:
                self.MySQLConnector.connect()
                return self.MySQLConnector.execute_query("SELECT Check_notification()")[0][0]
            except:
                return -1
        else:
            return -1

    def getUpdate(self) -> int:
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