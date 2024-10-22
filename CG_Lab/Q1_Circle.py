import matplotlib.pyplot as plt

def plot_circle(a, b, r):

    x_coordinates = []
    y_coordinates = []
    
    x = a - r
    while(x <= a + r):
        
        x_coordinates.append(x)
        y = ((r ** 2 - (x - a) ** 2) ** 0.5 ) + b
        y_coordinates.append(y)
        x += 0.05
        x = round(x, 2)

    y_coordinates_negative = []

    x = a - r
    while(x <= a + r):
        
        y = -((r ** 2 - (x - a) ** 2) ** 0.5) + b
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
    
    point = input("Enter the centre (x, y) of circle, separated by space : ").split()
    a = float(point[0])
    b = float(point[1])
    r = float(input("Enter the radius (r) : "))

    plot_circle(a, b, r)

if(__name__ == "__main__"):
    print()
    main()
    print()
    