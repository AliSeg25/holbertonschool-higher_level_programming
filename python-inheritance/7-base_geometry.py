#!/usr/bin/python3
"""5. Geometry module"""


class BaseGeometry:
    """class empty"""

    def area(self):
        """Raises an exception"""
        raise Exception('area() is not implemented')
    
    def integer_validator(self, name, value):
        """Fonction Raises an exception"""

        if not isinstance(value, int):
            raise TypeError('<name> must be an integer')
        if value <= 0:
            raise ValueError('<name> must be greater than 0')

