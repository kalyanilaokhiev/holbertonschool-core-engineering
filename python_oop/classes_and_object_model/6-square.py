#!/usr/bin/env python3
"""Control how objects are represented as strings."""


class Square:
    """Square class that includes instance and methods"""
    def __init__(self, size=0, position=(0, 0)):
        """initialising instances"""
        # __ makes size private instance
        self.__size = size
        self.position = position

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

    @property
    def position(self):
        """retreive setter"""
        return self.__position

    @position.setter
    def position(self, value):
        """set postions"""
        self.__position = value

        if (type(value) is not tuple or
                len(value) != 2 or
                type(value[0]) is not int or type(value[1]) is not int or
                value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """getting area from size"""
        area = self.__size * self.__size
        return area

    def my_print(self):
        """printing the total as hashags"""
        if self.size == 0:
            print("")
            return

        for i in range(self.__position[1]):
            print("")

        # prints each line of size seperatly
        for i in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
