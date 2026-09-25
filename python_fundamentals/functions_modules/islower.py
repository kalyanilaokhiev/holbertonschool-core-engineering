#!/usr/bin/env python3

def islower(c):
    lower = None
    if ord(c) >= ord('a') and ord(c) <= ord('z'):
        lower = True
    else:
        lower = False

    print(lower)
