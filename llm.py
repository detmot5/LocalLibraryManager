import os, click
import texts
from texts import print_title
from texts import console_colors
from paths import libs_path, target_dir
from commands import set_path
from commands import install
from commands import add_new_lib
from commands import list

def get_lib_path(file_path):
    global libs_path
    f = open(file_path,'r')
    libs_path = f.readline()
    f.close()
    return libs_path

os.system("cls")



@click.group()
def cli():
    pass
   


@click.command("install", help='install library in project')
@click.argument('libname')
def install_lib(libname):
    click.echo(f"{console_colors.CYAN}{texts.invoking_install}{console_colors.ENDC}")
    click.echo(install.run_command(libname))

@click.command("set-lib-path", help='set source of libraries')
@click.argument('path')
def set_lib_path(path):
    click.echo(f"{console_colors.CYAN}{texts.invoking_setPath}{console_colors.ENDC}")
    set_path.run_command(file_with_library_path, path)


@click.command("add-lib", help='add new library to llm')
@click.argument('path-to-lib')
def add_lib(path_to_lib):
    add_new_lib.run_command(path_to_lib)



@click.command("list", help='list of libraries')
@click.option("--installed", help='installed libraries', is_flag=True)
def lib_list(installed):
    click.echo(f"{console_colors.CYAN}{texts.invoking_list}{console_colors.ENDC}")
    res = False
    if False == installed:
        click.echo(f"{console_colors.CYAN}Libraries:{console_colors.ENDC}")
        res = list.run_command(libs_path)
    else:
        click.echo(f"{console_colors.CYAN}Installed libraries:{console_colors.ENDC}")
        res = list.run_command(target_dir)
    if False == res:
            click.echo(f"{console_colors.WARNING}No libraries installed.{console_colors.ENDC}"); return



def commands_init():            
    cli.add_command(install_lib)
    cli.add_command(set_lib_path)
    cli.add_command(lib_list)
    cli.add_command(add_lib)

if __name__ == '__main__':
    print_title()
    commands_init()
    cli()