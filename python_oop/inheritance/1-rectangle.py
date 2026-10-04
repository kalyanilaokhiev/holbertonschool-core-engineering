#!/usr/bin/env python3
from base_geometry import BaseGeometry
"""Create a class Rectangle that inherits from BaseGeometry"""

class Rectangle(BaseGeometry):
    """rectangle under base geometry parent"""
    def __init__(self, width, height):
        """initalising insances"""
        self.__width = width
        self.__height = height

        self.integer_validator("width", width)
        self.integer_validator("height", height)
