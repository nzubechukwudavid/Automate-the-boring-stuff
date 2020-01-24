#! Python
# bulletPointAdder.py - Adds wikipedia bullet points to the start
# of each line of text to the clipboard

# Author: Morah David
# last edited: 1/19/2020



import pyperclip
# Gets copied test
raw_text = pyperclip.paste()
lines = raw_text.split('\n')

for i in range(len(lines)):
    lines[i] = '* ' + lines[i]


text = '\n'.join(lines)


pyperclip.copy(text)