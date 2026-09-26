#!/usr/bin/env python3

def element_at(my_list, idx):
    if idx < 0 or idx >= len(my_list):
        return None
    else:
        return (my_list[idx])

my_list = ["a", "b", "c", "d", "e"]
print(element_at(my_list, 3))
print(element_at(my_list, -1))
print(element_at(my_list, 15))
