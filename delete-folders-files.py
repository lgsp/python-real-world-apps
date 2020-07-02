import shutil, os
from pathlib import Path

def choose_path(direction):
    global p
    choose_path = input("Do you want to choose your {d} path? (Y|N) ".format(d = direction))
    if choose_path.lower() == 'y':
        p = input("Enter your {d} path: ".format(d = direction))
    elif choose_path.lower() == 'n':
        p = Path.home()
    else:
        return
    return p

direction = "source"
p = choose_path(direction)

file_or_folder = input("Do you want to delete file (I) or folder (O)? ")
if file_or_folder.lower() == 'i':
    f = "file"
elif file_or_folder.lower() == 'o':
    f = "folder"
    
source_f = input("Enter the source {f} name: ".format(f = f))
source = p + '/{sf}'.format(sf = source_f)

shutil.rmtree(source)
