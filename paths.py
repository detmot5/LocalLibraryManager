import os

def get_lib_path(file_path):
    f = open(file_path,'r')
    libs_path = f.readline()
    f.close()
    return libs_path

root = os.path.dirname(os.path.abspath(__file__))
file_with_library_path = root +'\\Tools\\pathToLibraryFile.txt'




libs_path = get_lib_path(file_with_library_path)
libs_list = os.listdir(libs_path)

project_dir = './'
target_dir_name = 'lib'
target_dir = f'{project_dir}/{target_dir_name}'




def is_target_dir_exists():
    if target_dir_name in os.listdir(project_dir): return True
    return False
