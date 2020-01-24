#! Python
import sys
spam = ['apples', 'bananas', 'tofu', 'cats']

def show(sample):
    try:
        type(sample) == list
    except:
        print("Please ensure the value is a list.")
        sys.exit()

    result = ""
    for item in sample:
        if sample.index(item) != (len(sample) - 1):
            result = result + str(item) + ", "

        else:
            result = result + "and " + str(item)
            
    return result

print(show(spam))
            
