"""
Recurrence:
T(n) = 2T(n/2) + 1 ; n > 1
        1          ; n = 1

On appling Extended Master's Theorem,
T(n) = O(n)
"""

def search(arr, i, j, target):
    
    if(i == j):
        if(arr[i] == target):
            return True
        else:
            return False
        
    mid = (i + j) // 2
    return search(arr, i, mid, target) or search(arr, mid + 1, j, target)


arr = [3, 4, 8, 2, 1, 6, 2, 10, 7]
i = 0
j = len(arr) - 1
target = 7

result = search(arr, i, j, target)
if(result):
    print("Element found.")
else:
    print("Element not found!")
