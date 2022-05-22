import os
import sys
import glob

from classes.substitute import Substitute


folder_from = "/Users/mattlavis/sites and projects/1. Online Tariff/ott prototype/app/content/hs22/section_chapter_notes"
folder_to = "/Users/mattlavis/sites and projects/1. Online Tariff/ott prototype/app/content/hs22/section_chapter_notes/working"
files = []
for filename in glob.iglob(f'{folder_from}/*.md'):
    parts = filename.split("/")
    filename = parts[len(parts) - 1]
    files.append(filename)
    # print(filename)

files = sorted(files)
for file_in in files:
    file_in_path = os.path.join(folder_from, file_in)
    file_out_path = os.path.join(folder_to, file_in)
    f = open(file_in_path, "r")
    data = f.read()
    sub = Substitute(data)
    data_out = sub.substitute()
    f.close()

    f = open(file_out_path, "w")
    f.write(data_out)
    f.close()
