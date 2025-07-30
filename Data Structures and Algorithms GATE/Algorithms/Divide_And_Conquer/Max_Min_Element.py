"""
Recurrence:
T(n) = 2T(n/2) + 2 ; n > 1
        1          ; n = 2
        0          ; n = 1

On appling Extended Master's Theorem,
T(n) = O(n)
"""

def max_min(arr, i, j):

    if(i == j):
        return arr[i], arr[i]

    if(i + 1 == j):
        if(arr[i] > arr[j]):
            return arr[i], arr[j]
        else:
            return arr[j], arr[i]
        
    mid = (i + j)//2
    max_1, min_1 = max_min(arr, i, mid)
    max_2, min_2 = max_min(arr, mid + 1, j)

    if(max_1 > max_2):
        max = max_1
    else:
        max = max_2
    
    if(min_1 < min_2):
        min = min_1
    else:
        min = min_2
    
    return max, min

arr = [3, 4, 8, 2, 6, 10, 70]
i = 0
j = len(arr) - 1
max, min = max_min(arr, i, j)
print(max, min)
