"""
Write a program that opens all .txt files in a folder and searches for any
line that matches a user-supplied regular expression. The results should
be printed to the screen.
"""
import re
import os

# Function to get all .txt files in a folder:
def getFiles(filePath):
    folderContent = os.listdir(filePath)
    txtFileList = []
    for fileName in folderContent:
        if fileName[-4:] == '.txt':
            txtFileList.append(fileName)
    return txtFileList
