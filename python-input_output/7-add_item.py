#!/usr/bin/python3

load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


import sys

file = "add_item.json"

arg = sys.argv[1:]
json = load_from_json_file(arg)
with open(file, "w") as file:
    file.write(json)

print(json)