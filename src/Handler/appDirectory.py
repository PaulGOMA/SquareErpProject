import sys 
sys.path.append("..")

import os
import shutil
import subprocess

class FileManager:
    def __init__(self, central_path="C:/SquareERP", default_path="../Certificats"):
        self.central_path = central_path
        self.default_path = default_path

    def lock_file(self, path):
        os.chmod(path, 0o000)

    def unlock_file(self, path):
        os.chmod(path, 0o600)

    def hide_file(self, path):
        os.system("attrib +h " + path)

    def unhide_file(self, path):
        os.system("attrib -h " + path)

    def check_file_existence(self, file_path):
        self.unhide_file(file_path)
        return os.path.exists(file_path)

    def delete_file(self, file_path):
        if self.check_file_existence(file_path):
            os.remove(file_path)

    def create_directory(self, dir_path):
        if not self.check_directory_existence(dir_path):
            os.makedirs(dir_path)

    def check_directory_existence(self, dir_path):
        return os.path.isdir(dir_path)

    def delete_directory(self, dir_path):
        if self.check_directory_existence(dir_path):
            shutil.rmtree(dir_path)

    def lock_directory(self, dir_path):
        if os.path.isdir(dir_path):
            os.chmod(dir_path, 0o000)
            for root, dirs, files in os.walk(dir_path):
                for d in dirs:
                    os.chmod(os.path.join(root, d), 0o000)
                for f in files:
                    os.chmod(os.path.join(root, f), 0o000)

    def unlock_directory(self, dir_path):
        if os.path.isdir(dir_path):
            os.chmod(dir_path, 0o700)
            for root, dirs, files in os.walk(dir_path):
                for d in dirs:
                    os.chmod(os.path.join(root, d), 0o700)
                for f in files:
                    os.chmod(os.path.join(root, f), 0o600)

    def move_file(self, src_path, dest_path):
        if self.check_file_existence(src_path):
            shutil.move(src_path, dest_path)

    def move_directory(self, src_path, dest_path):
        if self.check_directory_existence(src_path):
            shutil.move(src_path, dest_path)

    def get_file_size(self, file_path):
        # Vérifier si le chemin correspond à un fichier
        if os.path.isfile(file_path):
            size = os.path.getsize(file_path)
            return round(size / (1024 ** 3), 4)  # Convertir en Go et arrondir
        else:
            return None  # Le chemin ne correspond pas à un fichier

    def get_folder_size(self, folder_path):
        # Vérifier si le chemin correspond à un dossier
        if os.path.isdir(folder_path):
            # Parcourir tous les fichiers du dossier et ajouter leur taille
            size = 0
            for root, dirs, files in os.walk(folder_path):
                size += sum([os.path.getsize(os.path.join(root, f)) for f in files])
            return round(size / (1024 ** 3), 4)  # Convertir en Go et arrondir
        else:
            return None  # Le chemin ne correspond pas à un dossier

    def list_files_in_directory(self, dir_path):
        if os.path.isdir(dir_path):
            return [f for f in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, f))]
        else:
            return []

    def write_file(self, file_path, lines, mode='wb'):
        with open(file_path, mode) as file:
            for line in lines:
                file.write(line + '\n')

    def read_file(self, file_path, mode='rb'):
        if self.check_file_existence(file_path):
            with open(file_path, mode) as file:
                return [line.strip() for line in file.readlines()]
        return []
    def init_directory(self):
        try:
            if not self.check_directory_existence(self.central_path):
                self.create_directory(self.central_path)
            if not self.check_directory_existence(self.central_path + "/Users"):
                self.create_directory(self.central_path + "/Users")
            if not self.check_directory_existence(self.central_path + "/Acces"):
                self.create_directory(self.central_path + "/Acces")
            if not self.check_directory_existence(self.central_path + "/Map"):
                self.create_directory(self.central_path + "/Map")
            if not self.check_directory_existence(self.central_path + "/Others"):
                self.create_directory(self.central_path + "/Others")
            if self.check_directory_existence(self.default_path):
                self.move_directory(self.default_path, self.central_path)
        except:
            return False
        finally:
            return True

    def execute_command(self, command):
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        return result.stdout, result.stderr


