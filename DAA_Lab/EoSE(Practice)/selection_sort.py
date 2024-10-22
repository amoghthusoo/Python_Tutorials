arr = input("Enter the elements of array separated by spaces : ")
arr = [int(i) for i in arr.split()]

i = 0
while(i < len(arr) - 1):
    
    j = i + 1
    min_index = i
    while(j < len(arr)):
        
        if(arr[j] < arr[min_index]):
            min_index= j        
        j += 1

    arr[i], arr[min_index] = arr[min_index], arr[i]
    
    i += 1

print(arr)