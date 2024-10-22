import matplotlib.pyplot as plt
from Q3_Line_using_DDA_algorithm import get_line_coordinates

def plot_rectangle(l1_x, l1_y, l2_x, l2_y, l3_x, l3_y, l4_x, l4_y):
    plt.plot(l1_x, l1_y, marker = "o", color = "purple")
    plt.plot(l2_x, l2_y, marker = "o", color = "purple")
    plt.plot(l3_x, l3_y, marker = "o", color = "purple")
    plt.plot(l4_x, l4_y, marker = "o", color = "purple")
    plt.show()

def main():
    
    point = input("Enter x, y separated by a space : ").split()
    x1 = float(point[0])
    y1 = float(point[1])

    length = float(input("Enter length of rectangle : "))
    breadth = float(input("Enter breadth of rectangle : "))

    x2 = x1 + length
    y2 = y1

    x3 = x2
    y3 = y2 + breadth

    x4 = x1
    y4 = y1 + breadth

    l1_x, l1_y = get_line_coordinates(x1, y1, x2, y2)
    l2_x, l2_y = get_line_coordinates(x2, y2, x3, y3)
    l3_x, l3_y = get_line_coordinates(x4, y4, x3, y3)
    l4_x, l4_y = get_line_coordinates(x1, y1, x4, y4)    

    plot_rectangle(l1_x, l1_y, l2_x, l2_y, l3_x, l3_y, l4_x, l4_y)
    

if(__name__ == "__main__"):
    print()
    main()
    print()
