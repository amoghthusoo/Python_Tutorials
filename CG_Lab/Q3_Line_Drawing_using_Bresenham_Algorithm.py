import matplotlib.pyplot as plt

def get_line_coordinates(x1, y1, x2, y2):
    
    dx = x2 - x1
    dy = y2 - y1
    m = dy/dx
    p = (2 * dy) - dx

    x = x1
    y = y1

    x_coordinates = [x1]
    y_coordinates = [y1]

    while(x <= x2):
        
        if(p < 0):
            p += 2 * dy
            x += 1
            
            x_coordinates.append(x)
            y_coordinates.append(y)

        elif(p >= 0):
            p += (2 * dy) - (2 * dx)
            x += 1
            y += 1

            x_coordinates.append(x)
            y_coordinates.append(y)

    return x_coordinates, y_coordinates

def plot_line(x_coordinates, y_coordinates):
    plt.plot(x_coordinates, y_coordinates, marker = "o", color = "purple")
    plt.show()

def main():
    
    point = input("Enter x1, y1 separated by a space : ").split()
    x1 = float(point[0])
    y1 = float(point[1])

    point = input("Enter x2, y2 separated by a space : ").split()
    x2 = float(point[0])
    y2 = float(point[1])

    print("Plotting, please wait ...")
    x_coordinates, y_coordinates = get_line_coordinates(x1, y1, x2, y2)
    # print(x_coordinates)
    # print(y_coordinates)
    plot_line(x_coordinates, y_coordinates)

if(__name__ == "__main__"):
    print()
    main()
    print()

