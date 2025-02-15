import numpy as np

def EncryptMessage(message, key):
    cipherText = ''
    
    if key == 1: 
        return message
    
    matrix = [['' for _ in range(len(message))] for _ in range(key)]
    
    r, c = 0, 0  
    down = True  
    
    for char in message:
        matrix[r][c] = char
        c += 1 
        
        if down:
            r += 1
        else:
            r -= 1
        
        if r == key - 1:
            down = False
        elif r == 0:
            down = True
    
    for row in matrix:
        cipherText += ''.join(row)
    
    return cipherText

message = input("Enter the message: ")
key = int(input("Enter the key: "))

encrypted_message = EncryptMessage(message, key)
print("Anonymus will preview this message as:", encrypted_message)
print("Receiver will preview this message as:",message)
