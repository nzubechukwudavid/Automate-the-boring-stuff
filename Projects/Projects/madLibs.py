#! Python

"""
Create a Mad Libs program that reads in text files and lets the user add
their own text anywhere the word ADJECTIVE, NOUN, ADVERB, or VERB
appears in the text file
"""
import os
#   Open the text file and read its contents
#   identify any adjective, noun, adverb or verb
#   prompt the user and replace the adjectives/ nouns / verbs / adverbs
#
#
import re

madLibSample = open(r'C:\Users\Morah\Documents\madlibs\challenges\challenge1.txt')
madLibText = madLibSample.read()

adjectiveRegex = re.compile(r'adjective', re.IGNORECASE)
nounRegex = re.compile(r'noun', re.IGNORECASE)
verbRegex = re.compile(r'verb', re.IGNORECASE)
adverbRegex = re.compile(r'adverb', re.IGNORECASE)

if adjectiveRegex.match(madLibText) is not None:
    madLibText = adjectiveRegex.sub(input("Enter an Adjective: \n"), madLibText)
if nounRegex.match(madLibText) is not None:
    madLibText = nounRegex.sub(input("Enter a Noun: \n"), madLibText)
if verbRegex.match(madLibText) is not None:
    madLibText = verbRegex.sub(input("Enter a verb: \n"), madLibText)
if adverbRegex.match(madLibText) is not None:
    madLibText = adverbRegex.sub(input("Enter an Adverb: \n"), madLibText)

# TODO A problem above is that i cant manage situations where the user may need to
# enter more than one different type of word. for instance when there is
# more than one instance of noun in the madlibs challenge/text

# save result to a new file
os.chdir(r'C:\Users\Morah\Documents\madlibs\solutions')
solutionFile = open(r'solution1.txt', 'w')
solutionFile.write(madLibText)

# close files
madLibSample.close()
solutionFile.close()
