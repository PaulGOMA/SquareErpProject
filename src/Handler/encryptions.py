import sys
sys.path.append("..")

import os
import base64
from cryptography.hazmat.primitives import hashes, padding as sym_padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

class EncryptionManager:
    def __init__(self, key=None):
        self.backend = default_backend()
        self.primary_key = b'rI+\x0b\x1a\xc1\x98a\xf1\rz9\xdf\r\x04\xdb\xb9D\x83X\xf9\x05\xf3\xef\x18\x91\xd4\x8d\xbe-\x06\x06'
        if key is None:
            self.key = self.generate_key()
        else:
            self.key = key

    def set_key(self, new_key):
        self.key = new_key

    @staticmethod
    def generate_key():
        return os.urandom(32)

    def encrypt_element(self, element):
        iv = os.urandom(16)
        cipher = Cipher(algorithms.AES(self.key), modes.CBC(iv), backend=self.backend)
        encryptor = cipher.encryptor()
        padder = sym_padding.PKCS7(algorithms.AES.block_size).padder()
        padded_data = padder.update(element.encode()) + padder.finalize()
        encrypted_element = encryptor.update(padded_data) + encryptor.finalize()
        return base64.urlsafe_b64encode(iv + encrypted_element).decode()

    def decrypt_element(self, encrypted_element):
        encrypted_element = base64.urlsafe_b64decode(encrypted_element)
        iv = encrypted_element[:16]
        encrypted_data = encrypted_element[16:]
        cipher = Cipher(algorithms.AES(self.key), modes.CBC(iv), backend=self.backend)
        decryptor = cipher.decryptor()
        padded_data = decryptor.update(encrypted_data) + decryptor.finalize()
        unpadder = sym_padding.PKCS7(algorithms.AES.block_size).unpadder()
        decrypted_element = unpadder.update(padded_data) + unpadder.finalize()
        return decrypted_element.decode()

    def encrypt_key(self, key):
        key_b64 = base64.urlsafe_b64encode(key).decode('utf-8')
        return self.encrypt_element(key_b64)

    def decrypt_key(self, encrypted_key):
        decrypted_key_b64 = self.decrypt_element(encrypted_key)
        return base64.urlsafe_b64decode(decrypted_key_b64)

    def Encode(self, key):
        return base64.urlsafe_b64encode(key)

    def Decode(self, key):
        return base64.urlsafe_b64decode(key)

    @staticmethod
    def hash_element(element):
        if isinstance(element, str):
            element = element.encode()
        hasher = hashes.Hash(hashes.SHA3_512(), backend=default_backend())
        hasher.update(element)
        hashed_element = hasher.finalize()
        return base64.urlsafe_b64encode(hashed_element).decode()

    @staticmethod
    def compare_hash(element, hashed_element):
        return EncryptionManager.hash_element(element) == hashed_element

