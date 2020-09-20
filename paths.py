import os

def read_lib_path(file_path):
    f = open(file_path,'r')
    libs_path = f.readline()
    f.close()
    return libs_path

root = os.path.dirname(os.path.abspath(__file__))
file_with_library_path = root +'\\Tools\\pathToLibraryFile.txt'




libs_path = ""
libs_list = ""

project_dir = './'
target_dir_name = 'lib'
target_dir = f'{project_dir}/{target_dir_name}'


def get_libs_path():
  return libs_path

def get_libs():
  return libs_list

def read_libraries():
  global libs_path
  global libs_list
  libs_path = read_lib_path(file_with_library_path)
  libs_list = os.listdir(libs_path)
  


def is_target_dir_exists():
    if target_dir_name in os.listdir(project_dir): return True
    return False
