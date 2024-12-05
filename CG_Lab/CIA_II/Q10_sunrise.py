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

    plt.fill(x_coordinates, y_coordinates, color = "yellow")
    plt.fill(x_coordinates, y_coordinates_negative, color = "yellow")

def draw_sunrise():
    
    boundary_x = [0, 100, 100, 0, 0]
    boundary_y = [0, 0, 50, 50, 0]
    mountains_x = [0, 25, 50, 75, 100, 0]
    mountains_y = [0, 20, 0, 20, 0, 0]

    plt.fill(boundary_x, boundary_y, color = "#1ecbe1")
    plt.fill(mountains_x, mountains_y, color = "#13ec32")
    plot_circle(85, 35, 7)
    
    plt.plot([85, 85], [43, 47], color = "yellow")
    plt.plot([85, 85], [27, 23], color = "yellow")
    plt.plot([93, 97], [35, 35], color = "yellow")
    plt.plot([77, 73], [35, 35], color = "yellow")

    plt.plot([90.95, 93.75], [40.95, 43.75], color = "yellow")  
    plt.plot([79.05, 76.25], [40.95, 43.75], color = "yellow")  
    plt.plot([90.95, 93.75], [29.05, 26.25], color = "yellow")  
    plt.plot([79.05, 76.25], [29.05, 26.25], color = "yellow") 
    
    plt.axis("equal")
    plt.show()

def main():
    print("Plotting, please wait...")
    draw_sunrise()

if(__name__ == "__main__"):
    print()
    main()
    print()
