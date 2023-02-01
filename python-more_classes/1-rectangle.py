#!/usr/bin/python3
"""Define a class"""


class Rectangle:
    """Define a class Rectancle"""

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Return private width"""

        return self.__width
    
    @width.setter
    def width(self, value):
        """Checks the Values"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        
        if value < 0:
            raise TypeError("width must be >= 0")

        self.__width = value
        

    @property
    def height(self):
        """Return private height"""

        return self.__height
    
    @height.setter
    def height(self, value):
        """checks the values"""

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        
        if value < 0:
            raise TypeError("height must be >= 0")
        
        self.__height = value
