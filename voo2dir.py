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

# Check if Windows or Linux for better usage the script //
operating = platform.system()
if "Linux" in operating:
    def BannerShow():
        print(f'''

 \ \    / /       |__ \|  __ \(_)     
  \ \  / /__   ___   ) | |  | |_ _ __ 
   \ \/ / _ \ / _ \ / /| |  | | | '__|
    \  / (_) | (_) / /_| |__| | | |   
     \/ \___/ \___/____|_____/|_|_|
                    {Sayan}A{Normal}d{Yellow}k{Normal}a{Sayan}l{Normal}i
'''         )

elif "Win" in operating:
    def BannerShow():
        print('''

 \ \    / /       |__ \|  __ \(_)     
  \ \  / /__   ___   ) | |  | |_ _ __ 
   \ \/ / _ \ / _ \ / /| |  | | | '__|
    \  / (_) | (_) / /_| |__| | | |   
     \/ \___/ \___/____|_____/|_|_|
                    Adkali
'''         )
        
parser = argparse.ArgumentParser()
parser.add_argument('-Url', type=str, required=True, help='Host URL, Make Sure You Insert It Properly.')
parser.add_argument('-Word', type=str, required=True, help="Wordlist Path.")
parser.add_argument('-v', type=str, required=False, help="voo2dir, Version 1.0 Made By Adkali With Love.")
args = parser.parse_args()
print("\n")
BannerShow()


progress = progressbar.ProgressBar()
for i in progress(range(80)):
    time.sleep(0.01)
           

try:
    with open(args.Word, "r") as directories:
        req = requests.get(f"{args.Url}")
        if req.status_code == 200:
            print("Successful HTTP requests!")
            time.sleep(1)
            print("Path Loaded - >", (args.Word),"")
            time.sleep(1)
            for i in directories:
                read = directories.read()
                word = read.split("\n")
                print("Words Loaded - >", len(word))
                time.sleep(1)
    with open(args.Word, "r") as directories:
        req = requests.get(f"{args.Url}")
        if req.status_code == 200:
            print("Starting Brute-Force Directories, Please Wait!\n")
            time.sleep(0.1)
            for j in directories:
                Newline = j.strip()
                req = requests.get(f"{args.Url}{Newline}")
                if "Linux" in operating:
                    if req.status_code == 200:
                        print(f"{Sayan}The Path{Normal} - > {Red}{args.Url}{Newline}{Normal} {Sayan}Has Been Found!{Normal} -- > [!] Status: {req.status_code}")
                elif "Win" in operating:
                    if req.status_code == 200:
                        print(f"The Path - > {args.Url}{Newline} Has Been Found! -- > [!] Status: {req.status_code}")
                else:
                    continue
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
    print("Invalid URL! use http:// OR https://, by using / at the end. Example: http://10.0.5.6/")
except requests.exceptions.ConnectionError:
    print("Invalid URL! use http:// OR https://, by using / at the end. Example: http://10.0.5.6/")
