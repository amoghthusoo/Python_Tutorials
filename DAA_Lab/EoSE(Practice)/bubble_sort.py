arr = input("Enter the elements of array separated by spaces : ")
arr = [int(i) for i in arr.split()]

i = 0
while(i < len(arr)):
    
    j = 0
    while(j < len(arr) - 1 - i):

        if(arr[j] > arr[j + 1]):
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

        j += 1
    i += 1

print(arr)