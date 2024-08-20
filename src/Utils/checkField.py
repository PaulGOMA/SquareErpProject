import sys
import re

sys.path.append("..")

from Utils.errors import DataEntryError

def check_all_fields_filled(li: list):
    if li == [""] * len(li):
        raise DataEntryError("Tous les champs doivent être remplis")


def check_email_format(email):
    email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    if not re.match(email_regex, email):
        raise DataEntryError("L'adresse email n'est pas valide")


def check_phone_format(number):
    number_regex = r"^\+?[0-9]{10,15}$"
    if not re.match(number_regex, number):
        raise DataEntryError("Le numéro de téléphone n'est pas valide")


def check_passwords_match(password, conf_pwd):
    if password != conf_pwd:
        raise DataEntryError("Les mots de passe ne correspondent pas")


def check_password_length(password):
    if len(password) <= 6:
        raise DataEntryError("Le mot de passe doit contenir\n plus de 6 caractères")


def check_password_differs_from_name(password, fName, lName):
    if password == fName or password == lName:
        raise DataEntryError("Le mot de passe doit être différent du nom ou du prenom")


def check_password_complexity(password):
    if not re.search(r'[A-Z]', password) or not re.search(r'[a-z]', password) or not re.search(r'[0-9]', password):
        raise DataEntryError("Le mot de passe doit contenir au moins \nune majuscule, une lettre minuscule \net un chiffre")
