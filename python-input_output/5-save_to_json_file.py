#!/usr/bin/python3
"""Write a function that returns an object"""


import json


def save_to_json_file(my_obj, filename):
    """Transform a data into file json and write il to file"""
    try:
            data = json.dumps(my_obj)
    except:
        raise TypeError("Object of type set is not JSON serializable")
    try:
        with open(filename, "w") as fichier:
            fichier.write(data)
    except:
        raise PermissionError("[Errno 13] Permission denied: '{:}'".format(filename))
try:
    filemame = "file_7"
    data = { 1, 2, 3 }
    save_to_json_file(data, filemame)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    filemame = "no_perm/file_7"
    data = [1, 2, 3]
    save_to_json_file(data, filemame)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))