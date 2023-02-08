#! Python

"""
Create a Mad Libs program that reads in text files and lets the user add
their own text anywhere the word ADJECTIVE, NOUN, ADVERB, or VERB
appears in the text file
"""
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

madLibText = adjectiveRegex.sub(input("Enter an Adjective: \n"), madLibText)
madLibText = nounRegex.sub(input("Enter a Noun: \n"), madLibText)
madLibText = verbRegex.sub(input("Enter a verb: \n"), madLibText)
madLibText = adverbRegex.sub(input("Enter an Adverb: \n"), madLibText)








