p = input("Enter the elements of p, separated by spaces : ")
p = [int(e) for e in p.split()]

INF = 2 ** 31 - 1
m = [[None for _ in range(len(p) - 1)] for _ in range(len(p) - 1)]

for i in range(len(m)):
    for j in range(len(m)):

        if(i == j):
            m[i][j] = 0
        
        elif(i < j):
            m[i][j] = INF

s = [[None for _ in range(len(m))] for _ in range(len(m))]

d = 1
while(d < len(m)):

    j = d
    i = 0
    while(i < len(m) - d):

        k = i
        while(k < j):
            
            temp = m[i][k] + m[k + 1][j] + p[i] * p[k + 1] * p[j + 1]

            if(temp < m[i][j]):
                m[i][j] = temp
                s[i][j] = k + 1
            
            k += 1

        i += 1
        j += 1

    d += 1

a = [i for i in range(1, len(p))]

def insert_brackets(lower_bound, upper_bound):
    
    a.insert(a.index(lower_bound), "(")
    a.insert(a.index(upper_bound) + 1, ")")
    

def find_partition(lower_bound, upper_bound):

    if(upper_bound - lower_bound + 1 <= 2):
        return
    
    partition = s[lower_bound - 1][upper_bound - 1]

    if(partition - lower_bound + 1 >= 2):
        insert_brackets(lower_bound, partition)
    
    if(upper_bound - partition >= 2):
        insert_brackets(partition, upper_bound)

    find_partition(lower_bound, partition)
    find_partition(partition + 1, upper_bound)

a.insert(0, "(")
a.append(")")

find_partition(1, len(p) - 1)

final_str = ""

for e in a:
    if(e in ["(", ")"]):
        final_str += e
    else:
        final_str += f"A{e}"

print(final_str)
