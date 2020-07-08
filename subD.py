import threading
import sys
import os
green="\033[1;32;40m"
red="\033[1;31;40m"
drk="\033[1;30;40m"
white="\033[1;37;40m"
usage = f'\n\033[1;31;40m[+]-----------------Required Arguments -----------------[+]\n{white}python3 subD.py [host]\n{green}example: python3 subD.py example.com\n[+]{red}------------------Optional Arguments------------------[+]{white}python3 subD.py [host]-o [filename or filepath]\n{green}example: python3 subD.py example.com -o results.txt '
if (len(sys.argv)<2):
	print(usage)
	sys.exit()
else:
	pass
try:
	import requests
except:
	os.system("pip install requests")
	os.system("clear")



print(f'{red}-'*60)
print(f"{white}--------------------[+] Sub-D BY RC [+]--------------------")
print(f'{green}-'*60)
filepath="test"
domain = sys.argv[1]

file=open('sbd.txt')
content = file.read()
# split by new lines
subdomains = content.splitlines()
find=0
def full(subdomains):
	    # construct the url
 	   url = f"http://{subdomain}.{domain}"
 	   try:
 	   	requests.get(url)
 	   except requests.ConnectionError:
 	   	pass
 	   else:
 	   	print("[+] Discovered subdomain:", url)
 	   	global find
 	   	find+=1

for subdomain in subdomains:
	thread= threading.Thread(target=full,args=(subdomains,))
	thread.start()
print(f"{red}[+]---------- Found {find} Unique Subdomains ----------[+]")
