#!/usr/bin/python

import os
import sys 

class bcolors:
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    ENDC = '\033[0m'

domain = sys.argv[1]
os.system('clear')
print "[+] Printing A records"+bcolors.WARNING
os.system('dig '+domain+' +short A')
print bcolors.ENDC+"[+] Printing A records(www)"+bcolors.WARNING
os.system('dig www.'+domain+' +short A')
print bcolors.ENDC+"[+] Printing MX records"+bcolors.WARNING
os.system('dig '+domain+' +short MX')
print bcolors.ENDC+"[+] Printing NS records"+bcolors.WARNING
os.system('dig '+domain+' +short NS')
print bcolors.ENDC+"[+] Printing TXT records"+bcolors.WARNING
os.system('dig '+domain+' +short TXT')
print bcolors.OKGREEN+"[+] Done."+bcolors.ENDC
