#!/usr/bin/python3
"""Class BASE"""
import json
#from models.base import Base
#from models.rectangle import Rectangle


class Base:
    """Class the Base de notre programme"""
    __nb_objects = 0

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return JSON string representation of a list of dictionaries"""

        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

