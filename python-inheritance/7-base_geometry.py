#!/usr/bin/python3
"""5. Geometry module"""


class BaseGeometry:
    """class empty"""

    def area(self):
        """Raises an exception"""
        raise Exception('area() is not implemented')


    def integer_validator(self, name, value):
        """Fonction Raises an exception"""

        if not type(value) is int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
