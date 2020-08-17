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

if __name__ == '__main__':
    print_title()
    commands_init()
    cli()