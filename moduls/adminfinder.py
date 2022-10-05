import sys
import requests
from colorama import init,Fore
init()

def AdminFinder(domain):
    file = open("moduls/adminpagelist.txt")
    content = file.read()
    admins = content.splitlines()
    for admin in admins:
        url = f"{domain}{admin}"
        try:
            respons = requests.get(url)
            if respons.status_code == 200:
                print(f"{Fore.GREEN} {url} is Exsists ----> 200 {Fore.RESET}")
            else:
                print(f"{Fore.RED} {url} Not Found ----> 404 {Fore.RESET}")
        except KeyboardInterrupt:
            sys.exit()
        except:
            print(f"{Fore.WHITE}(http://example.com or https://example.com){Fore.RESET}")
            break
