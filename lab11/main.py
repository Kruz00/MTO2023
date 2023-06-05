#!/usr/bin/env python3

import sys
import re


def my_printf(format_string, param):
    matcher = re.search("#b", format_string)
    if not matcher:
        print(format_string)
        return

    number = int(param)
    if number == 0:
        out = format_string.replace(matcher.group(), '0')
    else:
        out = format_string.replace(matcher.group(), str(number))

    print(out)


# data = sys.stdin.readlines()
data = ["abc #b",
        "16"]

for i in range(0, len(data), 2):
    my_printf(data[i].rstrip(), data[i + 1].rstrip())
