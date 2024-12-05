import matplotlib.pyplot as plt

def reflect_triangular_polygon():
    
    triangle_x = [-1, 0, 1, -1]
    triangle_y = [0, -2, 0, 0]

    line_x = [-5, 5]
    line_y = [-3, 7]

    refl_triangle_x = []
    refl_triangle_y = []

    i = 0
    while(i < len(triangle_x)):
        
        refl_triangle_x.append(triangle_y[i] - 2)
        refl_triangle_y.append(triangle_x[i] + 2)
        i += 1

    plt.plot(triangle_x, triangle_y, color = "red", label = "original figure")
    plt.plot(line_x, line_y, color = "orange")
    plt.plot(refl_triangle_x, refl_triangle_y, color = "green", label = "reflected figure")
    plt.axis("equal")
    plt.legend()
    plt.show()

def main():
    print("Plotting, please wait...")
    reflect_triangular_polygon()

if(__name__ == "__main__"):
    print()
    main()
    print()
