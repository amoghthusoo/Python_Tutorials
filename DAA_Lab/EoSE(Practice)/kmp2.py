pattern = input("Enter pattern : ")
string = input("Enter string : ")

pi = [None for _ in range(len(pattern))]
pi[0] = -1
k = -1
q = 1
while(q < len(pattern)):
    while(k > -1 and pattern[k + 1] != pattern[q]):
        k = pi[k]

    if(pattern[k + 1] == pattern[1]):
        k += 1
    
    pi[q] = k
    
    q += 1

q = -1
i = 0
while(i < len(string)):

    while(q > -1 and pattern[q + 1] != string[i]):
        q = pi[q]
    
    if(pattern[q + 1] == string[i]):
        q += 1
    
    if(q == len(pattern) - 1):
        print(i - len(pattern) + 1)
        q = pi[q]

    i += 1