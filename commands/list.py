from os import listdir
from os.path import isdir
from paths import libs_list, is_target_dir_exists

def is_LLM_library(lib):
    if lib in libs_list: return True
    return False



def run_command(dir):
    if not is_target_dir_exists(): return False
    list_dir = listdir(dir)
    if len(list_dir) == 0: return False
    for elem in list_dir:
        if isdir(dir+f'/{elem}') and is_LLM_library(elem): print(elem, sep='\n')
    return True

