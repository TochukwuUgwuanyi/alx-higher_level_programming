#!/usr/bin/python3
"""Define a Class Square"""


class Square:
    """Defining a class square"""
    def __init__(self, size=0):
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
