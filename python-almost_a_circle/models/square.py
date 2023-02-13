#!/usr/bin/python3
"""Class Square"""


from rectangle import Rectangle


class Square(Rectangle):
    """Class Square herite Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        """ La meme valeur """

        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update args""" 

        if args:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.width = args[1]
            if len(args) > 2:
                self._Rectangle__x = args[2]
            if len(args) > 3:
                self._Rectangle__y = args[3]

        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
