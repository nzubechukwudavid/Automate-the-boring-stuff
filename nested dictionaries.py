#! Python

allGuests = {'Alice': {'apples': 5, 'pretzels': 12},
             'Bob': {'ham sandwiches': 3, 'apples': 2},
             'Carol': {'cups': 3, 'apple pies': 1}}

def totalBrought(guests,item):
    numBrought = 0
    for k, v in guests.items():
        numBrought = numBrought + v.get(item, 0)
    return numBrought

print('Number of things being brought:')
print(' - Apples         ' + str(totalBrought(allGuests, 'apples')))
print(' - Cups           ' + str(totalBrought(allGuests, 'cups')))
print(' - Cakes          ' + str(totalBrought(allGuests, 'cakes')))
print(' - Ham Sandwiches ' + str(totalBrought(allGuests, 'ham sandwiches')))
print(' - Apple Pies     ' + str(totalBrought(allGuests, 'apple pies')))


# PRACTICE  QUESTIONS
# 1. empty_dictionary = {} 
# 2. dictionary = {'foo' : 42}
# 3. a dictionary maps a key to a value which may be of any datatype but a list contains an ordered sequence of values
# 4. you get a KeyError
# 5. no difference
# 6. 'cat' in spam will return True if and only if 'cat' exists as a key in the dictionary
#     while 'cat' in spam.values() will return True if and only if 'cat' is mapped to a key in the dictionary
# 7. spam.setdefault('color','black')
# 8. pprint module. functions are: pprint() and pformat()

