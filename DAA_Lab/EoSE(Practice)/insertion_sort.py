arr = input("Enter the elements of array separated by spaces : ")
arr = [int(i) for i in arr.split()]

i = 1
while(i < len(arr)):

    temp = arr[i]
    j = i - 1
    while(j >= 0 and arr[j] > temp):

        arr[j + 1] = arr[j]
        j -= 1
    
    arr[j + 1] = temp

    i += 1

print(arr)