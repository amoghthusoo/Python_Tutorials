import math

def get_n(p, q):
    return p * q

def get_pi_n(p, q):
    return (p - 1) * (q - 1)

def get_e(pi_n):
    
    for i in range(2, pi_n):
        if(math.gcd(i, pi_n) == 1):
            return i

def get_d(pi_n, e):

    i = 1
    while True:
        if(((pi_n * i) + 1) % e == 0):
            return ((pi_n * i) + 1) // e
        i += 1

def encrypt(m, n, e):
    return (m ** e) % n

def decrypt(c, n, d):
    return (c ** d) % n

def main():
    
    # m = 152   # 0 <= m < n
    # p = 61
    # q = 53

    m = int(input("Enter the message (decimal) : "))
    p = int(input("Enter first prime number : "))
    q = int(input("Enter second prime number : "))
    print()

    n = get_n(p, q)
    pi_n = get_pi_n(p, q)
    e = get_e(pi_n)
    d = get_d(pi_n, e)

    cipher_text = encrypt(m, n, e)
    decrypted_text = decrypt(cipher_text, n, d)

    print("Plain Text : ", m)
    print("Cipher Text: : ", cipher_text)
    print("Decrypted Text: : ", decrypted_text)
    print()

    if(m == decrypted_text):
        print("Decryption is successful.")
    else:
        print("Decryption is unsuccessful.")

if(__name__ == "__main__"):
    print()
    main()
    print()
