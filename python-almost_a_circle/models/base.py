#!/usr/bin/python3
"""Class BASE"""


class Base:
    __nb_objects = 0
    def __init__(self, id=None):
        if not id == None:
            self.id = id
        else:
            Base.__nb_objects +=1
            self.id =  Base.__nb_objects
