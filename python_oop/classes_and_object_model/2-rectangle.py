#!/usr/bin/env python3
"""Add the following instance methods to the Rectangle class"""


class Rectangle:
    """class to use width and height of rectangle"""
    def __init__(self, width=0, height=0):
        """initalising insances"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """retreive setter"""
        return self.__width

    @width.setter
    def width(self, value):
        """set postions"""
        self.__width = value

        if type(value) is not int:
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        """retreive setter"""
        return self.__height

    @height.setter
    def height(self, value):
        """set postions"""
        self.__height = value

        if type(value) is not int:
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

    def area(self):
        """getting area from width and height"""
        area = self.__width * self.__height
        return area

    def perimeter(self):
        """getting perimeter from width and height"""
        if self.__width == 0 or self.__height == 0:
            perimeter = 0
            return perimeter

        perimeter = (self.__width * 2) + (self.__height * 2)
        return perimeter

Rectangle = __import__('2-rectangle').Rectangle

my_rectangle = Rectangle(10)
print("{} - {} => {} / {}".format(
    my_rectangle.width,
    my_rectangle.height,
    my_rectangle.area(),
    my_rectangle.perimeter()
))