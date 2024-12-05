import matplotlib.pyplot as plt

r = 5

x_coordinates = []
y_coordinates = []

x = -r
while(x <= r):
    
    x_coordinates.append(x)
    y_coordinates.append((r ** 2 - x ** 2) ** 0.5)
        
    x += 0.1

plt.plot(x_coordinates, y_coordinates, color = "purple")

i = 0
while(i < len(y_coordinates)):
    y_coordinates[i] *= -1
    i += 1

plt.plot(x_coordinates, y_coordinates, color = "purple")
plt.axis("equal")
plt.show()