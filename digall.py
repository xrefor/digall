#!/usr/bin/python

import os
import sys

class bcolors:
        HEADER = '\033[95m'
        OKBLUE = '\033[94m'
        OKGREEN = '\033[92m'
        WARNING = '\033[93m'
        FAIL = '\033[91m'
        ENDC = '\033[0m'

try:
    domain = sys.argv[1]
    os.system('clear')
    if ".no" in domain:
        print "[!] Org/Id"+bcolors.WARNING
        orgid = os.system("whois "+domain+"|grep 'Id Number'|awk '{print $3}'")
    print bcolors.ENDC+"[+] Printing A records"+bcolors.WARNING
    os.system('dig '+domain+' +short A')
    print bcolors.ENDC+"[+] Printing AAAA records"+bcolors.WARNING
    os.system('dig '+domain+' +short AAAA')
    print bcolors.ENDC+"[+] Printing A records(www)"+bcolors.WARNING
    os.system('dig www.'+domain+' +short A')
    print bcolors.ENDC+"[+] Printing CNAME records"+bcolors.WARNING
    os.system('dig www.'+domain+' +short CNAME')
    print bcolors.ENDC+"[+] Printing MX records"+bcolors.WARNING
    os.system('dig '+domain+' +short MX')
    print bcolors.ENDC+"[+] Printing NS records"+bcolors.WARNING
    os.system('dig '+domain+' +short NS')
    print bcolors.ENDC+"[+] Printing TXT records"+bcolors.WARNING
    os.system('dig '+domain+' +short TXT')
    print bcolors.OKGREEN+"[+] Done."+bcolors.ENDC

except IndexError:
    print bcolors.FAIL+'[!] Error! No domain specified'
    print bcolors.WARNING+'[-] Usage: digall <domain>'+bcolors.ENDC
