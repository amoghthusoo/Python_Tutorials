from random import shuffle
permutation = [chr(e) for e in range(97, 123)]
shuffle(permutation)
encrypt_dict = dict(zip([chr(e) for e in range(97, 123)], permutation))
decrypt_dict = dict(zip(permutation, [chr(e) for e in range(97, 123)]))
def encrypt(p):
    c = ""
    for e in p:
        c += encrypt_dict[e]
    return c
def decrypt(c):
    p = ""
    for e in c:
        p += decrypt_dict[e]
    return p
input_text = input("Enter the plain text : ")
cipher_text = encrypt(input_text)
plain_text = decrypt(cipher_text)
print(f"Cipher Text : {cipher_text}")
print(f"Plain Text : {plain_text}")