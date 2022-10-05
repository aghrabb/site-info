import dns.resolver
from colorama import init,Fore
init()

class Dns_Checker:
    def __init__(self,domain):
        self.domain=domain

    def options(self=None):
        print(f"""
        options:
        
        {Fore.RED}[ {Fore.LIGHTGREEN_EX}1 {Fore.RED}] {Fore.WHITE} Dns A Record
        {Fore.RED}[ {Fore.LIGHTGREEN_EX}2 {Fore.RED}] {Fore.WHITE} Dns C Name
        {Fore.RED}[ {Fore.LIGHTGREEN_EX}3 {Fore.RED}] {Fore.WHITE} Dns MX Record
        {Fore.RED}[ {Fore.LIGHTGREEN_EX}00 {Fore.RED}] {Fore.WHITE} return to menu
        {Fore.RESET}""")

    def A_Record(self,domain,type="A"):
        res = dns.resolver.query(self.domain,type)
        for arecord in res:
            return arecord

    def MX_Record(self,domain,type="MX"):
        res = dns.resolver.query(self.domain,type)
        for rdata in res:
            return rdata

    def C_Name(self,domain,type="CNAME"):
        res = dns.resolver.query(self.domain,type)
        for cname in res:
            return cname.target