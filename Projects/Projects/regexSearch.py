"""
Write a program that opens all .txt files in a folder and searches for any
line that matches a user-supplied regular expression. The results should
be printed to the screen.
"""
import re
import os


# Function to get all .txt files in a folder.
def getFiles(file_path):
    folder_content = os.listdir(file_path)
    txt_file_list = []
    for fileName in folder_content:
        if fileName[-4:] == '.txt':
            txt_file_list.append(fileName)
    return txt_file_list


# Function to obtain the regex from the user.
def getQuery():
    query = input("Enter the regular expression you would like to search for.\n--> ")
    regex = re.compile(query, re.IGNORECASE)
    return regex
