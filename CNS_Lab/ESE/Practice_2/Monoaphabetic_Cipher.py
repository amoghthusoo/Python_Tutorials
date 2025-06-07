from random import shuffle
perm = [chr(e) for e in range(97, 123)]
shuffle(perm)
encrypt_dict = dict(zip([chr(e) for e in range(97, 123)], perm))
decrypt_dict = dict(zip(perm, [chr(e) for e in range(97, 123)]))

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

input_text = input("Enter input text : ")
cipher_text = encrypt(input_text)
plain_text = decrypt(cipher_text)
print(cipher_text)
print(plain_text)