print()

arr = [23, 409, 56, 125, 985, 7, 98]

max_num = arr[0]
i = 0
while(i < len(arr)):
    
    if(arr[i] > max_num):
        max_num = arr[i]
    
    i += 1

passes = 0
while(max_num != 0):

    max_num //= 10
    passes += 1


inter_arr = [0 for i in range(len(arr))]
i = 1
while(i <= passes):

    freq_arr = [0 for _ in range(10)]
    
    j = 0
    while(j < len(arr)):

        freq_arr[(arr[j] % 10 ** i) // (10 ** (i - 1))] += 1
        
        j += 1

    j = 1
    while(j < len(freq_arr)):
        
        freq_arr[j] += freq_arr[j - 1]
        
        j += 1

    j = len(arr) - 1
    while(j >= 0):

        freq_arr[(arr[j] % 10 ** i) // (10 ** (i - 1))] -= 1
        inter_arr[freq_arr[(arr[j] % 10 ** i) // (10 ** (i - 1))]] = arr[j]
        
        j -= 1

    arr = [i for i in inter_arr]

    i += 1

i = 0
while(i < len(arr)):
    print(arr[i], end=" ")
    i += 1

print("\n")