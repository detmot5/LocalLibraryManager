import os, shutil
from paths import libs_path



def run_command(path_to_lib):
    libs_list = os.listdir(libs_path)
    print(libs_path)
    lib_name = os.path.basename(path_to_lib)
    if lib_name not in libs_list:
        shutil.copytree(path_to_lib, f"{libs_path}/{lib_name}")
        return True
    else: return False


