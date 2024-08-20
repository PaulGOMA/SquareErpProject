import sys
sys.path.append("..")

from mysql.connector import Error
import mysql.connector
import threading

class MySQLConnector:
    def __init__(self, host, database, user, password, authif=False, ssl_ca=None, ssl_cert=None, ssl_key=None):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.ssl_ca = ssl_ca
        self.ssl_cert = ssl_cert
        self.ssl_key = ssl_key
        self.authif = authif
        self.connection = None
        self.lock = threading.Lock()

    def connect(self):
        try:
            with self.lock:
                connection_params = {
                    'host': self.host,
                    'database': self.database,
                    'user': self.user,
                    'password': self.password,
                    'raise_on_warnings': True
                }
                if self.ssl_ca and self.ssl_cert and self.ssl_key:
                    connection_params['ssl_ca'] = self.ssl_ca
                    connection_params['ssl_cert'] = self.ssl_cert
                    connection_params['ssl_key'] = self.ssl_key
                    connection_params['ssl_verify_identity'] = True
                if self.authif:
                    connection_params['auth_plugin'] = 'caching_sha2_password'
                self.connection = mysql.connector.connect(**connection_params)
                if self.connection.is_connected():
                    return None
        except Error as e:
            self.connection = None
            return e

    def disconnect(self):
        if self.connection is not None and self.connection.is_connected():
            self.connection.close()

    def execute_query(self, query, params=None):
        cursor = None
        results = None
        try:
            with self.lock:
                if self.connection is None or not self.connection.is_connected():
                    self.connect()
                cursor = self.connection.cursor(dictionary=False)
                cursor.execute(query, params)
                results = cursor.fetchall()
                self.connection.commit()
        except Error as e:
            return e
        finally:
            if cursor:
                cursor.close()
        return results

    def execute_procedure(self, proc_name, params):
        cursor = None
        results = None
        try:
            with self.lock:
                if self.connection is None or not self.connection.is_connected():
                    self.connect()
                cursor = self.connection.cursor()
                cursor.callproc(proc_name, params)
                results = []
                for result in cursor.stored_results():
                    results.extend(result.fetchall())
                self.connection.commit()
        except Error as e:
            return e
        finally:
            if cursor:
                cursor.close()
        return results

    # Methods to update individual parameters
    def set_host(self, host):
        self.host = host

    def set_database(self, database):
        self.database = database

    def set_user(self, user):
        self.user = user

    def set_password(self, password):
        self.password = password

    def set_ssl_ca(self, ssl_ca):
        self.ssl_ca = ssl_ca

    def set_ssl_cert(self, ssl_cert):
        self.ssl_cert = ssl_cert

    def set_ssl_key(self, ssl_key):
        self.ssl_key = ssl_key

    def set_authentification(self, authif):
        self.authif = authif