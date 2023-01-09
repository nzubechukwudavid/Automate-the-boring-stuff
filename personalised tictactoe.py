# AUTHOR : Morah David
# AUTHOR'S_NOTE : with what I learnt of dictionaries, im trying to represent a data structure for the tic-tac-toe game.
# VERSION : 1.2
# LAST EDITED : 1:18:2020

from random import randint
import sys

# Data Structure for TIC TAC TOE
theBoard = {'top-l': ' ', 'top-m': ' ', 'top-r': ' ',
            'mid-l': ' ', 'mid-m': ' ', 'mid-r': ' ',
            'low-l': ' ', 'low-m': ' ', 'low-r': ' '}


# Function to output the current board data
def printBoard(board):
    pad = "     "
    print()
    print(pad, board['top-l'] + '|' + board['top-m'] + '|' + board['top-r'])
    print(pad, '-+-+-')
    print(pad, board['mid-l'] + '|' + board['mid-m'] + '|' + board['mid-r'])
    print(pad, '-+-+-')
    print(pad, board['low-l'] + '|' + board['low-m'] + '|' + board['low-r'])
    print()


# Function to check for a winner
def checkBoard(board):
    # __________________________________1_____________________________________

    if (board['top-l'] == "X") and (board['top-m'] == "X") and (board['top-r'] == "X"):
        return True, "X"

    elif (board['top-l'] == "O") and (board['top-m'] == "O") and (board['top-r'] == "O"):
        return True, "O"

    # ___________________________________2_____________________________________

    elif (board['mid-l'] == "X") and (board['mid-m'] == "X") and (board['mid-r'] == "X"):
        return True, "X"

    elif (board['mid-l'] == "O") and (board['mid-m'] == "O") and (board['mid-r'] == "O"):
        return True, "O"

    # ____________________________________3_____________________________________

    elif (board['low-l'] == "X") and (board['low-m'] == "X") and (board['low-r'] == "X"):
        return True, "X"

    elif (board['low-l'] == "O") and (board['low-m'] == "O") and (board['low-r'] == "O"):
        return True, "O"

    # _____________________________________4__________________________________

    elif (board['top-l'] == "X") and (board['mid-l'] == "X") and (board['low-l'] == "X"):
        return True, "X"

    elif (board['top-l'] == "O") and (board['mid-l'] == "O") and (board['low-l'] == "O"):
        return True, "O"

    # ___________________________________5____________________________________

    elif (board['top-m'] == "X") and (board['mid-m'] == "X") and (board['low-m'] == "X"):
        return True, "X"

    elif (board['top-m'] == "O") and (board['mid-m'] == "O") and (board['low-m'] == "O"):
        return True, "O"

    # ___________________________________6_____________________________________

    elif (board['top-r'] == "X") and (board['mid-r'] == "X") and (board['low-r'] == "X"):
        return True, "X"

    elif (board['top-r'] == "O") and (board['mid-r'] == "O") and (board['low-r'] == "O"):
        return True, "O"
    # ___________________________________7_____________________________________

    elif (board['top-r'] == "X") and (board['mid-m'] == "X") and (board['low-l'] == "X"):
        return True, "X"

    elif (board['top-r'] == "O") and (board['mid-m'] == "O") and (board['low-l'] == "O"):
        return True, "O"

    # ___________________________________8___________________________________

    elif (board['top-l'] == "X") and (board['mid-m'] == "X") and (board['low-r'] == "X"):
        return True, "X"

    elif (board['top-l'] == "O") and (board['mid-m'] == "O") and (board['low-r'] == "O"):
        return True, "O"

    # ________________________________________________________________________
    else:
        return False, ""


# function to switch turns
def switchTurn(currentTurn):
    if currentTurn == "X":
        currentTurn = "O"
        return currentTurn
    else:
        currentTurn = "X"
        return currentTurn


# Who gets to go first?
turn = randint(0, 1)
if turn == 0:
    turn = "X"

elif turn == 1:
    turn = "O"

possibleMoves = {1: "top-l", 2: "top-m", 3: "top-r",
                 4: "mid-l", 5: "mid-m", 6: "mid-r",
                 7: "low-l", 8: "low-m", 9: "low-r"}

# Gameplay
for i in range(9):
    printBoard(theBoard)
    print('Turn for ' + turn + '. Move on which space?')

    # this is David from 2023-01-09.
    # I just cloned this project and im truly amazed that this is my code.
    # I'm going to try to finish this project.
    # I hope that this will help to spur me on with my journey.

    move = eval(input("Enter your move (1-9)"))

    try:
        move = possibleMoves.get(move)
    except KeyError:
        print("Invalid move! \n")

    theBoard[move] = turn

    win, winner = checkBoard(theBoard)

    if win and (winner == "X" or "O"):
        printBoard(theBoard)
        print(winner, "wins!  Good Game!")
        break
    else:
        pass

    turn = switchTurn(turn)

print('Thank you.')
