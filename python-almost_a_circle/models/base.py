#!/usr/bin/python3
"""Class BASE"""
import json


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

    @classmethod
    def save_to_file(cls, list_objs):
        file_name = cls.__name__ + ".json"
        if list_objs is not None:
            dic = [i.to_dictionary() for i in list_objs]
        else:
            dic = []
        with open(file_name, "w") as file:
            file.write(cls.to_json_string(dic))

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
