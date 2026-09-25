#!/usr/bin/env python3

for i in range(0, 10):
    # j will always be 1 more that i
    for j in range(i + 1, 10):
        if i == 8 and j == 9:
            end_symbol = '\n'
        else:
            end_symbol = ', '

        if i != j:
            print("{}{}".format(i, j), end=end_symbol)
