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

    plt.plot(x_coordinates, y_coordinates, color = "red", label = "circle")
    plt.plot(x_coordinates, y_coordinates_negative, color = "red")

def plot_arc(a, b, r, start_x, end_x):

    x_coordinates = []
    y_coordinates = []
    
    x = start_x
    while(x <= end_x):
        
        x_coordinates.append(x)
        y = ((r ** 2 - (x - a) ** 2) ** 0.5 ) + b
        y_coordinates.append(y)
        x += 0.05
        x = round(x, 2)

    plt.plot(x_coordinates, y_coordinates, color = "blue", label = "arc")
    
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

    plt.plot(x_coordinates, y_coordinates, color = "orange", label = "ellipse")
    plt.plot(x_coordinates, y_coordinates_negative, color = "orange")

        
def split_and_draw():
    
    div_line_1_x = [10, 10]
    div_line_1_y = [0, 20]
    
    div_line_2_x = [0, 20]
    div_line_2_y = [10, 10]


    rect_x = [12.5, 17.5, 17.5, 12.5, 12.5]
    rect_y = [13, 13, 17, 17, 13]
    
    plot_circle(5, 15, 2.5)
    plot_ellipse(15, 5, 2.5, 2)
    plot_arc(5, 5, 2.5, 3, 6)

    plt.plot(div_line_1_x, div_line_1_y, color = "black")
    plt.plot(div_line_2_x, div_line_2_y, color = "black")
    plt.plot(rect_x, rect_y, color = "green", label = "rectangle")
    plt.axis("equal")
    plt.legend()
    plt.show()
    
def main():
    print("Plotting, please wait...")
    split_and_draw()

if(__name__ == "__main__"):
    print()
    main()
    print()
