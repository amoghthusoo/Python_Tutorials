import matplotlib.pyplot as plt

def plot_points(x_coordinates, y_coordinates):

    plt.scatter(x_coordinates, y_coordinates, marker = "o", color = "purple")
    plt.show()

def main():
    x_coordinates = []
    y_coordinates = []

    n = int(input("Enter the number of points : "))

    for i in range(n):
        point = input(f"Enter x{i + 1}, y{i + 1} separated by space : ").split()
        x_coordinates.append(float(point[0]))
        y_coordinates.append(float(point[1]))

    plot_points(x_coordinates, y_coordinates)

if(__name__ == "__main__"):
    print()
    main()
    print()
