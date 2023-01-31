#!/usr/bin/python3
"""Add integer module."""


def add_integer(a, b=98):
    """
    Add integer function.
    @a: integer or float to be added.
    @b: integer or float to be added (default set to 98).
    Returns the result of the sum.
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    
    return int(a + b)
