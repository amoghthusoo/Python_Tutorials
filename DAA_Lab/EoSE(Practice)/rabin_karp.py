T = "314225142536214"
P = "14"
n = len(T)
m = len(P)
q = 11
d = 10

h = int(d ** (m - 1)) % q

p = 0
t = 0

i = 0
while(i < m):
    
    p = (p * d + int(P[i])) % q
    t = (t * d + int(T[i])) % q 
    
    i += 1

s = 0
while(s <= n - m):

    if(p == t and P == T[s : s + m]):
        print(f"Pattern occurs with {s} shifts.")

    if(s < n - m):
        t = (d * (t - int(T[s]) * h) + int(T[s + m])) % q

    s += 1

