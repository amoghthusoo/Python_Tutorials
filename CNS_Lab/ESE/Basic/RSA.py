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

M = 14

cipher_text = int(M ** e) % n
decrypted_text = int(cipher_text ** d) % n 

print(f"Plain Text -> {M}")
print(f"Cipher Text -> {cipher_text}")
print(f"Decrypted Text -> {decrypted_text}")