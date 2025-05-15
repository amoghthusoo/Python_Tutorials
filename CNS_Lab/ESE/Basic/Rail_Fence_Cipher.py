def encrypt(p):
    part1 = ""
    part2 = ""
    i = 0
    while(i < len(p)):
        part1 += p[i]
        try:
            part2 += p[i + 1]
        except:
            pass
        i += 2
    return part1 + part2
def decrypt(c):
    p = ""
    if(len(c) % 2 == 0):
        mid = len(c) // 2
    else:
        mid = len(c) // 2 + 1
    part1 = c[0 : mid]
    part2 = c[mid : ]
    i = 0
    while(i < max(len(part1), len(part2))):
        try:
            p += part1[i]
        except:
            pass
        try:    
            p += part2[i]
        except:
            pass
        i += 1
    return p
input_text = input("Enter the plain text : ")
cipher_text = encrypt(input_text)
plain_text = decrypt(cipher_text)
print(f"Cipher Text : {cipher_text}")
print(f"Plain Text : {plain_text}")