#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if key in a_dictionary:
        a_dictionary.pop(key)
        return a_dictionary
    else:
        return a_dictionary
print(simple_delete({'a': 1, 'b': 2, 'c': 3}, 'f'))