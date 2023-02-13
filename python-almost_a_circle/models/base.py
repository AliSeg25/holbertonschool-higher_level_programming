#!/usr/bin/python3
"""Class BASE"""


class Base:
    """Class the Base de notre programme"""
    __nb_objects = 0

    def __init__(self, id=None):
        if not id == None:
            self.id = id
        else:
            Base.__nb_objects +=1
            self.id =  Base.__nb_objects
