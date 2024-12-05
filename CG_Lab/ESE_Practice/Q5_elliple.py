import matplotlib.pyplot as plt

a = 4
b = 3

x_coordinates = []
y_coordinates = []

x = -a
while(x <= a):
    
    x_coordinates.append(x)
    y_coordinates.append((b/a) * (a ** 2 - x ** 2) ** 0.5)
    
    x += 0.1
    x = round(x, 1) # Can in skipped in written test

plt.plot(x_coordinates, y_coordinates, color = "purple")

i = 0
while(i < len(y_coordinates)):

    y_coordinates[i] *= -1

    i += 1

plt.plot(x_coordinates, y_coordinates, color = "purple")
plt.axis("equal")
plt.show()