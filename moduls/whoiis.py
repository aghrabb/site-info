from ipwhois import IPWhois
import whois,socket

class Information:
    def __init__(self,domain):
        self.domain=domain

    def get_ip(self,domain):
        return socket.gethostbyname(domain)

    def domain_info(self):
        return whois.whois(self.domain)

    def server_info(self,domain):
        Ip = Information.get_ip(self=None,domain=domain)
        info = IPWhois(Ip)
        info = info.lookup_whois()
        return info