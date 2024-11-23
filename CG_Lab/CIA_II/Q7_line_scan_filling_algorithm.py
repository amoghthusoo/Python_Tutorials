import matplotlib.pyplot as plt

def get_y_min_max(coordinates):

    y_min = coordinates[0][1]
    y_max = coordinates[0][1]

    i = 1
    while(i < len(coordinates)):
        
        if(coordinates[i][1] > y_max):
            y_max = coordinates[i][1]
        
        if(coordinates[i][1] < y_min):
            y_min = coordinates[i][1]

        i += 1

    return y_min, y_max

def main():
    
    coordinates = [[0, 0], [100, 0], [100, 100], [50, 50], [0, 100]]
    
    _coordinates = [c for c in coordinates]
    _coordinates.append(coordinates[0])
    
    y_min, y_max = get_y_min_max(coordinates)
    

    x_coordinates = []
    y_coordinates = []

    scan_line = y_min
    while(scan_line <= y_max):

        intersection_points = []

        i = 0
        while(i < len(_coordinates) - 1):

            p1 = _coordinates[i]   
            p2 = _coordinates[i + 1]

            max_p_y = max(p1[1], p2[1])
            min_p_y = min(p1[1], p2[1])

            if(not (min_p_y <= scan_line <= max_p_y)):
                i += 1
                continue

            dy = p2[1] - p1[1]
            dx = p2[0] - p1[0]

            if(dy == 0):
                i += 1
                continue
            elif(dx == 0):
                intersection = [p1[0], scan_line]
            else:
                m = dy/dx
                c = p1[1] - (m * p1[0])
                x = (scan_line - c)/m
                intersection = [x, scan_line]

            if(intersection in coordinates):
                
                index = coordinates.index(intersection)

                if(index == len(coordinates) - 1):
                    
                    if((coordinates[0][1] > scan_line and coordinates[index - 1][1] > scan_line) or
                   (coordinates[0][1] < scan_line and coordinates[index - 1][1] < scan_line)):
                        intersection_points.append(intersection)
                        intersection_points.append(intersection)
                    else:
                        intersection_points.append(intersection)

                elif((coordinates[index + 1][1] > scan_line and coordinates[index - 1][1] > scan_line) or
                   (coordinates[index + 1][1] < scan_line and coordinates[index - 1][1] < scan_line)):
                    intersection_points.append(intersection)
                    intersection_points.append(intersection)
                
                else:
                    intersection_points.append(intersection)

            else:
                intersection_points.append(intersection)
            
            i += 1

        intersection_points.sort()

        i = 0
        while(i < len(intersection_points) - 1):
            
            p1 = intersection_points[i]
            p2 = intersection_points[i + 1]
            
            j = p1[0]
            while(j <= p2[0]):
                x_coordinates.append(j)
                y_coordinates.append(p1[1])

                j += 1
            
            i += 2

        scan_line += 1

    poly_x_coordinates = []
    poly_y_coordinates = []

    for coordinate in _coordinates:
        poly_x_coordinates.append(coordinate[0])
        poly_y_coordinates.append(coordinate[1])

    print("Plotting, please wait ...")
    plt.plot(poly_x_coordinates, poly_y_coordinates, color = "purple")
    plt.scatter(x_coordinates, y_coordinates, color = "purple")
    plt.axis("equal")
    plt.show()

if(__name__ == "__main__"):
    print()
    main()
    print()
