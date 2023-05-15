#!/usr/bin/env python3

import sys


def my_printf(format_string, param):
    shouldDo = True
    for idx in range(0, len(format_string)):
        if shouldDo:
            if format_string[idx] == '#' and format_string[idx + 1] == 'j':
                number = int(param)
                out_str = '{:x}'.format(number) \
                    .replace("a", "g") \
                    .replace("b", "h") \
                    .replace("c", "i") \
                    .replace("d", "j") \
                    .replace("e", "k") \
                    .replace("f", "l")\
                    .replace("0", "o")
                print(out_str, end="")
                shouldDo = False
            else:
                print(format_string[idx], end="")
        else:
            shouldDo = True
    print("")


data = sys.stdin.readlines()
# data = ["abc #j",
#         "10"]

for i in range(0, len(data), 2):
    my_printf(data[i].rstrip(), data[i + 1].rstrip())
