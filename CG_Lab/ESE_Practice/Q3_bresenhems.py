import matplotlib.pyplot as plt

x1 = 2
y1 = 3

x2 = 8
y2 = 9

dx = x2 - x1
dy = y2 - y1
p = 2 * dy - dx

x_coordinates = [x1]
y_coordinates = [y1]

x = x1
y = y1
while(True):

    if(p < 0):
        x += 1
        p += 2 * dy

    elif(p >= 0):
        x += 1
        y += 1
        p += 2 * dy - 2 * dx

    x_coordinates.append(x) 
    y_coordinates.append(y)

    if(x == x2):
        break

plt.plot(x_coordinates, y_coordinates, marker = 'o', color = "purple")
plt.axis("equal") 
plt.show()