import builtwith,sys
from colorama import init,Fore
init()

def SiteInfo(domain):
    result = builtwith.builtwith(domain)

    for res in result:
        try:
            print(f"{Fore.GREEN} {res}",result[res])
        except KeyboardInterrupt:
            sys.exit()
        except:
            print(f"{Fore.WHITE}(example.com no http://example.com){Fore.RESET}")
            break