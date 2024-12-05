import matplotlib.pyplot as plt

x1 = 2
y1 = 3

x2 = 8
y2 = 9

m = (y2 - y1) / (x2 - x1)

x = x1
y = y1

x_coordinates = [x1]
y_coordinates = [y1]

while(True):

    if(m < 1):
        x += 1
        y += m

    elif(m > 1):
        x += 1/m
        y += 1

    elif(m == 1):
        x += 1
        y += 1

    x_coordinates.append(x)    
    y_coordinates.append(y)

    if(x == x2):
        break

plt.plot(x_coordinates, y_coordinates, marker = "o", color = "purple")
plt.axis("equal")
plt.show()    