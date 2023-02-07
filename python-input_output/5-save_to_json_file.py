#!/usr/bin/python3
"""Write a function that returns an object"""


import json


def save_to_json_file(my_obj, filename):
    """Transform a data into file json and write il to file"""

    data = json.dumps(my_obj)
    try:
        with open(filename, "w") as fichier:
            fichier.write(data)
    except:
        raise PermissionError("Permission denied: '{:}'".format(filename))
