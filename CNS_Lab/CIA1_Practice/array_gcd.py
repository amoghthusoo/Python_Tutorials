def gcd(a, b):

    if(b == 0):
        return a
    else:
        return gcd(b, a % b)

arr = [48,72,120,36,60,96,144,180,108,240]

result = arr[0]
i = 1
while(i < len(arr)):
    result = gcd(result, arr[i])    
    i += 1

print(result)