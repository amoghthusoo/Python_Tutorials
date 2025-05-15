from random import shuffle
from copy import deepcopy

alphabets = [chr(e) for e in range(97, 123)]
permutation = deepcopy(alphabets)
shuffle(permutation)

encrypt_dict = dict(zip(alphabets, permutation))
decrypt_dict = dict(zip(permutation, alphabets))

def encrypt(s):

    c = ""
    for e in s:
        c += encrypt_dict[e]
    return c

def decrypt(s):

    p = ""
    for e in s:
        p += decrypt_dict[e]
    return p

input_text = input("Enter the plain text : ")
cipher_text = encrypt(input_text)
plain_text = decrypt(cipher_text)
print(f"Cipher Text : {cipher_text}")
print(f"Plain Text : {plain_text}")