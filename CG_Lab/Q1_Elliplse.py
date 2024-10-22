import matplotlib.pyplot as plt

def plot_ellipse(h, k, a, b):

    x_coordinates = []
    y_coordinates = []
    
    x = h - a
    while(x <= h + a):
        
        x_coordinates.append(x)
        y = ((b/a) * (a ** 2 - (x - h) ** 2) ** 0.5) + k
        y_coordinates.append(y)
        x += 0.05
        x = round(x, 2)

    y_coordinates_negative = []

    x = h - a
    while(x <= h + a):
        
        y = -((b/a) * (a ** 2 - (x - h) ** 2) ** 0.5) + k
        y_coordinates_negative.append(y)
        x += 0.05
        x = round(x, 2)

    # print(x_coordinates)
    # print(y_coordinates)

    plt.plot(x_coordinates, y_coordinates, color = "purple")
    plt.plot(x_coordinates, y_coordinates_negative, color = "purple")
    plt.axis("equal")
    plt.show()

def main():
    
    point = input("Enter the centre (x, y) of ellipse, separated by space : ").split()
    h = float(point[0])
    k = float(point[1])
    a = float(input("Enter the semi-major axis (a) : "))
    b = float(input("Enter the semi-minor axis (b) : "))

    plot_ellipse(h, k, a, b)

if(__name__ == "__main__"):
    print()
    main()
    print()
