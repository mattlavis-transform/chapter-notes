import os
from dotenv import load_dotenv
import glob

from classes.substitute import Substitute

class Application(object):
    def __init__(self):
        load_dotenv('.env')
        self.folder_from = os.getenv('FOLDER_FROM')
        self.folder_to = os.getenv('FOLDER_TO')
        self.files = []

    def insert_hyperlinks(self):
        for filename in glob.iglob(f'{self.folder_from}/*.md'):
            parts = filename.split("/")
            filename = parts[len(parts) - 1]
            self.files.append(filename)

        self.files = sorted(self.files)
        for file_in in self.files:
            file_in_path = os.path.join(self.folder_from, file_in)
            file_out_path = os.path.join(self.folder_to, file_in)
            f = open(file_in_path, "r")
            data = f.read()
            sub = Substitute(data)
            data_out = sub.substitute()
            f.close()

            f = open(file_out_path, "w")
            f.write(data_out)
            f.close()
