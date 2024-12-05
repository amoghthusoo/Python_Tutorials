import matplotlib.pyplot as plt
from math import sin, cos, pi

x_master = [2, 6, 6, 2, 2]
y_master = [3, 3, 6, 6, 3]

plt.plot(x_master, y_master, color = "purple", label = "Original Figure")

##########################################################################################################
# Translation
x_coordinates = []
y_coordinates = []


dx = 10
dy = 10

i = 0
while(i < len(x_master)):

    x_coordinates.append(x_master[i] + dx)
    y_coordinates.append(y_master[i] + dy)

    i += 1

plt.plot(x_coordinates, y_coordinates, color = "red", label = "Translation")

##########################################################################################################
# Scaling
x_coordinates = []
y_coordinates = []


sx = 2.3
sy = 2.3

i = 0
while(i < len(x_master)):

    x_coordinates.append(x_master[i] * sx)
    y_coordinates.append(y_master[i] * sy)

    i += 1

plt.plot(x_coordinates, y_coordinates, color = "blue", label = "Scaling")

##########################################################################################################
# Rotation
x_coordinates = []
y_coordinates = []

theta = 35

i = 0
while(i < len(x_master)):
    
    x_coordinates.append(x_master[i] * cos(theta * pi / 180) - y_master[i] * sin(theta * pi / 180))
    y_coordinates.append(x_master[i] * sin(theta * pi / 180) + y_master[i] * cos(theta * pi / 180))
    
    i += 1

plt.plot(x_coordinates, y_coordinates, color = "green", label = "Rotation")

##########################################################################################################
# Shearing
x_coordinates = []
y_coordinates = []

shx = 1.5

i = 0
while(i < len(x_master)):
    
    x_coordinates.append(x_master[i] + y_master[i] * shx)
    y_coordinates.append(y_master[i])
    
    i += 1

plt.plot(x_coordinates, y_coordinates, color = "orange", label = "Shearing")

##########################################################################################################
# Reflection
x_coordinates = []
y_coordinates = []

i = 0
while(i < len(x_master)):
    
    x_coordinates.append(x_master[i] * -1)
    y_coordinates.append(y_master[i])
    
    i += 1

plt.plot(x_coordinates, y_coordinates, color = "brown", label = "Reflection")

plt.legend()
plt.axis("equal")
plt.show()