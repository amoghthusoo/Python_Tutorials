def encrypt(s, k):
    c = ""
    for e in s:
        c += chr(((ord(e) - 97 + k) % 26) + 97)
    return c

def decrypt(s, k):
    p = ""
    for e in s:
        p += chr(((ord(e) - 97 - k) % 26) + 97)
    return p

input_text = input("Enter the plain text : ")
k = 3
cipher_text = encrypt(input_text, k)
plain_text = decrypt(cipher_text, k)
print(f"Cipher Text : {cipher_text}")
print(f"Plain Text : {plain_text}")