#!/usr/bin/python3
"""Define a Rectangle class"""

class Rectangle:
    """Represent rectangle"""

    def __init__(self, width=0, height=0):
        """Instantiation of the rectangle"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """ returns the rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """ returns the rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Create a rectangle using print #"""
        if self.__height == 0 or self.__width == 0:
            return ""
        for q in range(self.__height):
            for j in range(self.__width):
                print("#", end="")
            if q != self.__height - 1:
                print()
        return ""

    def __repr__(self):
        """__repr__ method to enable creating a new instance using the current state #"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)
