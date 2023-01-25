#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if not a_dictionary:
        return a_dictionary
    for i, j in list(a_dictionary.items()):
        if j == value:
            del a_dictionary[i]
    return a_dictionary
