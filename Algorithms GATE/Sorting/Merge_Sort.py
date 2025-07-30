"""
Recurrence:
T(n) = 2T(n/2) + n ; n > 1
        1          ; n = 1

On appling Extended Master's Theorem,
T(n) = O(nlog(n))
"""

def merge(arr, p, r, q):

    i = p
    j = r + 1
    k = 0
    temp = [None for _ in range(q - p + 1)]

    while(i <= r and j <= q):

        if(arr[i] <= arr[j]):
            temp[k] = arr[i]
            i +=1
            k += 1
        
        else:
            temp[k] = arr[j]
            j += 1
            k += 1

    while(i <= r):
        temp[k] = arr[i]
        i += 1
        k += 1

    while(j <= q):
        temp[k] = arr[j]
        j += 1
        k += 1

    i = p
    k = 0
    while(i <= q):
        arr[i] = temp[k]
        i += 1
        k += 1

def merge_sort(arr, i, j):

    if(i < j):

        mid = (i + j)//2
        merge_sort(arr, i, mid)
        merge_sort(arr, mid + 1, j)
        merge(arr, i, mid, j)


arr = [5, 4, 3, 2]
i = 0
j = len(arr) - 1
merge_sort(arr, i, j)
print(arr)
