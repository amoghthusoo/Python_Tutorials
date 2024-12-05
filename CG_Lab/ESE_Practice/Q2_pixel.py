import matplotlib.pylab as plt

x1 = 2
y1 = 3
x2 = 6
y2 = 5

x_coordinates = [x1, x2]
y_coordinates = [y1, y2]

plt.scatter(x_coordinates, y_coordinates, color = "purple")
plt.axis("equal")
plt.show()