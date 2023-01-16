#! Python3

# PASSWORD LOCKER 
# This program is designed to allow you store your passwords and retrieve them easily at the time of need
import pyperclip
import sys
import time

PASSWORDS = {'email': 'F7minlBDDuvMJuxESSKhTxFtjVB6',
             'blog': 'VmALvQyKAxiVH5G8vo1ifMLZF3sdt',
             'luggage': '12345'}

if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1].lower()  # first command line argument is the file name

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard')
else:
    print('There is no account named ' + account)

time.sleep(3)
