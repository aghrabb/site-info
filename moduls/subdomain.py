import requests,time,sys
from colorama import init,Fore
init()

def sub_domain(domain):
    file = open("moduls/subdomain.txt")
    content = file.read()
    subdomains = content.splitlines()
    count = content.count("\n") + 1
    i = 0
    for subdomain in subdomains:
        url = f"https://{subdomain}.{domain}"

        try:
            requests.get(url)
            i += 1
            time.sleep(1)
        except requests.ConnectionError:
            i += 1
        except KeyboardInterrupt:
            sys.exit()
        except:
            print(f"{Fore.WHITE}(example.com no http://example.com){Fore.RESET}")
            break
        else:
            print(f"{Fore.GREEN}[+] Subdomain : {Fore.RESET} {url}")

