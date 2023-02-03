#!/usr/bin/python3
"""Define a Class Square"""


class Square:
    """Defining a class square"""
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        """Get/set the current size of the square."""
        return(self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")

    def area(self):
        """Return the area of a square"""
        return(self.__size * self.__size)
