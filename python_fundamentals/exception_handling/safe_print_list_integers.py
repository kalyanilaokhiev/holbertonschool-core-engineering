#!/usr/bin/env python3

def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
            int(my_list[i])
            print("{}".format(my_list[i]), end="")
            count += 1
        except ValueError:
            continue
        except TypeError:
            continue

    print("")
    return count
