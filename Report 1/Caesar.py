import numpy as np
def EncryptMessage(plainText, key):
    cipherText=''
    for letter in plainText:
        if letter in lowerCase:
            index=lowerCase.index(letter)
            shiftedIndex=(index+key)%26
            cipherText+=lowerCase[shiftedIndex]
        elif letter in upperCase:
            index=upperCase.index(letter)
            shiftedIndex=(index+key)%26
            cipherText+=upperCase[shiftedIndex]
        else:
            cipherText+=letter
    return cipherText

def DecryptMessage(cipherText, key):
    plainText=''
    for letter in cipherText:
        if letter in lowerCase:
            index=lowerCase.index(letter)
            shiftedIndex=(index-key)%26
            plainText+=lowerCase[shiftedIndex]
        elif letter in upperCase:
            index=upperCase.index(letter)
            shiftedIndex=(index-key)%26
            plainText+=upperCase[shiftedIndex]
        else:
            plainText+=letter
    return plainText

upperCase=[]
lowerCase=[]

for i in range(65,91):
    upperCase.append(chr(i))

for j in range(97,123):
    lowerCase.append(chr(j))

message=input("Enter your message here: ")
key=input("Enter your key here: ")
cipherText=EncryptMessage(message,int(key))

print('Anonymous will preview this message as:',cipherText)
print('Receiver will preview this message as:',message)