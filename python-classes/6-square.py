#!/usr/bin/python3
class Square:
    """Initialize the square with size """

    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):

        """Initialize the square with size """
        return self.__size

    @size.setter
    def size(self, value):

        """Veriification de la valeur"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):

        """Initialize the square with size """
        return self.__position

    @position.setter
    def position(self, value):

        """Veriification de la valeur"""
        for i in range(len(self.position)):
            if not isinstance(value[i], int):
                raise TypeError("position must be a tuple of\
                                 2 positive integers")
            if self.position[i] < 0:
                raise TypeError("position must be a tuple of\
                                 2 positive integers")
        self.__position = value

    def area(self):

        """ Return the area of the square """
        self.size **= 2

    def my_print(self):

        """Print #"""
        if self.size == 0:
            print()
        else:
            for i in range(self.size):
                for j in range(self.position[0]):
                    print("_", end="")
                for k in range(self.size):
                    print("#", end="")
                print()
