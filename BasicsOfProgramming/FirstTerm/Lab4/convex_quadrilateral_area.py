import math

def four_lines_area(k1, c1, k2, c2, k3, c3, k4, c4):
    x1, y1 = lines_intersection(k1, c1, k2, c2)
    x2, y2 = lines_intersection(k2, c2, k3, c3)
    x3, y3 = lines_intersection(k3, c3, k4, c4)
    x4, y4 = lines_intersection(k4, c4, k1, c1)
    a = distance(x1, y1, x2, y2)
    b = distance(x2, y2, x3, y3)
    c = distance(x3, y3, x4, y4)
    d = distance(x4, y4, x1, y1)
    f1 = distance(x1, y1, x3, y3)
    f2 = distance(x2, y2, x4, y4)
    area = quadrangle_area(a, b, c, d, f1, f2)
    return area


def lines_intersection(k1, c1, k2, c2):
    if k1==k2:
        return None
    x1 = round((c1-c2)/(k2-k1),2)
    y1 = round((k2 * c1-k1 * c2) / (k2-k1), 2)
    return x1, y1


def distance(x1, y1, x2, y2):
    a = round(math.sqrt((x2-x1)**2+(y2-y1)**2),2)
    return a



def quadrangle_area(a, b, c, d, f1, f2):
    area = round(math.sqrt((4*(f1**2)*(f2**2)-(b**2+d**2-a**2-c**2)**2)/16), 2)
    if area>0:
        return area
    else:
        return None
