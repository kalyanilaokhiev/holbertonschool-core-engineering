#!/usr/bin/env python3

def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    else:
        key = None
        biggest = max(a_dictionary, key=a_dictionary.get)
        return biggest
