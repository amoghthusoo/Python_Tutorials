import matplotlib.pyplot as plt

r = 500
p = 1 - r

x = 0
y = r

x_coordinates = [x]
y_coordinates = [y]

while True:

    if(p < 0):
        x += 1
        p += 2 * x + 1

    elif(p >= 0):
        x += 1
        y -= 1
        p += -2 * y + 2 * x + 1

    x_coordinates.append(x)
    y_coordinates.append(y)

    if(x >= y):
        break

i = len(x_coordinates) - 1
while(i >= 0):
    x_coordinates.append(y_coordinates[i])
    y_coordinates.append(x_coordinates[i])
    
    i -= 1

plt.plot(x_coordinates, y_coordinates, color = "purple")

i = 0
while(i < len(x_coordinates)):

    y_coordinates[i] *= -1
    i += 1

plt.plot(x_coordinates, y_coordinates, color = "purple")

i = 0
while(i < len(x_coordinates)):

    x_coordinates[i] *= -1
    i += 1

plt.plot(x_coordinates, y_coordinates, color = "purple")

i = 0
while(i < len(x_coordinates)):

    y_coordinates[i] *= -1
    i += 1

plt.plot(x_coordinates, y_coordinates, color = "purple")

plt.axis("equal")
plt.show()