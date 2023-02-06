#!/usr/bin/python3
""" function is_same_class"""


def is_same_class(obj, a_class):
    """Return True type(obj) ==  a_class"""

    try :
        if type(obj) is a_class:
            return True
    except:
            return False
