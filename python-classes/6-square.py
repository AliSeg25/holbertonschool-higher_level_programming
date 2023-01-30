#!/usr/bin/python3
"""This module contains a class called Square"""


class Square:
    """Initialize the square with size """

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):

        """Return the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):

        """Verify the value of the size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):

        """Return the position of the square"""
        return self.__position

    @position.setter
    def position(self, value):

        """Verify the value of the position"""
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(map(lambda x: isinstance(x, int) and x >= 0, value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):

        """Return the area of the square"""
        return self.size ** 2

    def my_print(self):

        """Print the square"""
        if self.size == 0:
            print()
            return
        else:
            for _ in range(self.position[1]):
                print()
            for i in range(self.size):
                print(" " * self.position[0], end="")
                print("#" * self.size)
