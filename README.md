A script that can be used to bruteforce the tomcat manager login page.

# Usage

Tomcat Manager or Host-Manager Credential Bruteforcing

options:

-h, --help                              show this help message and exit
-U URL, --url URL                       Base URL to the Tomcat page (e.g., http://target.com)
-P PATH, --path PATH                    Manager or host-manager URI (e.g., /host-manager/html)
-u USERNAMES, --usernames USERNAMES     Path to file containing usernames
-p PASSWORDS, --passwords PASSWORDS     Path to file containing passwords
  -v, --verbose                         Enable verbose output to see attempted credentials and encoded values
  -r RATE_LIMIT, --rate-limit RATE_LIMIT Delay in seconds between requests (e.g., 0.5 for half a second)
                        
# Example

python3 tomforce.py -U https://example.com -P /host-manager -u usernames.txt -p passwords.txt -v
