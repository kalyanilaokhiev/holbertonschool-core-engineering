#!/usr/bin/env python3
"""Add an instance method area(self) to the Square class"""


class Square:
    """Square class that includes instance and methods"""
    def __init__(self, size=0):
        """initialising size"""
        # __ makes size private instance
        self.__size = size

        if type(size) is not int:
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

    # getter
    @property
    def size(self):
        """getting size from init"""
        return self.__size

    # setter
    @size.setter
    def size(self, side):
        """setting size of square"""
        self.__size = side

    def area(self):
        """getting area from size"""
        area = self.__size * self.__size
        return area
