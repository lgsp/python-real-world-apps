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

source_file = input("Enter the source file name: ")
source = p + '/{sf}'.format(sf = source_file)

direction = "destination"
p = choose_path(direction)

destination_file = input("Enter the destination file: ")
destination = p + '/{df}'.format(df = destination_file)

shutil.move(source, destination)
