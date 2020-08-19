import os, shutil
from enum import Enum
from paths import libs_path, target_dir, project_dir, is_target_dir_exists
from texts import console_colors

class DeleteStatus(Enum):
    lib_folder_not_exists = "Lib folder doensn't exists"
    lib_not_installed = 'Library is not installed in project'
    success = 'Deleted succesfully'
def error():
    print('error')


def delete(libname):
    if not is_target_dir_exists(): DeleteStatus.lib_folder_not_exists
    if libname not in os.listdir(target_dir): return DeleteStatus.lib_not_installed
    path = f'{target_dir}/{libname}'
    shutil.rmtree(path, onerror=error)
    return DeleteStatus.success


def run_command(libname):
    status = delete(libname)
    if DeleteStatus.success == status: print(f"{console_colors.OKGREEN}{status.value} {libname}{console_colors.ENDC}")
    else: print(f"{console_colors.FAIL}{status.value}{console_colors.ENDC}")




