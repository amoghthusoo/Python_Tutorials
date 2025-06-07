from math import gcd
p, q = 7, 11
n = p * q
phi = (p - 1) * (q - 1)

for i in range(2, phi):
    if(gcd(i, phi) == 1):
        e = i
        break

i = 1
while(True):
    
    if(((phi * i) + 1) % e == 0):
        d = ((phi * i) + 1) // e
        break
    i += 1

M = int(input("Enter an integer : "))
cipher_text = int(M ** e) % n
plain_text = int(cipher_text ** d) % n
print(cipher_text)
print(plain_text)