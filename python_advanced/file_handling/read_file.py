#!/usr/bin/env python3
""" reading a file """

def read_file(filename=""):
    """function that will open the file and read it"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
