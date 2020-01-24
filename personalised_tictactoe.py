#! Python

#AUTHOR : Morah David
#AUTHOR'S_NOTE : with what i learnt of dictionaries, im trying to represent a data structure for the tic tac toe game.
#VERSION : 1.2
#LAST EDITED : 1:18:2020 


from random import randint
import sys

#Data Structure for TIC TAC TOE
theBoard = {'top-l': ' ', 'top-m': ' ', 'top-r': ' ',
            'mid-l': ' ', 'mid-m': ' ', 'mid-r': ' ',
            'low-l': ' ', 'low-m': ' ', 'low-r': ' '}

#Function to output the current board data
def printBoard(board):
    pad = "     "
    print()
    print(pad, board['top-l'] + '|' + board['top-m'] + '|' + board['top-r'])
    print(pad, '-+-+-')
    print(pad, board['mid-l'] + '|' + board['mid-m'] + '|' + board['mid-r'])
    print(pad,'-+-+-')
    print(pad, board['low-l'] + '|' + board['low-m'] + '|' + board['low-r'])
    print()
#Function to check for a winner
def checkBoard(board):

#__________________________________1_____________________________________

    if (board['top-l'] == "X") and (board['top-m'] == "X") and (board['top-r'] == "X") :
        return (True, "X")

    elif (board['top-l'] == "O") and (board['top-m'] == "O") and (board['top-r'] == "O") :
        return (True, "O")
#___________________________________2_____________________________________

    elif (board['mid-l'] == "X")  and (board['mid-m'] == "X") and (board['mid-r'] == "X"):
        return (True, "X")

    elif (board['mid-l'] == "O")  and (board['mid-m'] == "O") and (board['mid-r'] == "O"):
        return (True, "O")

#____________________________________3_____________________________________

    elif ( board['low-l'] == "X") and (board['low-m'] == "X") and (board['low-r'] == "X"):
        return (True, "X")
    
    elif ( board['low-l'] == "O") and (board['low-m'] == "O") and (board['low-r'] == "O"):
        return (True, "O")
    
#_____________________________________4__________________________________

    elif ( board['top-l'] == "X") and (board['mid-l'] == "X") and (board['low-l']  == "X"):
        return (True, "X")

    elif ( board['top-l'] == "O") and (board['mid-l'] == "O") and (board['low-l']  == "O"):
        return (True, "O")


#___________________________________5____________________________________

    elif ( board['top-m'] == "X") and (board['mid-m'] == "X")and (board['low-m'] == "X"):
        return (True, "X")

    elif ( board['top-m'] == "O") and (board['mid-m'] == "O")and (board['low-m'] == "O"):
        return (True, "O")

#___________________________________6_____________________________________

    elif ( board['top-r'] == "X")and (board['mid-r'] == "X") and (board['low-r'] == "X"):
        return (True, "X")

    elif ( board['top-r'] == "O")and (board['mid-r'] == "O") and (board['low-r'] == "O"):
        return (True, "O")
#___________________________________7_____________________________________

    elif ( board['top-r'] == "X") and (board['mid-m'] == "X")and (board['low-l'] == "X"):
        return (True, "X")

    elif ( board['top-r'] == "O") and (board['mid-m'] == "O")and (board['low-l'] == "O"):
        return (True, "O")

#___________________________________8___________________________________

    elif ( board['top-l'] == "X") and (board['mid-m'] == "X") and (board['low-r'] == "X"):
        return (True, "X")

    elif ( board['top-l'] == "O") and (board['mid-m'] == "OL") and (board['low-r'] == "O"):
        return (True, "O")

#________________________________________________________________________
    else:
        return (False, "")

#function to switch turns
def switchTurn(turn):
    if turn == "X" :
        turn = "O"
        return turn
    else:
        turn = 'X'
        return turn


#Who gets to go first?
turn = randint(0,1)
if turn == 0:
    turn = "X"

elif turn == 1:
    turn = "O"
else:
    sys.exit()

#Gameplay
for i in range(9):
    printBoard(theBoard)
    print('Turn for ' + turn + '. Move on which space?')
    
#Raise an error if input isn't acceptable. Will modify input system later
    try:
        move = input().lower()
        assert (move in theBoard)
    except:
        print("An error has occurred. Exiting..")
        sys.exit()


    theBoard[move] = turn

    win, winner = checkBoard(theBoard)

    if win and (winner == "X" or "O"):
        printBoard(theBoard)
        print(winner, "wins!  Good Game!")
        break
    else:
        pass

    switchTurn(turn)

print('Thank you.')