import matplotlib.pylab as plt

x1 = 2
y1 = 3
x2 = 6
y2 = 7

m = (y2 - y1) / (x2 - x1)
c = y1 - m * x1

x_coordinates = []
y_coordinates = []

i = x1
while(i <= x2):

    x_coordinates.append(i)
    y_coordinates.append(m * i + c)

    i += 0.5

plt.plot(x_coordinates, y_coordinates, marker = 'o', color = "purple", linestyle = "solid", linewidth = 2)
plt.show()