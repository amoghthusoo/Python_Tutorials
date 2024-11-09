import matplotlib.pyplot as plt

def get_circle_coordinates(r):
    
    x = 0
    y = r
    p = 1 - r

    x_coordinates = [x]
    y_coordinates = [y]

    while(True):

        if(p < 0):
            x += 1
            p += (2 * x) + 1

            if(x < y):
                x_coordinates.append(x)
                y_coordinates.append(y)
            else:
                break

        elif(p >= 0):
            x += 1
            y -= 1
            p += (-2 * y) + (2 * x) + 1

            if(x < y):
                x_coordinates.append(x)
                y_coordinates.append(y)
            else:
                break

    i = len(x_coordinates) - 1
    while(i >= 0):
        
        x_coordinates.append(y_coordinates[i])
        y_coordinates.append(x_coordinates[i])
        
        i -= 1

    i = len(x_coordinates) - 1
    while(i >= 0):

        x_coordinates.append(x_coordinates[i])
        y_coordinates.append(y_coordinates[i] * -1)

        i -= 1

    i = len(x_coordinates) - 1
    while(i >= 0):

        x_coordinates.append(x_coordinates[i] * -1)
        y_coordinates.append(y_coordinates[i])

        i -= 1

    return x_coordinates, y_coordinates

def plot_circle(x_coordinates, y_coordinates):
    plt.plot(x_coordinates, y_coordinates, color = "purple")
    plt.axis("equal")
    plt.show()

def main():
    
    r = int(input("Enter radius of circle, separated by a space : "))

    print("Plotting, please wait ...")
    x_coordinates, y_coordinates = get_circle_coordinates(r)
    # print(x_coordinates)
    # print(y_coordinates)
    plot_circle(x_coordinates, y_coordinates)

if(__name__ == "__main__"):
    print()
    main()
    print()
