import matplotlib.pyplot as plt

def get_reflected_coordinates(x, y):    
    _x = -x
    _y = y
    return _x, _y

def plot_reflection(x_coordinates, y_coordinates, _x_coordinates, _y_coordinates):
    
    plt.plot(x_coordinates, y_coordinates, color = "purple", label = "Original Figure")
    plt.plot(_x_coordinates, _y_coordinates, color = "blue", label = "Reflected Figure")
    plt.axis("equal")
    plt.title("2D Transformations (Reflection)", fontsize = 16)
    plt.axhline(color = "black")
    plt.axvline(color = "black")
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

    x_coordinates.append(x_coordinates[0])
    y_coordinates.append(y_coordinates[0])

    _x_coordinates = []
    _y_coordinates = []

    i = 0
    while(i < len(x_coordinates)):

        _x, _y = get_reflected_coordinates(x_coordinates[i], y_coordinates[i])        
        _x_coordinates.append(_x)
        _y_coordinates.append(_y)
        
        i += 1

    print()
    print("Plotting, please wait ...")
    
    plot_reflection(x_coordinates, y_coordinates, _x_coordinates, _y_coordinates)

if(__name__ == "__main__"):
    print()
    main()
    print()