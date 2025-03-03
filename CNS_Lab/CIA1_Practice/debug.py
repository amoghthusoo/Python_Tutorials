def p10(s):
    return s[2] + s[4] + s[1] + s[6] + s[3] + s[9] + s[0] + s[8] + s[7] + s[5]

def p8(s):
    return s[5] + s[2] + s[6] + s[3] + s[7] + s[4] + s[9] + s[8]

def p4(s):
    return s[1] + s[3] + s[2] + s[0]   

def ip(s):    
    return s[1] + s[5] + s[2] + s[0] + s[3] + s[7] + s[4] + s[6]

def ipi(s):
    return s[3] + s[0] + s[2] + s[4] + s[6] + s[1] + s[7] + s[5]

def ep(s):
    return s[3] + s[0] + s[1] + s[2] + s[1] + s[2] + s[3] + s[0]

def split(s):
    n = len(s)//2
    return s[0 : n], s[n : ]

def shift(s, k):
    return s[k : ] + s[0 : k]

def xor(x, y):

    result = ""
    i = 0
    while(i < len(x)):
        result += str(int(x[i]) ^ int(y[i]))
        i += 1

    return result

def s0(s):

    r = int(s[0] + s[3], 2)
    c = int(s[1] + s[2], 2)

    mat = [
        [1, 0, 3, 2],
        [3, 2, 1, 0],
        [0, 2, 1, 3],
        [3, 1, 3, 2]
    ]

    return bin(mat[r][c])[2:].zfill(2)

def s1(s):

    r = int(s[0] + s[3], 2)
    c = int(s[1] + s[2], 2)

    mat = [
        [0, 1, 2, 3],
        [2, 0, 1, 3],
        [3, 0, 1, 0],
        [2, 1, 0, 3]
    ]

    return bin(mat[r][c])[2:].zfill(2)

def generate_keys(k):

    k = p10(k)

    l, r = split(k)

    ls = shift(l, 1)
    rs = shift(r, 1)

    k1 = p8(ls + rs)

    ls = shift(ls, 2)
    rs = shift(rs, 2)

    k2 = p8(ls + rs)

    return k1, k2


def encrypt_decrypt(m, k1, k2, encrypt = True):

    if(encrypt):
        keys = [k1, k2]
    else:
        keys = [k2, k1]

    m = ip(m)

    for i in range(2):

        l, r = split(m)
        y = ep(r)
        x = xor(y, keys[i])
        x1, x2 = split(x)
        x1 = s0(x1)
        x2 = s1(x2)
        x = x1 + x2
        x = p4(x)
        x = xor(x, l)

        if(i != 1):
            result = r + x
            m = result

        else:
            result = x + r


    result = ipi(result)
    return result
    
M = "10100110"
K = "1100101001"

k1, k2 = generate_keys(K)

cipher_text = encrypt_decrypt(M, k1, k2)
decrypted_text = encrypt_decrypt(cipher_text, k1, k2, encrypt = False)

print(f"Plain Text -> {M}")
print(f"Cipher Text -> {cipher_text}")
print(f"Decrypted Text -> {decrypted_text}")

