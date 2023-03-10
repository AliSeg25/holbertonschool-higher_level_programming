#!/usr/bin/python3
"""Class Rectangle"""


from .base import Base


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
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        """Property"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        """Property"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")

        if not value >= 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Property"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")

        if not value >= 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    @property
    def id(self):
        """Property"""
        return self.__id

    @id.setter
    def id(self, value):
        """Setter"""
        self.__id = value

    def area(self):
        """Area Rectangle"""

        return self.height * self.width

    def display(self):
        """Display the rectangle with #"""
        for i in range(self.height):
            for j in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)

    def display(self):
        """Recatngle # et"""

        for i in range(self.y):
            print("")
        for i in range(self.height):
            print(" "*self.x + "#"*self.width)

    def update(self, *args, **kwargs):
        """Update args"""

        if args:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.width = args[1]
            if len(args) > 2:
                self.height = args[2]
            if len(args) > 3:
                self.x = args[3]
            if len(args) > 4:
                self.y = args[4]

        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of the square instance"""

        return {'id': self.id, 'width': self.width,
                'height': self.height, 'x': self.x, 'y': self.y}
