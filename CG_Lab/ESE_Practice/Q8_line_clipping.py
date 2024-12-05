import matplotlib.pyplot as plt

def get_code(x_min, x_max, y_min, y_max, x, y):

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

def get_bitwise_or(c1, c2):

    bitwise_or = []

    i = 0
    while(i < len(c1)):

        bitwise_or.append(c1[i] | c2[i])
        i += 1

    return bitwise_or

def get_bitwise_and(c1, c2):

    bitwise_and = []

    i = 0
    while(i < len(c1)):

        bitwise_and.append(c1[i] & c2[i])
        i += 1
    
    return bitwise_and

def get_intersection_points(x_min, x_max, y_min, y_max, x, y, m, code):


    i = 0
    while(i < len(code)):

        if(code[i] == 1):

            if(i == 0):
                _x = x + (y_max - y) / m
                _y = y_max

            elif(i == 1):
                _x = x + (y_min - y) / m
                _y = y_min

            elif(i == 2):
                _x = x_max
                _y = y + (x_max - x) * m

            elif(i == 3):
                _x = x_min
                _y = y + (x_min - x) * m

            temp = get_code(x_min, x_max, y_min, y_max, _x, _y)
            if(1 not in temp):
                return _x, _y

        i += 1

x_min = 5
x_max = 12
y_min = 5
y_max = 10

x1 = 7
y1 = 13

x2 = 13
y2 = 5

p1_code = get_code(x_min, x_max, y_min, y_max, x1, y1)
p2_code = get_code(x_min, x_max, y_min, y_max, x2, y2)

bor = get_bitwise_or(p1_code, p2_code)
if(1 not in bor):
    _x1 = x1
    _y1 = y1
    _x2 = x2
    _y2 = y2

else:

    band = get_bitwise_and(p1_code, p2_code)

    if(1 in band):
        _x1 = None
        _y1 = None
        _x2 = None
        _y2 = None

    else:
        if(1 not in p1_code):
            _x1 = x1
            _x2 = x2
        else:
            try:
                m = (y2 - y1)/(x2 - x1)
                _x1, _y1 = get_intersection_points(x_min, x_max, y_min, y_max, x1, x2, m, p1_code)
            except:
                _x1 = None
                _y1 = None

        if(1 not in p2_code):
            _x2 = x2
            _y2 = y2
        else:
            try:
                m = (y2 - y1)/(x2 - x1)
                _x2, _y2 = get_intersection_points(x_min, x_max, y_min, y_max, x2, y2, m, p2_code)
            except:
                _x2 = None
                _y2 = None

box_x_coor = [x_min, x_max, x_max, x_min, x_min]
box_y_coor = [y_min, y_min, y_max, y_max, y_min]
plt.plot(box_x_coor, box_y_coor, color = "purple")
plt.plot([_x1, _x2], [_y1, _y2])
plt.axis("equal")
plt.show()