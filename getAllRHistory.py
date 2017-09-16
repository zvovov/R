#! python3

# Created by Chirag Khatri - zvovov@gmail.com

# Copy all .Rhistory files from the current directory with nested folders
# Location for copied files is a RHISTORY folder in current directory.
# all .RHistory files are renamed acc to their original directory

import os
from pathlib import Path
from shutil import copy2

new_folder_name = 'Rhistory-folder'
curr_dir = Path('.')
rhistory_paths = list(curr_dir.glob('**/.Rhistory'))

# create new folder
if not os.path.exists(new_folder_name):
    os.makedirs(new_folder_name)
    # copy all these .Rhistory files to new locations, while renaming them
    for path in rhistory_paths:
        copy2(str(path), new_folder_name + '/' + '-'.join(path.parts))
else:
    print(new_folder_name, "already exists.")