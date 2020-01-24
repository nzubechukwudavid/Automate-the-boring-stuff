#! Python

message = "It was a bright cold day in April, and the clocks were striking thirten."
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] += 1


z = list(count.items())



for x in range(len(z)):
    z[x] = list(z[x])
    

print(z)
print("\n\n\n\n")


for i in z:
    print()
    print(i[0], "-->", i[1])
