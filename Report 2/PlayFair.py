import numpy as np

def FindIndex(matrix, letter):
    for r, row in enumerate(matrix):
        for c, element in enumerate(row):
            if element == letter:
                return r, c
    return None, None

def generateMatrix(key):
    matrix = []
    keyMatrix = [[None for _ in range(5)] for _ in range(5)]
    
    key = key.upper().replace("J", "I")
    
    for char in key:
        if char not in matrix and char.isalpha():
            matrix.append(char)
    
    letters = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    for letter in letters:
        if letter not in matrix:
            matrix.append(letter)
    
    count = 0
    for r in range(5):
        for c in range(5):
            keyMatrix[r][c] = matrix[count]
            count += 1
    
    return keyMatrix

def prepareMessage(message):
    message = message.upper().replace("J", "I") 
    message = list(message.replace(" ", "")) 
    
    formatted_message = []
    i = 0
    
    while i < len(message):
        if i + 1 < len(message):
            if message[i] == message[i + 1]:  
                formatted_message.append(message[i])
                formatted_message.append('X') 
                i += 1 
            else:
                formatted_message.append(message[i])
                formatted_message.append(message[i + 1])
                i += 2
        else:
            formatted_message.append(message[i])
            formatted_message.append('X')
            i += 1
    
    return formatted_message

def EncryptMessage(message, key):
    keyMatrix = generateMatrix(key)
    prepared_message = prepareMessage(message)
    cipherText = ''
    
    for i in range(0, len(prepared_message), 2):
        digraph = [prepared_message[i], prepared_message[i + 1]]
        
        r1, c1 = FindIndex(keyMatrix, digraph[0])
        r2, c2 = FindIndex(keyMatrix, digraph[1])
        
        if r1 == r2: 
            cipherText += keyMatrix[r1][(c1 + 1) % 5]
            cipherText += keyMatrix[r1][(c2 + 1) % 5]
        elif c1 == c2:
            cipherText += keyMatrix[(r1 + 1) % 5][c1]
            cipherText += keyMatrix[(r2 + 1) % 5][c2]
        else: 
            cipherText += keyMatrix[r1][c2]
            cipherText += keyMatrix[r2][c1]
    
    return cipherText

message = input("Enter the message here: ")
key = input("Enter the key here: ")
encrypted_message = EncryptMessage(message, key)
print("Anonymus will preview this message as:",encrypted_message)
print("Receiver will decrypt this message as:",message)