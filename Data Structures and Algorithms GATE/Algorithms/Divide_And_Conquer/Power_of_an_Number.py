"""
Recurrence:
T(n) = 2T(n/2) + c ; n > 1
        1          ; n = 1

On appling Extended Master's Theorem,
T(n) = O(n)
"""

def power(a, n):

    if(n == 1):
        return a
    
    if(n % 2 == 0):
        return power(a, n//2) * power(a, n//2)

    else:
        return a * power(a, n//2) * power(a, n//2)


a = 4
n = 2
result = power(a, n)
print(result)