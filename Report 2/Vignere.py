import numpy as np
def encrypt_message(plain_text, key):
    cipher_text = ''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for i, letter in enumerate(plain_text):
        if letter.isalpha():
            is_upper = letter.isupper()
            letter = letter.lower()
            index = alphabet.find(letter)
            shift = alphabet.find(key[i % len(key)].lower())
            shifted_index = (index + shift) % 26
            shifted_letter = alphabet[shifted_index]
            cipher_text += shifted_letter.upper() if is_upper else shifted_letter
        else:
            cipher_text += letter
    return cipher_text

def decrypt_message(cipher_text, key):
    plain_text = ''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for i, letter in enumerate(cipher_text):
        if letter.isalpha():
            is_upper = letter.isupper()
            letter = letter.lower()
            index = alphabet.find(letter)
            shift = alphabet.find(key[i % len(key)].lower())
            shifted_index = (index - shift) % 26
            shifted_letter = alphabet[shifted_index]
            plain_text += shifted_letter.upper() if is_upper else shifted_letter
        else:
            plain_text += letter
    return plain_text

message = input('Enter your message here : ')
key = input('Enter the key here : ')
cipher_text = encrypt_message(message, key)
print("Anonymus will preview this message as:", cipher_text)
decrypted_message = decrypt_message(cipher_text, key)
print("Receiver will decrypt this message as:", decrypted_message)