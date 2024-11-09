import matplotlib.pyplot as plt
import math as m

def get_rotated_coordinates(x, y, theta):    
    _x = x * m.cos(theta * m.pi / 180) - y * m.sin(theta * m.pi / 180)
    _y = x * m.sin(theta * m.pi / 180) + y * m.cos(theta * m.pi / 180)
    return _x, _y

def plot_translation(x_coordinates, y_coordinates, _x_coordinates, _y_coordinates):
    
    plt.plot(x_coordinates, y_coordinates, color = "purple", label = "Before Rotation")
    plt.plot(_x_coordinates, _y_coordinates, color = "blue", label = "After Rotation")
    plt.axis("equal")
    plt.title("2D Transformations (Rotation)", fontsize = 16)
    plt.legend()
    plt.show()

def main():

    x_coordinates = []
    y_coordinates = []
    
    print("Enter the coordinates in clockwise or counter clockwise.")
    for i in range(1, 5):
        temp = input(f"Enter x{i}, y{i} separated by a space : ").split()
        x_coordinates.append(int(temp[0]))
        y_coordinates.append(int(temp[1]))

    print()
    theta = float(input("Enter theta (in degrees) : "))

    x_coordinates.append(x_coordinates[0])
    y_coordinates.append(y_coordinates[0])

    _x_coordinates = []
    _y_coordinates = []

    i = 0
    while(i < len(x_coordinates)):

        _x, _y = get_rotated_coordinates(x_coordinates[i], y_coordinates[i], theta)        
        _x_coordinates.append(_x)
        _y_coordinates.append(_y)
        
        i += 1

    plot_translation(x_coordinates, y_coordinates, _x_coordinates, _y_coordinates)

if(__name__ == "__main__"):
    print()
    main()
    print()