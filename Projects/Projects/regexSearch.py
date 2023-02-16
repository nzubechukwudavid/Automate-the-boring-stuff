"""
Write a program that opens all .txt files in a folder and searches for any
line that matches a user-supplied regular expression. The results should
be printed to the screen.
"""
import re
import os


# Function to get all .txt files in a folder.
def getFiles(file_path):
    os.chdir(file_path)
    folder_content = os.listdir(file_path)
    txt_file_list = []
    for fileName in folder_content:
        if fileName[-4:] == '.txt':
            txt_file_list.append(fileName)
    return txt_file_list


# Function to obtain the regex from the user.
def getQuery():
    directory = input("Enter the directory you would like to scan.\n-->")
    query = input("Enter the regular expression you would like to search for.\n--> ")
    regex = re.compile(query, re.IGNORECASE)

    return regex, directory


def searchFiles(txt_file_list):
    for file in txt_file_list:
        match_found = False
        print(f"Scanning file: {file}...")
        file_object = open(file)
        content = file_object.readlines()
        file_object.close()

        for line in content:
            match = searchTermRegex.search(line)

            if match is not None:
                match_found = True
                print(f"\tmatch found in: line {content.index(line) + 1}\n\t\t>>{line}")
        if not match_found:
            print(f"No matches in {file}")


searchTermRegex, filePath = getQuery()
txtFileList = getFiles(filePath)
searchFiles(txtFileList)
