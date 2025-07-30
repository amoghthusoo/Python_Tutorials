"""
Recurrence:
T(n) = T(k) + T(n - k - 1) + O(n) ; n > 1
        1                         ; n = 1

Best Case : k = n/2
On appling Extended Master's Theorem,
T(n) = O(nlog(n)) 

Worst Case : k = 0
Solving by back substitution,
T(n) = O(n ^ 2)
"""

def partition(arr, p, r):

    pivot = arr[r]
    i = p - 1
    j = p
    while(j < r):

        if(arr[j] <= pivot):
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

        j += 1

    arr[i + 1], arr[r] = arr[r], arr[i + 1]
    return i + 1

def quick_sort(arr, p, r):

    if(p < r):
        q = partition(arr, p, r)
        quick_sort(arr, p, q - 1)
        quick_sort(arr, q + 1, r)


arr = [1, 2, 3, 4, 5]
p = 0
r = len(arr) - 1
quick_sort(arr, p, r)
print(arr)