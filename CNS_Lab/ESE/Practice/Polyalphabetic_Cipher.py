matrix = []
for i in range(26):
    row = []
    for j in range(i, i + 26):
        row.append(chr((j % 26) + 97))
    matrix.append(row)

# for i in range(len(matrix)):
#     for j in range(len(matrix)):
#         print(matrix[i][j], end=" ")
#     print()``

def encrypt(p, k):
    c = ""
    for i in range(len(p)):
        c += matrix[ord(k[i]) - 97][ord(p[i]) - 97]
    return c

def decrypt(c, k):
    p = ""
    for z in range(len(c)):
        i = ord(k[z]) - 97
        for j in range(26):
            if(matrix[i][j] == c[z]):
                p += chr(j + 97)
                break
    return p

input_text = input("Enter the input_text : ")
key = input("Enter the key : ")
cipher_text = encrypt(input_text, key)
plain_text = decrypt(cipher_text, key)
print(cipher_text)
print(plain_text)
