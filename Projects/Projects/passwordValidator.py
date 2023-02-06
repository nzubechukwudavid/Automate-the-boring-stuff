#! Python3
# This program is made to detect strong passwords using these criteria:
# * At least 8 characters long
# * contains both uppercase and lowercase characters
# * has at least one digit
#
# The purpose of this project is to practice implementing regexes in solutions.

import re

print("This program checks your password to determine if it is a strong one.")
print("""
Your password should:
* Be at least 8 characters long.
* Contain both uppercase and lowercase letters.
* Have at least one digit.""")
# initialize variables
sample = 0
passwordIsValid = False
trueCondition = [True, True, True, True]

while passwordIsValid is False:
    sample = input("Enter your password: ")
    # regular expressions for the conditions
    numberRegex = re.compile(r"\d")
    uppercaseRegex = re.compile(r"[A-Z]")
    lowercaseRegex = re.compile(r"[a-z]")
    characterCountRegex = re.compile(r"(\S){8}")

    # dictionary to store the conditions
    isvalid = {"number": False, "uppercase": False,
               "lowercase": False, "characterCount": False}

    # check through the conditions
    if numberRegex.search(sample) is not None:
        isvalid["number"] = True

    if uppercaseRegex.search(sample) is not None:
        isvalid["uppercase"] = True

    if lowercaseRegex.search(sample) is not None:
        isvalid["lowercase"] = True

    if characterCountRegex.search(sample) is not None:
        isvalid["characterCount"] = True

    for condition, state in isvalid.items():
        if state is False:

            if condition == "number":
                print("This password does not contain a Number.")
            if condition == "uppercase":
                print("This password does not contain an Uppercase Letter.")
            if condition == "lowercase":
                print("This password does not contain a lowercase letter.")
            if condition == "characterCount":
                print("This password does not contain up to 8 characters.")

    # Check if all conditions are met
    x = list(isvalid.values())
    if trueCondition is x:
        passwordIsValid = True
    else:
        print("Try again.\n")


print(sample, "is a Strong Password")
                                               