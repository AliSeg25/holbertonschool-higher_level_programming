#!/usr/bin/python3
"""Class Rectangle"""


Base = __import__('base').Base


class Rectangle(Base):
    """Class retangle qui herite de la class base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id=id)


    @property
    def width(self):
        """Property"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter"""
        self.__width = value

    @property
    def height(self):
        """Property"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter"""
        self.__height = value

    @property
    def x(self):
        """Property"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter"""
        self.__x = value

    @property
    def y(self):
        """Property"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter"""
        self.__y = value

    @property
    def id(self):
        """Property"""
        return self.__id

    @id.setter
    def id(self, value):
        """Setter"""
        self.__id = value
