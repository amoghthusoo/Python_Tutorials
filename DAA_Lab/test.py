const = 4

a = const
b = const
c = const

beta = b

for i in range(c - 1):
    beta = (beta * b) % 10


alpha = a
for i in range(beta - 1):
    alpha = (alpha * a) % 10

if(beta == 0):
    print(0)
elif(beta == 1):
    print(alpha % 10)
else:
    print(alpha)