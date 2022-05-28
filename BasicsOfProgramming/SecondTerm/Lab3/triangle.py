"""Triangle"""
import point
from math import sqrt

class Triangle:
    """
    Main Triangle
    """
    def __init__(self, ver1, ver2, ver3):
        """
        Adding attributes to a class
        >>> triangle = Triangle(point.Point(1,1), point.Point(3,1),\
point.Point(2,3))
        >>> print(triangle.ver1.x)
        1
        """
        self.ver1 = ver1
        self.ver2 = ver2
        self.ver3 = ver3
    def area(self):
        """
        Evaluates the triangle area
        >>> triangle = Triangle(point.Point(1,1), point.Point(3,1), \
point.Point(2,3))
        >>> print(triangle.area())
        2.0
        """
        area = sqrt((self.perimeter() / 2) * ((self.perimeter() / 2) - \
distance(self.ver1.x, self.ver1.y, self.ver2.x, self.ver2.y)) * \
((self.perimeter() / 2) - distance(self.ver1.x, self.ver1.y, \
self.ver3.x, self.ver3.y)) * ((self.perimeter() / 2) - \
distance(self.ver2.x, self.ver2.y, self.ver3.x, self.ver3.y)))
        return area
    def is_triangle(self):
        """
        Checks whether this figure could be triangle
        >>> triangle = Triangle(point.Point(1,1), point.Point(3,1),\
point.Point(2,3))
        >>> triangle.is_triangle()
        True
        """
        if self.area() == 0:
            return False
        else:
            return True
    def perimeter(self):
        """
        Evaluates a triangle perimeter
        >>> triangle = Triangle(point.Point(1,1), point.Point(3,1),\
point.Point(2,3))
        >>> print(triangle.perimeter())
        6.47213595499958
        """
        return distance(self.ver1.x, self.ver1.y, self.ver2.x, self.ver2.y)\
+ distance(self.ver1.x, self.ver1.y, self.ver3.x, self.ver3.y) +\
distance(self.ver2.x, self.ver2.y, self.ver3.x, self.ver3.y)


def distance(iksa,igra,iksb,igrb):
    """
    Returns the side distance
    >>> print(distance(1,1,3,1))
    2.0
    """
    return sqrt((iksa-iksb)*(iksa-iksb)+(igra-igrb)*(igra-igrb))
