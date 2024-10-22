import matplotlib.pyplot as plt

def get_line_coordinates(x1, y1, x2, y2):

    try:
        m = (y2 - y1)/(x2 - x1)
    except:
        m = None

    x_coordinates = []
    y_coordinates = []

    if(m == None):

        i = x1
        j = y1

        while(True):
            

            x_coordinates.append(i)
            y_coordinates.append(j)

            if(round(i) == round(x2) and round(j) == round(y2)):
                break
            
            j += 1
            
    elif(m < 1):
        i = x1
        j = y1
        while(True):
            
            
            x_coordinates.append(i)
            y_coordinates.append(j)

            if(round(i) == round(x2) and round(j) == round(y2)):
                break
            
            i += 1
            j += m

    elif(m > 1):
        i = x1
        j = y1
        
        while(True):
            
            x_coordinates.append(i)
            y_coordinates.append(j)
            
            if(round(i) == round(x2) and round(j) == round(y2)):
                break

            i += 1/m
            j += 1


    elif(m == 1):
        i = x1
        j = y1
 
        while(True):
            
            
            x_coordinates.append(i)
            y_coordinates.append(j)
            
            if(round(i) == round(x2) and round(j) == round(y2)):
                break

            i += 1
            j += 1
    
    return x_coordinates, y_coordinates


def plot_line(x_coordinates, y_coordinates):
    plt.plot(x_coordinates, y_coordinates, marker = "o", color = "purple")
    plt.show()

def main():

    point = input("Enter x1, y1 separated by a space : ").split()
    x1 = float(point[0])
    y1 = float(point[1])

    point = input("Enter x2, y2 separated by a space : ").split()
    x2 = float(point[0])
    y2 = float(point[1])

    print("Plotting, please wait ...")
    x_coordinates, y_coordinates = get_line_coordinates(x1, y1, x2, y2)
    # print(x_coordinates)
    # print(y_coordinates)
    plot_line(x_coordinates, y_coordinates)

if(__name__ == "__main__"):
    print()
    main()
    print()
