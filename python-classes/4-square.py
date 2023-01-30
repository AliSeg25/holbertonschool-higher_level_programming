#!/usr/bin/python3
"""This module contains a class called Square"""


class Square:
    """Initialize the square with size """

    def __init__(self, size=0):
        """ Initialize the square with size """
        self.__size = size

    @property
    def size(self):

        """ Initialize the square with size """
        return self.__size

    @size.setter
    def size(self, value):

        """Veriification de la valeur"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):

        """ Return the area of the square """
        return self.size ** 2
