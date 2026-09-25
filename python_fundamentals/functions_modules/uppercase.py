#!/usr/bin/env python3

def uppercase(str):
    for i in str:
        if ord(i) >= ord('a') and ord(i) <= ord('z'):
            char = ord(i) - 32
            char = chr(char)
        else:
            char = i
        print("{}".format(char), end="")
    print("")
