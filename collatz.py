import sys

def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return (number // 2)

    else:
        print(3 * number + 1)
        return (3 * number + 1)


try:
    sample = int(input("Enter a number to undergo the collatz sequence. \n"))
except ValueError:
    print("You should enter an integer only.")
    sys.exit()
    
    
while sample != 1:
    sample = collatz(sample)
