from copy import deepcopy

print()

n = int(input("Enter number of nodes : "))

d0 = []

s = [[-1 for _ in range(n)] for _ in range(n)]

for i in range(n):
    temp = input(f"Enter the weights of row{i + 1}, separated by spaces : ")

    temp_arr = []

    for e in temp.split():
        if(e != "inf"):
            temp_arr.append(int(e))
        elif(e == "inf"):
            temp_arr.append(2 ** 31 - 1)
    
    d0.append(temp_arr)

previous = deepcopy(d0)
current = [[None for _ in range(n)] for _ in range(n)]

k = 0
while(k < n):
    
    i = 0
    while(i < n):

        j = 0
        while(j < n):

            first_term = previous[i][j]
            second_term = previous[i][k] + previous[k][j]

            if(second_term < first_term):
                current[i][j] = second_term
                s[i][j] = k
            else:
                current[i][j] = first_term

            j += 1

        i += 1
    
    previous = deepcopy(current)
    k += 1

print()
start_node = int(input("Enter starting node : "))
end_node = int(input("Enter ending node : "))

start_node -= 1
end_node -= 1

path = [start_node, end_node]

loop_memory = True
while(loop_memory):
    i = 0
    while(i < len(path) - 1):
        
        in_between_node = s[path[i]][path[i + 1]]

        if(in_between_node != -1):
            path.insert(i + 1, in_between_node)
            i = 0
            continue

        if(i == len(path) - 2):
            loop_memory = False
            break
        
        i += 1

print()
print("Path : ", end="")
i = 0
while(i < len(path)):
    
    print(path[i] + 1, end="")

    if(i != len(path) - 1):
        print(" -> ", end="")
    else:
        print()
        
    i += 1

print()

'''
0 3 8 inf -4
inf 0 inf 1 7
inf 4 0 inf inf
2 inf -5 0 inf
inf inf inf 6 0
'''