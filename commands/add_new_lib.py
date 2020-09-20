import os, shutil
from paths import is_target_dir_exists, get_libs, get_libs_path



def run_command(path_to_lib):
    if not is_target_dir_exists(): return False
    lib_name = os.path.basename(path_to_lib)
    if lib_name not in get_libs():
        path = f"{get_libs_path()}\\{lib_name}"
        shutil.copytree(path_to_lib, path)
        return True
    else: return False


