#!/usr/bin/python3
"""Write a function that returns an object"""


import json


def save_to_json_file(my_obj, filename):
    """Transform a data into file json and write il to file"""

    with open(filename, "w") as f:
        f.write(json.dumps(my_obj))