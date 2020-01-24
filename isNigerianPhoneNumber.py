#! Python

def isNigerianPhoneNumber(text):
   
    if len(text) == 14:
        if text[0] != '+':
            return False
        for i in range(1,14):
            if not text[i].isdecimal():
                return False
    
#    if len(text) == 11:
#        if text[0] != '0':
#            return False
#        if text.isdecimal() == False:
#            return False
            
        return True


print("'+2348146139053' is a phone number:")
print(isNigerianPhoneNumber('+2348146139053'))
print("'08146139053' is a phone number:")
print(isNigerianPhoneNumber('08146139053'))
print("'+Booksaregreat' is not a phone number")
print(isNigerianPhoneNumber('+Booksaregreat'))
print()


message = 'Call me at +2348146139053 tomorrow.'
for i in range(len(message)):
    chunk = message[i:i+14]
    if isNigerianPhoneNumber(chunk):
        print('Phone number found: ' + chunk)
print("Done")