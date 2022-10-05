import os,sys
from colorama import init,Fore
from moduls import banner,whoiis,ddns,portscanner,subdomain,adminfinder,site_info
from pprint import pprint

init()


while True:
    os.system('cls' or 'clear')

    banner.tool.banner(None)
    banner.tool.options(None)
    try:
        num = input(f"{Fore.RED} [ * ] {Fore.RESET}Enter a number from to list:")
        if num == "1" or num == "01":
            os.system('cls' or 'clear')
            domain = input(f"{Fore.RED} [ {Fore.LIGHTGREEN_EX}** {Fore.RED}] {Fore.RESET}Enter a Domain:")
            whois = whoiis.Information(domain)
            res_domain = whois.domain_info()
            res_server = whois.server_info(domain)
            print(f"{Fore.RED} Result of Domain : {Fore.GREEN}")
            pprint(res_domain)
            print(f"{Fore.RED} \n Result of Server : {Fore.GREEN}")
            pprint(res_server)
            input(f"{Fore.RED}please enter return to menu")
        elif num == "2" or num == "02":
            os.system('cls' or 'clear')
            ddns.Dns_Checker.options(None)
            num = input(f"{Fore.RED} [ {Fore.LIGHTGREEN_EX}** {Fore.RED}] {Fore.RESET}Enter a number from to list:")
            if num == "00":
                continue
            domain = input(f"{Fore.RED} [ {Fore.LIGHTGREEN_EX}** {Fore.RED}] {Fore.RESET}Enter a Domain:")
            Dns = ddns.Dns_Checker(domain)
            if num == "1":
                res = Dns.A_Record(domain)
                print(f"{Fore.GREEN} [+] ip -> {Fore.WHITE} {res}")
                input(f"{Fore.RED}please enter return to menu")
            elif num == "2":
                res = Dns.C_Name(domain)
                print(f"{Fore.GREEN} [+] ip -> {Fore.WHITE} {res}")
                input(f"{Fore.RED}please enter return to menu")
            elif num == "3":
                res = Dns.MX_Record(domain)
                print(f"{Fore.GREEN} Host {res.exchange} {Fore.WHITE} {res.perference}")
                input(f"{Fore.RED}please enter return to menu")
        elif num == "3" or num == "03":
            os.system("cls" or "clear")
            ip = input(f"{Fore.RED} [ {Fore.LIGHTGREEN_EX}** {Fore.RED}] {Fore.RESET}Enter a ip:")
            start_port= input(f"{Fore.RED} [ {Fore.LIGHTGREEN_EX}** {Fore.RED}] {Fore.RESET}Start Port:")
            end_port= input(f"{Fore.RED} [ {Fore.LIGHTGREEN_EX}** {Fore.RED}] {Fore.RESET}End Port:")
            Pscanner=portscanner.PortScanner(ip=ip)
            Pscanner.port_scanner(ip=ip,sport=start_port,eport=end_port)
            input(f"{Fore.RED}please enter return to menu")
        elif num == "4" or num == "04":
            os.system('cls' or 'clear')
            domain = input(f"{Fore.RED} [ {Fore.LIGHTGREEN_EX}** {Fore.RED}] {Fore.RESET}Enter a Domain:")
            subdomain.sub_domain(domain)
            input(f"{Fore.RED}please enter return to menu")
        elif num == "5" or num == "05":
            os.system('cls' or 'clear')
            domain = input(f"{Fore.RED} [ {Fore.LIGHTGREEN_EX}** {Fore.RED}] {Fore.RESET}Enter a Domain(http://example.com):")
            adminfinder.AdminFinder(domain)
            input(f"{Fore.RED}please enter return to menu")
        elif num == "6"  or num == "06":
            os.system('cls' or 'clear')
            domain = input(f"{Fore.RED} [ {Fore.LIGHTGREEN_EX}** {Fore.RED}] {Fore.RESET}Enter a Domain(http://example.com):")
            site_info.SiteInfo(domain)
            input(f"{Fore.RED}please enter return to menu")
    except KeyboardInterrupt:
        sys.exit()
    except Exception as ex:
        print(f"{Fore.RED} Error : {ex}")
        input(f"{Fore.RED}please enter return to menu")
        continue
