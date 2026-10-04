#!/usr/bin/env python3
"""Create a class Rectangle that inherits from BaseGeometry"""


class BaseGeometry:
    """foundational concept for geometric shapes.
    It defines behavior that other shape classes will build upon"""
    def area(self):
        """area function with only exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """method validates that a value represents
        a valid positive integer."""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """rectangle under base geometry parent"""
    def __init__(self, width, height):
        """initalising insances"""
        self.__width = width
        self.__height = height

        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        """getting area from width and height"""
        area = self.__width * self.__height
        return area

    def __str__(self):
        """readable string representation of the rectangle"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)


class Square(Rectangle):
    """class Square that inherits from Rectangle"""
    def __init__(self, size):
        """initalising insances"""
        # renaming width and height to size
        self.integer_validator("size", size)

        Rectangle.__init__(self, size, size)
        self.__size = size

    def area(self):
        """getting area from sizet"""
        area = self.__size * self.__size
        return area
