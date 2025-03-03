def p10(s):
    return s[9] + s[7] + s[8] + s[4] + s[6] + s[3] + s[5] + s[0] + s[2] + s[1]

def p8(s):
    return s[2] + s[9] + s[7] + s[8] + s[3] + s[5] + s[6] + s[4]

def p4(s):
    return s[3] + s[1] + s[2] + s[0]

def ep(s):
    return s[0] + s[3] + s[1] + s[2] + s[3] + s[2] + s[0] + s[1]

def ip(s):
    return s[7] + s[5] + s[6] + s[2] + s[4] + s[3] + s[0] + s[1]

def ipi(s):
    return s[6] + s[7] + s[3] + s[5] + s[4] + s[1] + s[2] + s[0]

def split(s):

    n = len(s) // 2
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

    return bin(mat[r][c])[2 : ].zfill(2)

def s1(s):

    r = int(s[0] + s[3], 2)
    c = int(s[1] + s[2], 2)

    mat = [
        [2, 1, 0, 3],
        [3, 1, 3, 2], 
        [0, 1, 2, 3],
        [1, 3, 2, 0]
    ]

    return bin(mat[r][c])[2 : ].zfill(2)

def generate_keys(k):

    k = p10(k)
    l, r = split(k)
    l = shift(l, 1)
    r = shift(r, 1)
    k1 = p8(l + r)

    l = shift(l, 2)
    r = shift(r, 2)
    k2 = p8(l + r)

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
        y = xor(y, keys[i])
        x, y = split(y)
        x = s0(x)
        y = s1(y)
        y = p4(x + y)
        y = xor(y, l)

        if(i != 1):
            result = r + y
            m = result
        else:
            result = y + r

    result = ipi(result)
    return result

M = "10100110"
K = "1100101001"

k1, k2 = generate_keys(K)

ct = encrypt_decrypt(M, k1, k2)
pt = encrypt_decrypt(ct, k1, k2, encrypt = False)


print(M)
print(ct)
print(pt)