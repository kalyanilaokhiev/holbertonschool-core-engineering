#!/usr/bin/env python3
""" writing in a file """


def write_file(filename="", text=""):
    """function that will open the file and write in it"""
    with open(filename, encoding="utf-8") as f:
        print(f.write(text), end="")
