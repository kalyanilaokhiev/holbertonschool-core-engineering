#!/usr/bin/env python3
""" appending in a file """


def append_write(filename="", text=""):
    """function that will open the file and append to it"""
    with open(filename, mode="a", encoding="utf-8") as f:
        return (f.write(text))
