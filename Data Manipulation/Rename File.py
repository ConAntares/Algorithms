#### Rename File with Ctrl+H

"""
Subfolders are not included
"""

import os

def files():
    file_list = os.listdir()
    return file_list

def renamefile(file_list):
    for filename in file_list:
        if "_" in filename:
            newname = filename.replace("_"," ")
            os.rename(filename,newname)

file_list = files()
renamefile(file_list)
