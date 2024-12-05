import matplotlib.pyplot as plt

def draw_and_fill_graphic_primitives():
    
    point_x = [1]
    point_y = [2]

    line_x = [3, 7]
    line_y = [2, 6]
    
    square_x = [9, 13, 13, 9, 9]
    square_y = [2, 2, 6, 6, 2]

    plt.plot(point_x, point_y, marker = "o", color = "blue", label = "point")
    plt.plot(line_x, line_y, color = "red", label = "line segment")
    plt.fill(square_x, square_y, color = "green", label = "square")
    plt.axis("equal")
    plt.legend()
    plt.show()

def main():
    print("Plotting, please wait...")
    draw_and_fill_graphic_primitives()

if(__name__ == "__main__"):
    print()
    main()
    print()
