#!/usr/bin/python3
"""Define a class"""


class Rectangle:
    """Define a class Rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")

        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        return cls(size, size)

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
            Rec = ""
            for i in range(self.__height):
                Rec += str(self.print_symbol) * self.__width + "\n"\
                    if i < self.height - 1 else str(self.print_symbol) *\
                    self.__width
            return Rec

    def __repr__(self):
        """methode repr"""

        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """Message to god"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
