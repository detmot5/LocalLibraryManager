import os, click
from texts import print_title
from commands import set_path
from commands import install
os.system("cls")



file_with_library_path = './Tools/pathToLibraryFile.txt'
libs_path = ''







@click.group()
def cli():
    pass
   


@click.command("install")
@click.argument('libname')
def install_lib(libname):
    libs_path = install.get_lib_path(file_with_library_path)
    click.echo(install.run_command(libname))

@click.command("set-lib-path")
@click.argument('path')
def set_lib_path(path):
    set_path.run_command(file_with_library_path, path)


def commands_init():            
    cli.add_command(install_lib)
    cli.add_command(set_lib_path)

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

if __name__ == '__main__':
    print_title()
    commands_init()
    cli()