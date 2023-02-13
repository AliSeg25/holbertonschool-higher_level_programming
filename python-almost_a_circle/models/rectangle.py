#!/usr/bin/python3
"""Class Rectangle"""


from base import Base


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

if __name__ == "__main__":

    r1 = Rectangle(10, 2)
    print(r1.id)

    r2 = Rectangle(2, 10)
    print(r2.id)

    r3 = Rectangle(10, 2, 0, 0, 12)
    print(r3.id)