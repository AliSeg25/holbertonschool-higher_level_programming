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

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or json_string == "[]":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        file_name = cls.__name__ + ".json"
        if list_objs is not None:
            dic = [i.to_dictionary() for i in list_objs]
        else:
            dic = []
        with open(file_name, "w") as file:
            file.write(cls.to_json_string(dic))

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            instance = cls(1, 1)
        else:
            instance = cls(1)
        instance.update(**dictionary)
        return instance

    @classmethod
    def load_from_file(cls):
        file_name = cls.__name__ + ".json"
        try:
            with open(file_name, "r") as file:
                file = file.read()
        except FileNotFoundError:
            return []

        liste_json = cls.from_json_string(file)
        liste_instance = []

        for el in liste_json:
            instance = cls.create(**el)
            liste_instance.append(instance)

        return liste_instance

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
