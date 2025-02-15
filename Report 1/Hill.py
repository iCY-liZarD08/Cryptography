import numpy as np
from math import gcd

def mod_inverse(determinant, mod=26):

    for i in range(1, mod):
        if (determinant * i) % mod == 1:
            return i
    return None

def hill_cipher_encrypt(plain_text, key):

    plain_text = plain_text.upper().replace(" ", "")  
    key = key.upper()

    block_size = int(np.sqrt(len(key)))
    if block_size**2 != len(key):
        raise ValueError("Key length must be a perfect square.")

    key_matrix = np.array([[ord(key[i * block_size + j]) - 65 for j in range(block_size)] for i in range(block_size)])

    determinant = int(round(np.linalg.det(key_matrix))) % 26
    if determinant == 0 or gcd(determinant, 26) != 1:
        raise ValueError("Key matrix is not invertible under modulo 26.")

    while len(plain_text) % block_size != 0:
        plain_text += 'X'

    blocks = [plain_text[i:i + block_size] for i in range(0, len(plain_text), block_size)]
    cipher_text = ""

    for block in blocks:
        block_vector = np.array([ord(char) - 65 for char in block]).reshape(-1, 1)
        cipher_vector = np.dot(key_matrix, block_vector) % 26
        cipher_text += ''.join(chr(int(num) + 65) for num in cipher_vector.flatten())

    return cipher_text

def hill_cipher_decrypt(cipher_text, key):

    key = key.upper()
    block_size = int(np.sqrt(len(key)))

    key_matrix = np.array([[ord(key[i * block_size + j]) - 65 for j in range(block_size)] for i in range(block_size)])

    determinant = int(round(np.linalg.det(key_matrix))) % 26
    mod_inv = mod_inverse(determinant, 26)
    
    if mod_inv is None:
        raise ValueError("Key matrix is not invertible under modulo 26.")

    adjugate_matrix = np.round(np.linalg.inv(key_matrix) * np.linalg.det(key_matrix)).astype(int) % 26
    inverse_key_matrix = (mod_inv * adjugate_matrix) % 26

    blocks = [cipher_text[i:i + block_size] for i in range(0, len(cipher_text), block_size)]
    decrypted_text = ""

    for block in blocks:
        block_vector = np.array([ord(char) - 65 for char in block]).reshape(-1, 1)
        plain_vector = np.dot(inverse_key_matrix, block_vector) % 26
        decrypted_text += ''.join(chr(int(num) + 65) for num in plain_vector.flatten())

    return decrypted_text


message = input("Enter the message here: ")
key = input("Enter the key here: ")
encrypted_message = hill_cipher_encrypt(message, key)
print("Anonymus will preview this message as:", encrypted_message)
decrypted_message = hill_cipher_decrypt(encrypted_message, key)
print("Reciever will decrypt this message as:", decrypted_message)
