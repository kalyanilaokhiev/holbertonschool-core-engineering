#!/usr/bin/env python3
"""Use object state to generate output."""


class Square:
    """Square class that includes instance and methods"""
    def __init__(self, size=0):
        """initialising size"""
        # __ makes size private instance
        self.__size = size

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

        if type(side) is not int:
            raise TypeError("size must be an integer")

        if side < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """getting area from size"""
        area = self.__size * self.__size
        return area

    def my_print(self):
        if self.size == 0:
            print("")

        print ("#" * self.area())
