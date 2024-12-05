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

    plt.fill(x_coordinates, y_coordinates, color = "#e3661b")
    plt.fill(x_coordinates, y_coordinates_negative, color = "#e3661b")

def draw_sunset():
    
    boundary_x = [0, 100, 100, 0, 0]
    boundary_y = [0, 0, 50, 50, 0]

    mountains_x = [0, 25, 50, 75, 100, 0]
    mountains_y = [0, 20, 0, 20, 0, 0]

    plt.fill(boundary_x, boundary_y, color = "#106d79")
    plt.fill(mountains_x, mountains_y, color = "#2a913b")
    plot_circle(85, 35, 7)
    plt.axis("equal")
    plt.show()

def main():
    print("Plotting, please wait...")
    draw_sunset()

if(__name__ == "__main__"):
    print()
    main()
    print()
