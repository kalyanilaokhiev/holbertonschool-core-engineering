#!/usr/bin/env python3
"""Define a class Square with a private instance attribute size"""


class Square:
    """Square that includes a private instance of size"""
    def __init__(self,size):
        """initialising size"""
        self.__size = size
