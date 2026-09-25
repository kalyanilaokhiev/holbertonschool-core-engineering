#!/usr/bin/env python3

def uppercase(str):
    result = ""
    for i in str:
        if ord(i) >= ord('a') and ord(i) <= ord('z'):
            char = ord(i) - 32
            i = chr(char)

            result += i
        else:
            result += i

    return(result)
