import argparse
import requests
import sys
import time
import progressbar
import platform
import os

Sayan = "\033[1;36;40m"
Normal = "\033[0;0m"
Red = "\033[0;31;40m"
Yellow = "\033[1;33;40m"

 # ------ RESULTS Template -------

MAIN = "├──"
TEE2 = "└──"
SPACE_PREFIX = "   "

 # ------ CHECK FOR OPERATION SYSTEM FOR BETTER USAGE -------

operating = platform.system()
if "Linux" in operating:
    def BannerShow():
        print(f'''

 \ \    / /       |__ \|  __ \(_)     
  \ \  / /__   ___   ) | |  | |_ _ __ 
   \ \/ / _ \ / _ \ / /| |  | | | '__|
    \  / (_) | (_) / /_| |__| | | |   
     \/ \___/ \___/____|_____/|_|_|
                {Sayan}A{Normal}d{Yellow}k{Normal}a{Sayan}l{Normal}i, Version 1.1
''')

elif "Win" in operating:
    def BannerShow():
        print('''

 \ \    / /       |__ \|  __ \(_)     
  \ \  / /__   ___   ) | |  | |_ _ __ 
   \ \/ / _ \ / _ \ / /| |  | | | '__|
    \  / (_) | (_) / /_| |__| | | |   
     \/ \___/ \___/____|_____/|_|_|
                Adkali, Version 1.1
''')


BannerShow()


# ------- Manually error message for args -------

def Parser_Err(msg):
    print("Wrong Syntax! use --help flag for more help.")
    print(f"{Yellow}Basic usage:{Normal} Python3 Voo2dir.py -Url [Example-Site] -Word [WordFile]\nUse '-help' for more information.")
    exit()

parser = argparse.ArgumentParser()
parser.error = Parser_Err
parser.add_argument('-Url', type=str, action="store", required=True, help='Host URL, Make Sure You Insert It Properly.')
parser.add_argument('-Word', type=str, action="store",  required=True, help="Wordlist Path.")
parser.add_argument('-ex', type=str, required=False, help='Add extension to the path [ php,zip,html,rar,txt]')
args = parser.parse_args()

# ------- ERROR MESSAGE -------

def msg_err(err):
    print(f"{err}")
    exit(0)

# ------- JUST A NICE LOADING BAR -------

progress = progressbar.ProgressBar()
for i in progress(range(80)):
    time.sleep(0.01)

# ------- ARGS TO BE DEFINED -------

URL = args.Url
Word = args.Word
ex = args.ex

# ------- CODE EXECUTION -------

try:
    with open(args.Word, "r") as directories:
        req = requests.get(f"{args.Url}")
        if req.status_code == 200:
            print(f"\n\033[1;33m{MAIN}Successful HTTP request!\033[m")
            time.sleep(1)
            print(f"\n{Yellow}{SPACE_PREFIX}{TEE2}Path Loaded{Normal} - > {args.Word}")
            time.sleep(1)
        if args.ex:
            if ex == "rar" or ex == "php" or ex == "html" or ex == "zip" or ex == "txt":
                for i in directories:
                    read = directories.read()
                    word = read.split("\n")
                    print(f"{Yellow}{SPACE_PREFIX}{TEE2}Words Loaded{Normal} - >", len(word))
                    time.sleep(2)
                    print(f"{Yellow}{SPACE_PREFIX}{TEE2}Extension:{Normal} {ex}\n")
                    time.sleep(1)
            else:
                msg_err(err=f"{Red}[ERROR[!]]{Normal} ---- > Choose only between rar, php, html, zip, txt < ----- ")
                time.sleep(2)
        else:
            for i in directories:
                read = directories.read()
                word = read.split("\n")
                print(f"{Yellow}{SPACE_PREFIX}{TEE2}Words Loaded{Normal} - >", len(word))
                time.sleep(2)
                print(f"{Yellow}{SPACE_PREFIX}{TEE2}Continue without any specified extension.....{Normal}\n")
                time.sleep(3)
                pass

    with open(args.Word, "r") as directories:
        req = requests.get(f"{args.Url}")
        if req.status_code == 200:
            print(f"{TEE2}Starting Brute-Force Directories, Please Wait!\n")
            time.sleep(0.1)
            if args.ex:
                for i in directories:
                    Newline = i.strip()
                    req = requests.get(f"{args.Url}{Newline}.{ex}")
                    if "Linux" in operating:
                        if req.status_code == 200:
                            print(f"{Sayan}The Path{Normal} - > {Red}{args.Url}{Newline}.{ex}{Normal} {Sayan}Has Been Found!{Normal} -- > [!] Status: {req.status_code}")
                        else:
                            pass
                    elif "Win" in operating:
                        if req.status_code == 200:
                            print(f"The Path - > {args.Url}{Newline}.{ex} Has Been Found! -- > [!] Status: {req.status_code}")
                        else:
                            pass

            else:
                for i in directories:
                    Newline = i.strip()
                    req = requests.get(f"{args.Url}{Newline}.{ex}")
                    if "Linux" in operating:
                        if req.status_code == 200:
                            print(f"{Sayan}The Path{Normal} - > {Red}{args.Url}{Newline}{Normal} {Sayan}Has Been Found!{Normal} -- > [!] Status: {req.status_code}")

                        else:
                            pass
                    elif "Win" in operating:
                        if req.status_code == 200:
                            print(f"The Path - > {args.Url}{Newline} Has Been Found! -- > [!] Status: {req.status_code}")
                        else:
                            pass

        elif req.status_code == 404:
            print("Error! Seems like The requested resource could not be found.")
        elif req.status_code == 403:
            print("403 - Forbidden.")
        elif req.status_code == 503:
            print("Service Unavailable!")
        elif req.status_code == 504:
            print("Timeout server error")
        elif req.status_code == 408:
            print("Time Out!")
except FileNotFoundError as e:
    print("\nNo such file, try put all the path to the file.\n Example: */home/user/Desktop/file.txt")
except KeyboardInterrupt as e:
    print("\nUser stopped the script, exit...")
except requests.exceptions.InvalidURL:
    print("Invalid URL! use 'http://' OR 'https://' with using '/' at the end. Example: http://10.0.5.6/")
except requests.exceptions.ConnectionError:
    print("Invalid URL! use 'http://' OR 'https://' with using '/' at the end. Example: http://10.0.5.6/")
