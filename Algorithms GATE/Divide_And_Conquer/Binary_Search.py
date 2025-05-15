"""
Recurrence:
T(n) = T(n/2) + 1 ; n > 1
        1         ; n = 1

On appling Extended Master's Theorem,
T(n) = O(log(n))
"""

def binary_search(arr, i, j, target):

    if(i == j):
        if(arr[i] == target):
            return i
        else:
            return -1
        
    mid = (i + j)//2

    if(arr[mid] == target):
        return mid
    elif(target < arr[mid]):
        return binary_search(arr, i, mid - 1, target)
    else:
        return binary_search(arr, mid + 1, j, target)
    
arr = [2, 3, 8, 10, 12, 15]
i = 0
j = len(arr) - 1
target = 18
result = binary_search(arr, i, j, target)
print(result)