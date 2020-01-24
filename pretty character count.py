#! Python

import pprint
message = "It was a bright cold day in April, and the clocks were striking thirten."
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] += 1


#pprint.pprint(count)

f = pprint.pformat(count)
print(f)



#pprint.pprint(someDictionaryValue)
#print(pprint.pformat(someDictionaryValue))
