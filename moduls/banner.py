from colorama import Fore,init
init()


class tool:
    def banner(self=None):
        print(f"""{Fore.GREEN}

███████╗██╗████████╗███████╗██╗███╗   ██╗███████╗ ██████╗ 
██╔════╝██║╚══██╔══╝██╔════╝██║████╗  ██║██╔════╝██╔═══██╗
███████╗██║   ██║   █████╗  ██║██╔██╗ ██║█████╗  ██║   ██║
╚════██║██║   ██║   ██╔══╝  ██║██║╚██╗██║██╔══╝  ██║   ██║
███████║██║   ██║   ███████╗██║██║ ╚████║██║     ╚██████╔╝
╚══════╝╚═╝   ╚═╝   ╚══════╝╚═╝╚═╝  ╚═══╝╚═╝      ╚═════╝ 
                                                          
                {Fore.RED}

            **************************************
            *    Coded By : Masoud Shakarami     *
            *    Telegram : @hacker_1one         *
            *    Instagram : @pentest112         *
            **************************************
        {Fore.RESET}""")

    def options(self=None):
        print(f"""
        options:
        
        {Fore.RED}[ {Fore.LIGHTGREEN_EX}01 {Fore.RED}] {Fore.WHITE} Domain whois Lookup
        {Fore.RED}[ {Fore.LIGHTGREEN_EX}02 {Fore.RED}] {Fore.WHITE} Dns Checker
        {Fore.RED}[ {Fore.LIGHTGREEN_EX}03 {Fore.RED}] {Fore.WHITE} Port Scanner
        {Fore.RED}[ {Fore.LIGHTGREEN_EX}04 {Fore.RED}] {Fore.WHITE} Sub Domain
        {Fore.RED}[ {Fore.LIGHTGREEN_EX}05 {Fore.RED}] {Fore.WHITE} Admin Page Finder
        {Fore.RED}[ {Fore.LIGHTGREEN_EX}06 {Fore.RED}] {Fore.WHITE} site information
        {Fore.RED}[ {Fore.LIGHTGREEN_EX}00 {Fore.RED}] {Fore.WHITE} return to menu
        {Fore.RESET}""")