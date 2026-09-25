#!/usr/bin/env python3

def islower(c):
    lower = None
    if ord(c) in range(ord('a'), ord('z')):
        lower = True
    else:
        lower = False

    print(lower)
