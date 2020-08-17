import os, sys
from shutil import copytree
from enum import Enum
from texts import console_colors

lib_path = ''
libs = []
target_dir = 'lib'

cmdTitle = 'Install'

class Install_Status(Enum):
    success = 'Library installed succesfully'
    lib_not_found = 'Library not found in given location'
    already_installed = 'Library is already installed in this project' 





def get_libs():
    global libs, lib_path
    libs = os.listdir(lib_path)

def print_install_info(libname):
    print(f"Installing {libname}...")

def check_lib(libname):
    print(f"{console_colors.OKGREEN}{cmdTitle}: Looking for library: {libname} in {lib_path}{console_colors.ENDC}")

    if libname not in libs:                  return Install_Status.lib_not_found

    print(f"{console_colors.OKGREEN}{cmdTitle}: Checking the project/{target_dir} folder{console_colors.ENDC}")
    if libname in os.listdir(target_dir):    return Install_Status.already_installed
    
    return Install_Status.success


def install_lib(libname):
    src_lib_dir = f"{lib_path}/{libname}"
    target_lib_dir = f"./{target_dir}/{libname}"
    
    
    status = check_lib(libname)
    if(Install_Status.success != status): return status
    if target_dir not in os.listdir('.'): os.mkdir('lib')

    copytree(src_lib_dir, target_lib_dir)
    

    return Install_Status.success
    

# externally called functions
def get_lib_path(file_path):
    global lib_path
    f = open(file_path,'r')
    lib_path = f.readline()
    f.close()
    return lib_path

def run_command(libname):
    get_libs()
    status = install_lib(libname)
    if(status == Install_Status.success): color = console_colors.OKGREEN
    else: color = console_colors.FAIL
    
    return f"{color}{status.value}{console_colors.ENDC}"



