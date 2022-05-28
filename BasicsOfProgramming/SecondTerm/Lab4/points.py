"""
Point
"""

import math

class Point:
    """
    Main Point
    """
    def __init__(self, x, y):
        """
        Adds attributes to an object
        >>> poin1 = Point(10, 10)
        >>> print(poin1.x)
        10
        """
        self.x = x
        self.y = y

    def vector_length(self):
        """
        Defines the vector length
        >>> poin1 = Point(10, 10)
        >>> print(poin1.vector_length())
        14.14
        """
        return round(math.sqrt(self.x ** 2 + self.y ** 2), 2)
    def __str__(self):
        """
        Defines what to print
        >>> poin1 = Point(10, 10)
        >>> print(poin1)
        Point in two-dimensional space with coordinates (10, 10)
        """
        return f"Point in two-dimensional space with coordinates ({self.x}, {self.y})"
    def __repr__(self):
        """
        Defines what to print
        >>> poin1 = Point(10, 10)
        >>> print(poin1.x)
        10
        """
        return f"Point(x={self.x}, y={self.y})"

    def __eq__(self, other):
        """
        Equals the parameters
        >>> poin1 = Point3D(10, 10)
        >>> print("Hello")
        Hello
        """
        if not isinstance(other, Point):
            # don't attempt to compare against unrelated types
            return NotImplemented

        return self.x == other.x and self.y == other.y

class Point3D(Point):
    """
    Main Point3d
    """
    def __init__(self, x, y, z = 0):
        """
        Adds attributes to an object
        >>> poin1 = Point3D(10, 10)
        >>> print(poin1.x)
        10
        """
        super().__init__(x, y)
        self.z = z
    def vector_length(self):
        """
        Defines the vector length
        >>> poin1 = Point3D(10, 10)
        >>> print(poin1.vector_length())
        14.14
        """
        return round(math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2), 2)
    def __str__(self):
        """
        Defines what to print
        >>> poin1 = Point3D(10, 10)
        >>> print(poin1)
        Point in three-dimensional space with coordinates (10, 10, 0)
        """
        return f"Point in three-dimensional space with coordinates ({self.x}, {self.y}, {self.z})"
    def __repr__(self):
        """
        Defines what to print
        >>> poin1 = Point3D(10, 10)
        >>> print(poin1.x)
        10
        """
        return f"Point(x={self.x}, y={self.y}, z={self.z})"

    def __eq__(self, other):
        """
        Equals the parameters
        >>> poin1 = Point3D(10, 10)
        >>> print("Hello")
        Hello
        """
        if not isinstance(other, Point3D):
            # don't attempt to compare against unrelated types
            return NotImplemented

        return self.x == other.x and self.y == other.y and self.z == self.y

if __name__ == "__main__":
    point1 = Point(17, 2)
    assert (point1.y, point1.x) == (2, 17)
    assert str(point1) == "Point in two-dimensional space with coordinates (17, 2)"

    point2 = Point3D(17, 4, 2)
    assert (point2.y, point2.z, point2.x) == (4, 2, 17)
    assert str(point2) == "Point in three-dimensional space with coordinates (17, 4, 2)"
    assert str([point1, point2]) == "[Point(x=17, y=2), Point(x=17, y=4, z=2)]"
    assert Point(3, 4).vector_length() == 5
    assert Point(4, 5).vector_length() == 6.4
    assert Point(6, -12).vector_length() == 13.42
    assert Point(100, 0).vector_length() == 100

    assert Point3D(-6, -12, 0).vector_length() == 13.42, Point3D(-6, -12, 0).vector_length()
    assert Point3D(3, 4, 12).vector_length() == 13
    assert Point3D(-13, 14, -15).vector_length() == 24.29
    assert Point(3, 4) == Point(3, 4)
    assert Point(3, 4) != Point(2, 3)

    assert Point(5, 4) == Point3D(5, 4, 0)
    assert Point3D(5, 4, 0) == Point(5, 4)
