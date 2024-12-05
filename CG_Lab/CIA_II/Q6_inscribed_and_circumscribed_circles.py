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
    
    x = a + r
    x_coordinates.append(x)
    y = ((r ** 2 - (x - a) ** 2) ** 0.5 ) + b
    y_coordinates.append(y)

    y_coordinates_negative = []

    x = a - r
    while(x <= a + r):
        
        y = -((r ** 2 - (x - a) ** 2) ** 0.5) + b
        y_coordinates_negative.append(y)
        x += 0.05
        x = round(x, 2)

    x = a + r
    y = -((r ** 2 - (x - a) ** 2) ** 0.5) + b
    y_coordinates_negative.append(y)

    # print(x_coordinates)
    # print(y_coordinates)

    plt.plot(x_coordinates, y_coordinates, color = "green")
    plt.plot(x_coordinates, y_coordinates_negative, color = "green")
      
def inscribed_and_circumscribed_circles():
    
    triangle_in_x = [0, 5, 2.5, 0]
    triangle_in_y = [0, 0, 4.3301, 0]

    plot_circle(2.5, 1.4434, 1.4434)
    plot_circle(10, 2.16505, 2.16505)

    triangle_out_x = [10, 8.124622, 11.875378, 10]
    triangle_out_y = [4.3301, 1.082525, 1.082525, 4.3301]

    rectangle_x = [0, 12.16505, 12.16505, 0, 0]
    rectangle_y = [0, 0, 4.3301, 4.3301, 0]

    plt.plot(triangle_in_x, triangle_in_y, color = "blue")
    plt.plot(triangle_out_x, triangle_out_y, color = "blue")
    plt.plot(rectangle_x, rectangle_y, color = "red")
    plt.axis("equal")
    plt.show()

def main():

    print("Plotting, please wait...")
    inscribed_and_circumscribed_circles()

if(__name__ == "__main__"):
    print()
    main()
    print()
