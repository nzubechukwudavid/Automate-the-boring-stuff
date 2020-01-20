#! Python 

# PASSWORD LOCKER 
# This program is to allow you store your passwords and retrieve them easily at the time of need

PASSWORDS = {'email': 'F7minlBDDuvMJuxESSKhTxFtjVB6', 
             'blog':'VmALvQyKAxiVH5G8vo1ifMLZF3sdt', 
             'luggage': '12345'}
import pyperclip
import sys
import time

if len(sys.argv) < 2 :
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]     #first command line argument is the file name

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard' )
else:
    print('There is no account named ' + account)
    
time.sleep(3)