#!/usr/bin/env python3

import sys


def my_printf(format_string, param):
    shouldDo = True
    for idx in range(0, len(format_string)):
        if shouldDo:
            if format_string[idx] == '#' and format_string[idx + 1] == 'g':
                number = int(str(int(param))[::-1])
                print(number, end="")
                shouldDo = False
            else:
                print(format_string[idx], end="")
        else:
            shouldDo = True
    print("")


# data = sys.stdin.readlines()
data = ["abc #7.3kjhdf#.10kkjdf df#7kdf",
        "TEST2"]

for i in range(0, len(data), 2):
    my_printf(data[i].rstrip(), data[i + 1].rstrip())
