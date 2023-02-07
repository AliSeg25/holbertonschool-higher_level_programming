#!/usr/bin/python3

load_from_json_file = __import__('6-load_from_json_file.py').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file.py').save_to_json_file


import sys

arg = sys.argv[1:]

print(arg)