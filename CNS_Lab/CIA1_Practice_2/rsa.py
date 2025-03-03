from math import gcd

p = 7
q = 11
n = p * q
phi = (p - 1) * (q - 1)

i = 2
while(gcd(i, phi) != 1):
    i += 1
e = i

i = 1
while((phi * i + 1) % e != 0):
    i += 1

d = (phi * i + 1) // e

M = 50

ct = int(M ** e) % n
pt = int(ct ** d) % n

print(M)
print(ct)
print(pt)