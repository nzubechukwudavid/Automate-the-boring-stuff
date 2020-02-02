#! Python
# phoneAndEmail.py - Finds all phone numbers and addresses on the clipboard

import pyperclip
import re



# Create a regex for phone numbers
phoneRegex = re.compile(r'''(
    (\+234 | 0)                            # area code
    (\s|-|\.)?                             # separator
    (\d{3})                                # first 3 digits
    (\s|-|\.)?                             # separator
    (\d{3})                                # next 3 digits
    (\s|-|\.)?                             # separator
    (\d{4})                                # last 4 digits
    )''', re.VERBOSE)

# create regex for emails
emailRegex = re.compile(r'((\S)+@(\S)+.(\w+))') 
# i have a problem here, but i dont know how to get around it, but this works well enough... i hope. 
# please leave a comment if you can help with this regular expression.

# This regex doesn't seem to work:
#emailRegex = re.compile(r'''(
#                              [a-zA-Z0-9._%+-]+                # username
#                               @                               # @ symbol
#                               [a-zA-Z0-9.-]+                  # domain name
#                               (\.[a-zA-Z]{2,4})               # dot-something
#                               )''', re.VERBOSE)

# Get text off of the clipboard
text = str(pyperclip.paste())

matches = []

#Match the numbers and emails
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5], groups[7]])
    # get the number groups and join them with '-' inbetween them 
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])

#  make a string for the clipboard and copy it to the clipboard

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to Clipboard:')
    print('\n'.join(matches))
else:
    print("No numbers or email addresses were found.")

