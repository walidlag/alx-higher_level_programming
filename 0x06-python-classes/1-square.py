#!/usr/bin/python3
"""Square module."""


class Square:
    """Represent a square."""
     
    def __init__(self, size):
        """Initialize a new Square.

        Args:
            size (int): the size of one edge of the square.
        """
        self.__size = size
