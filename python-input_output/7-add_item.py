#!/usr/bin/python3
"""Write a script that adds all arguments to a Python list"""


import sys
import json


load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

try:
    my_list = load_from_json_file("add_item.json")
except:
    my_list = []

my_list.append(sys.argv[1:])

save_to_json_file(my_list, "add_item.json")
