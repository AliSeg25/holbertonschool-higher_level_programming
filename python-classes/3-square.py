#!/usr/bin/python3
"""This module contains a class called Square"""


class Square:
    """ Initialize the square with size """

    def __init__(self, size=0):
        """ Initialize the square with size """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self._size = size

    def area(self):
        """ Return the area of the square """
        return self._size ** 2
