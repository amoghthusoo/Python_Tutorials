def encrypt(p, k = 3):
    c = ""
    for e in p:
        c += chr(((ord(e) - 97 + k) % 26) + 97)
    return c

def decrypt(c, k = 3):
    p = ""
    for e in c:
        p += chr(((ord(e) - 97 - k) % 26) + 97)
    return p

input_text = input("Enter the plain text : ")
cipher_text = encrypt(input_text)
plain_text = decrypt(cipher_text)
print(cipher_text)
print(plain_text)