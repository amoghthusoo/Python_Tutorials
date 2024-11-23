import matplotlib.pyplot as plt

def diamond_in_rectangle(l, b):
    
    rectangle_x = [0, l, l, 0, 0]
    rectangle_y = [0, 0, b, b, 0]

    diamond_x = [l/2, l, l/2, 0, l/2]
    diamond_y = [0, b/2, b, b/2, 0]

    plt.plot(rectangle_x, rectangle_y, color = "purple", label = "rectangle")
    plt.plot(diamond_x, diamond_y, color = "blue", label = "diamond")
    plt.axis("equal")
    plt.legend()
    plt.show()

def main():
    l = int(input("Enter length of rectangle : "))
    b = int(input("Enter breadth of rectangle : "))

    print()
    print("Plotting, please wait...")
    diamond_in_rectangle(l, b)

if(__name__ == "__main__"):
    print()
    main()
    print()