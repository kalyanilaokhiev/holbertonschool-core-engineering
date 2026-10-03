#!/usr/bin/env python3

for i in range(0, 100):
    # to make sure the last number does not have a ,
    if i == 99:
        end_symbol = '\n'
    else:
        end_symbol = ', '

    # adding 0 infront of 0-9
    if i < 10:
        print("0{}".format(i), end=end_symbol)
    else:
        print(i, end=end_symbol)
