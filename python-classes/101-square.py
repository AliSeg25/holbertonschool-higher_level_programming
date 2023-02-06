#!/usr/bin/python3
"""Print square instance"""

class Square:
    """The class square"""

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position
        self.a = []

    @property
    def size(self):
        return self.__size
    
    @size.setter
    def size(self, value):
        """check Value"""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        
        if value < 0:
            raise ValueError("size must be >= ")
        
        self.__size = value
        


    @property
    def position(self):
        return self.__position
    
    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) and len(value) == 2 and isinstance(value[0], int) and isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integer")
        
        self.__position = value
    
    def area(self):
        return self.size * self.size
    
    def my_print(self):
        value = self.__size
        for i in range(self.__size):
            self.a.appennd("#" * value)
    
    def __str__(self):
        return self.a

my_square = Square(5, (0, 0))
print(my_square)
