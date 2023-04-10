import argparse
import logging
import random
import time
import requests
import threading
from pathlib import Path
from typing import List
from urllib.parse import urljoin
from alive_progress import alive_bar

#----------------------------------------------------------
                                                           #
# Made by Adkali                                           #
# A Python-based directory brute-forcing tool              #
# HTTP GET requests to each path                           #
# The tool is designed for educational purposes only       #
# allowing users to discover hidden directories            #
# Using DEBUG/TIME                                         #
#----------------------------------------------------------


# COLOR TO BE DEFINED
Normal = "\033[0;0m"
Red = "\033[0;31;40m"
Yellow = "\033[1;33;40m"
Cyan = "\033[1;36;40m"
Purple = "\033[0;35m"

# SIMPLE BANNER WHEN PROGRAM RUNS
def BannerShow():
    print(f'''

 \ \    / /       |__ \|  __ \(_)     
  \ \  / /__   ___   ) | |  | |_ _ __ 
   \ \/ / _ \ / _ \ / /| |  | | | '__|
    \  / (_) | (_) / /_| |__| | | |   
     \/ \___/ \___/____|_____/|_|_|
                {Cyan}A{Normal}d{Yellow}k{Normal}a{Cyan}l{Normal}i, Version 2.0
''')


BannerShow()

# MAKE LIKE A NICE TREE WHEN PROGRAMS RUNS
MAIN = "├──"
TEE2 = "└──"
SPACE_PREFIX = "   "

# Define a list of user agent headers
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:54.0) Gecko/20100101 Firefox/54.0",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:39.0) Gecko/20100101 Firefox/39.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:40.0) Gecko/20100101 Firefox/40.0",
    ]
random_agent = random.choice(user_agents)

# Arguments error message
def parser_error(msg):
    raise ValueError("Check -h for usage please!")

# SET THE BASIC CONF FOR LOGGING
logging.basicConfig(level=logging.INFO)
# CREATE A LOGGER WITH __NAME__ FOR THE CURRENT MODULE
logger = logging.getLogger(__name__)

# Define the parser for using the code
def setup_argparse():
    parser = argparse.ArgumentParser(description="Voo2dir -  a directory brute-forcing tool for website path enumeration.")
    parser.add_argument("-u", "--url", required=True, help="Host/Target.")
    parser.add_argument("-w", "--wordlist", required=True, help="path to wordlist.")
    parser.add_argument("-e", "--extensions", nargs="+", default=[], help="EXTENSIONS to be set like php txt rar")
    parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose mode.")
    parser.add_argument("-t", "--time", required=False, type=float, help="Set the timing for each request.")
    parser.add_argument("-b", "--batch", required=True, type=int, help="Numbers requests are sent at once.")
    parser.error = parser_error
    args = parser.parse_args()

    # Set up logging level based on verbosity
    if args.verbose:
        # SHOWS ALL PATH AND RESPONSE CODE.
        logger.setLevel(logging.DEBUG)
    else:
        # SHOW INFO [ NO VERBOSE ]
        logger.setLevel(logging.INFO)

    # CHECK IS WORDLIST FILE EXIST/NOT EXIST USING PATH
    if not Path(args.wordlist).is_file():
        msg_err(f"No such file! Try again please {args.wordlist}")

    if args.time is not None and args.time < 0:
        msg_err("Delay time must be a positive number.")

    return args

def msg_err(err):
    logger.warning(err)
    exit(0)

def make_request(url: str, word: str, ext: str, delay_time: int):
    # Make the request
    if ext:
        path = f"{word}.{ext}"
    else:
        path = word
    try:
        req = requests.get(urljoin(url, path), timeout=2, headers={"User-Agent": random_agent})
        if req.status_code == 200:
            logger.info(f"{Cyan}The path -> {urljoin(url, path)} has been found! Status: {req.status_code}{Normal}")

        else:
            logger.debug(f"{Red}Request to {urljoin(url, path)} failed with status code {req.status_code}{Normal}")

        if delay_time:
            time.sleep(delay_time)

    except requests.exceptions.RequestException as e:
        logger.debug(f"{Red}Error sending request to {urljoin(url, path)}:\nINFO: {str(e)}{Normal}")

# ------------------------------- MAIN FUNCTION -------------------------------

def main(url: str, wordlist: str, extensions: List[str], batch_size: int, delay_time: int):
    logger.info(f"Starting Voo2dir for {url}")
    time.sleep(1)
    try:
        with open(wordlist, "r") as f:
            words = []
            for line in f:
                line = line.strip()
                if line and "#" not in line:
                    words.append(line)

        logger.info(f"{SPACE_PREFIX}{TEE2}{Red}Loaded {len(words)} words from {wordlist}{Normal}")
        time.sleep(1)
        logger.info(f"{SPACE_PREFIX * 2}{TEE2}{Red}Extensions: {extensions or ['(No Extension loaded)']}{Normal}")
        time.sleep(1)

        # Use alive_bar to see the progress for nice waiting time and indication
        with alive_bar(len(words) * len(extensions or [None])) as bar:
            word_ext_pairs = [(word, ext) for word in words for ext in extensions or [None]]
            for i in range(0, len(word_ext_pairs), batch_size):
                batch = word_ext_pairs[i:i+batch_size]
                if len(batch) > 10:
                    logger.warning(f"{Purple}Batch limits: 10. Try again please.{Normal}")
                    exit(0)
                else:
                    threads = [threading.Thread(target=make_request, args=(url, word, ext, delay_time)) for word, ext in batch]
                    for thread in threads:
                        thread.start()
                    for thread in threads:
                        thread.join()
                        bar()

    except FileNotFoundError:
        msg_err(f"No such file! Try again please... {wordlist}")
    except KeyboardInterrupt:
        logger.info("User interrupted, exit...")
        exit(0)
    except Exception as e:
        logger.error(f"Something went wrong!\nINFO:{str(e)}")

if __name__ == "__main__":
    try:
        args_run = setup_argparse()
        main(args_run.url, args_run.wordlist, args_run.extensions, batch_size=args_run.batch, delay_time=args_run.time)
    except Exception as e:
        print(e)
