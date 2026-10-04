#!/usr/bin/env python3
"""creating base parent class"""


class BaseGeometry:
    """foundational concept for geometric shapes.
    It defines behavior that other shape classes will build upon"""
    def area(self):
        """area function with only exception"""
        raise Exception("not implemented in this class.")

    def integer_validator(self, name, value):
        """method validates that a value represents
        a valid positive integer."""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
