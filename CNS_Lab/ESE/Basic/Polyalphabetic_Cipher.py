matrix = []

for i in range(26):
    row = []
    for j in range(i, i + 26):
        row.append(chr(j % 26 + 97))
    matrix.append(row)

def encrypt(s, k):
    c = ""
    for i in range(len(s)):
        c += matrix[ord(k[i]) - 97][ord(s[i]) - 97]
        i += 1

    return c

def decrypt(s, k):
    p = "" 
    
    for x in range(len(s)):
        
        i = ord(k[x]) - 97
        for j in range(26):
            if(matrix[i][j] == s[x]):
                p += chr(j + 97)
                break
        x += 1

    return p

input_text = input("Enter the plain text : ")
input_key = input("Enter the key : ")
cipher_text = encrypt(input_text, input_key)
plain_text = decrypt(cipher_text, input_key)
print(f"Cipher Text : {cipher_text}")
print(f"Plain Text : {plain_text}")
