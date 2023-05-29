#!/usr/bin/env python3

import sys


def my_printf(format_string, param):
    shouldDo = True
    for idx in range(0, len(format_string)):
        if shouldDo:
            if format_string[idx] == '#' and format_string[idx + 1] == 'a':

                number = int(param)
                number_of_digits = len(str(abs(number)))

                final_number = int((number * 2) / number_of_digits)

                if final_number % 2 == 0:
                    out_str = str(final_number)
                else:
                    out_str = '{:x}'.format(number)

                print(out_str, end="")
                shouldDo = False
            else:
                print(format_string[idx], end="")
        else:
            shouldDo = True
    print("")


data = sys.stdin.readlines()
# data = ["abc #a",
#         "16"]

for i in range(0, len(data), 2):
    my_printf(data[i].rstrip(), data[i + 1].rstrip())
