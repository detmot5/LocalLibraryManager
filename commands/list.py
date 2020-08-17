from os import listdir
from os.path import isdir
from paths import libs_list

def is_LLM_library(lib):
    if lib in libs_list: return True
    return False



def run_command(dir):
    list_dir = listdir(dir)
    if len(list_dir) == 0: return False
    for elem in list_dir:
        if isdir(dir+f'/{elem}') and is_LLM_library(elem): print(elem, sep='\n')
    return True

