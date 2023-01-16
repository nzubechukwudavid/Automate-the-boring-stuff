#! Python

# Author: Morah David

# Last Edited: 1/20/2020 

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]


def printTable(tableData):
    colWidths = [0] * len(tableData)

    for i in range(len(tableData)):
        colWidth = 0
        for j in tableData[i]:
            if len(j) > colWidth:
                colWidth = len(j)

        colWidths[i] = colWidth

    # Adds an extra space for more readability
    for i in range(len(colWidths)):
        colWidths[i] += 1

    # loops through each inner list and prints the nth item in it
    for i in range(len(tableData[0])):
        for j in range(len(tableData)):
            print(tableData[j][i].rjust(colWidths[j]), end="")
        print()


printTable(tableData)
input()
