#!/usr/bin/env python3
"""Add validations to the sizeattribute on the Square class."""


class Square:
    """Square that includes a private instance of size"""
    def __init__(self, size=0):
        """initialising size"""
        self.__size = size

        if type(size) is not int:
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")
