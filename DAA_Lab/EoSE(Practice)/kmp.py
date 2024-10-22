p = input("Enter pattern : ")
s = input("Enter string : ")

# Construction of pi array
pi = [None for _ in range(len(p))]
pi[0] = -1
k = -1
q = 1
while(q < len(p)):

    while(k > -1 and p[k + 1] != p[q]):
        k = pi[k]

    if(p[k + 1] == p[q]):
        k += 1
    
    pi[q] = k
    
    q += 1


# Finding shifts
q = -1
i = 0
while(i < len(s)):

    while(q > -1 and p[q + 1] != s[i]):
        q = pi[q]

    if(p[q + 1] == s[i]):
        q += 1

    if(q == len(p) - 1):
        print(i - len(p) + 1)
        q = pi[q]

    i += 1
