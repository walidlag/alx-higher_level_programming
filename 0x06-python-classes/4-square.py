#!/usr/bin/python3
"""Defines a class aquare."""


class Square:
    """Defines a class aquare."""

    def __init__(self, size=0):
        """initialize square
        Args:
            size (int): size of the square
        """
        self.__size = size

    @property
    def size(self):
        """initialize square
        Args:
            size (int): size of the square
        """
        return self.__size

    @size.setter
        if type(size) is not int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size  #: size of the square

    def area(self):
        """Area of this square

        Returns:
            The square of the size
        """
        return self.__size**2
