#!/usr/bin/python3
"""Write a function that returns an object"""


import json


def save_to_json_file(my_obj, filename):
    """Transform a data into file json and write il to file"""
    try:
            data = json.dumps(my_obj)
    except:
        raise PermissionError("[Errno 13] Permission denied: '{:}'".format(filename))
    try:
        with open(filename, "w") as fichier:
            fichier.write(data)
    except:
        raise PermissionError("[Errno 13] Permission denied: '{:}'".format(filename))
