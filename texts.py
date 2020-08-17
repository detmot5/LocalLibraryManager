title = '***llm - Local Library Manager***'
description = 'Easy management of your local libraries '

invoking_install = 'Invoking: Install command...\n'
invoking_setPath = 'Invoking: Set-path command...\n'
invoking_list = 'Invoking: list command...\n'


class console_colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    CYAN = '\u001b[36m'
    Magenta = '\u001b[35m'





def print_title():
    print(f"{console_colors.HEADER} {console_colors.BOLD}  {title}  {console_colors.ENDC}")
    print(f" {console_colors.OKBLUE}{console_colors.UNDERLINE}{description}{console_colors.ENDC}")
    print()