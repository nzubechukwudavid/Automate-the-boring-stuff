#! Python

"""
Create a Mad Libs program that reads in text files and lets the user add
their own text anywhere the word ADJECTIVE, NOUN, ADVERB, or VERB
appears in the text file
"""
import re
file = open(r'C:\Users\Morah\Documents\madlibs\challenges\challenge1.txt')
sample = file.read()
file.close()

regex = re.comple(r'ADJECTIVE|NOUN|VERB|ADVERB', re.IGNORECASE)

while True:
    match = regex.search(sample)
    if match is None:
        break
    elif match.group().upper() == 'ADJECTIVE':
        print("Enter an Adjective: ")
    elif match.group().upper() == 'NOUN':
        print("Enter a Noun: ")
    elif match.group().upper() == 'VERB':
        print("Enter a Verb: ")
    elif match.group().upper() == 'ADVERB':
        print("Enter an Adverb: ")
    word = input()
    sample = sample.replace(match.group(), word, 1)

newFile = open(r'C:\Users\Morah\Documents\madlibs\solutions\solution1.txt')


