import os
from texts import console_colors


cmdTitle = 'SetPath'

def run_command(path, path_to_library_folder):
    f = open(path, 'w')
    
    message = f"{console_colors.OKGREEN}{cmdTitle}: Setting library source folder to {path_to_library_folder}{console_colors.ENDC}"
    print(message)

    f.write(os.path.abspath(path_to_library_folder))
    f.close()



