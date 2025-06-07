def encrypt(p):
    
    part1 = part2 = ""
    for i in range(0, len(p), 2):
        
        part1 += p[i]
        try:
            part2 += p[i + 1]
        except:
            pass
        
    return part1 + part2

def decrypt(c):

    if(len(c) % 2 == 0):
        mid = len(c) // 2
    else:
        mid = len(c) // 2 + 1

    part1 = c[0 : mid]
    part2 = c[mid : ]

    p = ""
    for i in range(len(part1)):
        p += part1[i]

        try:
            p += part2[i]
        except:
            pass

    return p

input_text = input("Enter input text : ")
cipher_text = encrypt(input_text)
plain_text = decrypt(cipher_text)
print(cipher_text)
print(plain_text)
