import os, sys
from shutil import copytree
from enum import Enum
from texts import console_colors
from paths import libs_path, libs_list, target_dir, is_target_dir_exists

cmdTitle = 'Install'

class Install_Status(Enum):
    success = 'Library installed succesfully'
    lib_not_found = 'Library not found in given location'
    already_installed = 'Library is already installed in this project' 





def print_install_info(libname):
    print(f"Installing {libname}...")

def check_lib(libname):
    print(f"{console_colors.OKGREEN}{cmdTitle}: Looking for library: {libname} in {libs_path}{console_colors.ENDC}")
    if libname not in libs_list:                  
        return Install_Status.lib_not_found

    print(f"{console_colors.OKGREEN}{cmdTitle}: Checking the project/{target_dir} folder{console_colors.ENDC}")
    if libname in os.listdir(target_dir): 
        return Install_Status.already_installed
    
    return Install_Status.success


def install_lib(libname):
    print(is_target_dir_exists())
    if not is_target_dir_exists(): os.mkdir('lib')

    src_lib_dir = f"{libs_path}/{libname}"
    target_lib_dir = f"./{target_dir}/{libname}"
    
    status = check_lib(libname)
    if(Install_Status.success != status): return status

    copytree(src_lib_dir, target_lib_dir)
    

    return Install_Status.success
    

# externally called functions


def run_command(libname):
    status = install_lib(libname)
    if(status == Install_Status.success): color = console_colors.OKGREEN
    else: color = console_colors.FAIL
    
    return f"\n{color}{console_colors.UNDERLINE}{status.value}{console_colors.ENDC}"



