import socket
from colorama import init,Fore
from .port_list import ports
init()

class PortScanner:
    def __init__(self,ip):
        self.ip=ip

    def port_scanner(self,ip,sport,eport):
        
        print(f"""{Fore.GREEN}
-------------------------------
 Target Ip : {ip}
-------------------------------        
        """)
        try:
            for port in range(int(sport),int(eport)+1):
                s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                res = s.connect_ex((ip,port))
                if res == 0:
                    port_name=ports[port]
                    print(f"[+] {ip}:{port}\TCP  Port {port}\{port_name} is Open !")
        except KeyboardInterrupt:
            print("scan cancelled")
        except socket.gaierror:
            print("server not responding")