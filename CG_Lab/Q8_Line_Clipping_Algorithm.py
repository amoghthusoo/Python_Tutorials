import matplotlib.pyplot as plt

def get_code(x_min, y_min, x_max, y_max, x, y):
    
    code = [0 for _ in range(4)]

    if(x < x_min):
        code[3] = 1
    if(x > x_max):
        code[2] = 1
    if(y < y_min):
        code[1] = 1
    if(y > y_max):
        code[0] = 1

    return code

def get_bitwise_or(code1, code2):
    
    temp = []

    i = 0
    while(i < len(code1)):
        temp.append(code1[i] | code2[i])
        i += 1

    return temp

def get_bitwise_and(code1, code2):
    
    temp = []

    i = 0
    while(i < len(code1)):
        temp.append(code1[i] & code2[i])
        i += 1

    return temp

def get_intersection_point(x_min, y_min, x_max, y_max, x, y, m, code):

    i = 0
    while(i < len(code)):
        
        if(code[i] == 1):

            if(i == 0):
                _x = x + (y_max - y)/m
                _y = y_max

            elif(i == 1):
                
                _x = x + (y_min - y)/m
                _y = y_min

            elif(i == 2):
                _x = x_max
                _y = y + (x_max - x) * m

            elif(i == 3):
                _x = x_min
                _y = y + (x_min - x) * m
            
            temp = get_code(x_min, y_min, x_max, y_max, _x, _y)
            if(1 not in temp):
                return _x, _y
        
        i += 1

def get_clipped_coordinates(x_min, y_min, x_max, y_max, x1, y1, x2, y2):
    
    p1_code = get_code(x_min, y_min, x_max, y_max, x1, y1)
    p2_code = get_code(x_min, y_min, x_max, y_max, x2, y2)

    bitwise_or = get_bitwise_or(p1_code, p2_code)
    
    if(1 not in bitwise_or):
        return True
    
    else:

        bitwise_and = get_bitwise_and(p1_code, p2_code)
        if(1 in bitwise_and):
            return False
        
        else:
            m = (y2 - y1)/(x2 - x1)
            if(1 in p1_code):
                try:
                    _x1, _y1 = get_intersection_point(x_min, y_min, x_max, y_max, x1, y1, m, p1_code)
                except:
                    return False
            else:
                _x1 = x1
                _y1 = y1

            if(1 in p2_code):
                try:
                    _x2, _y2 = get_intersection_point(x_min, y_min, x_max, y_max, x1, y1, m, p2_code)
                except:
                    return False
            else:
                _x2 = x2
                _y2 = y2

        return [_x1, _y1, _x2, _y2]


def plot_clipped_line(x_min, y_min, x_max, y_max, _x1, _y1, _x2, _y2, x1, y1, x2, y2):
    
    box_x_coordinates = [x_min, x_min, x_max, x_max, x_min]
    box_y_coordinates = [y_min, y_max, y_max, y_min, y_min]
    
    fig, (plot1, plot2) = plt.subplots(1, 2)
    
    plot1.plot(box_x_coordinates, box_y_coordinates, color = "purple")
    plot1.plot([x1, x2], [y1, y2], color = "purple")
    plot1.set_aspect("equal")
    plot1.set_title("Before Clipping")

    plot2.plot(box_x_coordinates, box_y_coordinates, color = "purple")
    plot2.set_aspect("equal")
    plot2.set_title("After Clipping")

    if(x1):
        plot2.plot([_x1, _x2], [_y1, _y2], color = "purple")

    fig.suptitle("Line Clipping", fontsize = "16")
    plt.tight_layout()
    plt.show()
    

def main():
    
    # x_min = 4
    # y_min = 4
    # x_max = 10
    # y_max = 8

    # x1 = 7
    # y1 = 9
    # x2 = 11
    # y2 = 4

    temp = input("Enter x_min, y_min, separated by a space : ").split()
    x_min = int(temp[0])
    y_min = int(temp[1])
    
    temp = input("Enter x_max, y_max, separated by a space : ").split()
    x_max = int(temp[0])
    y_max = int(temp[1])
    
    print()

    temp = input("Enter x1, y1 separated by a space : ").split()
    x1 = int(temp[0])
    y1 = int(temp[1])
    
    temp = input("Enter x2, y2 separated by a space : ").split()
    x2 = int(temp[0])
    y2 = int(temp[1])
    
    print()
    print("Plotting, please wait ...")

    result = get_clipped_coordinates(x_min, y_min, x_max, y_max, x1, y1, x2, y2)
    
    if(result == True):
        plot_clipped_line(x_min, y_min, x_max, y_max, x1, y1, x2, y2, x1, y1, x2, y2)
    elif(not result):
        plot_clipped_line(x_min, y_min, x_max, y_max, False, False, False, False, x1, y1, x2, y2)
    else:
        plot_clipped_line(x_min, y_min, x_max, y_max, result[0], result[1], result[2], result[3], x1, y1, x2, y2)


if(__name__ == "__main__"):
    print()
    main()
    print()
