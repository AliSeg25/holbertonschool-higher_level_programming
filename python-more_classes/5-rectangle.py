#!/usr/bin/python3
"""Define a class"""


class Rectangle:
    """Define a class Rectangle"""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """Return private width"""

        return self.__width

    @width.setter
    def width(self, value):
        """Check the values"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise TabError("width must be >= 0")

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
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """Return rectancle area"""

        if self.__height == 0 or self.__width == 0:
            return 0
        return self.__height * self.__width

    def perimeter(self):
        """Return rectangle perimeter"""

        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__height + self.__width)

    def __str__(self):
        """Print #"""

        if self.__height == 0 or self.__width == 0:
            return ""

        else:
            Rectangle = ""
            for i in range(self.__height):
                Rectangle += "#" * self.__width + "\n"\
                    if i < self.height - 1 else "#" * self.__width
            return Rectangle

    def __repr__(self):
        """methode repr"""

        return "Rectangle({}, {})".format(self.width, self.height)
    
    def __del__(self):
        """Message to god"""

        print("Bye rectangle...")
