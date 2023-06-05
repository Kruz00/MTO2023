#!/usr/bin/env python3

import sys
import re

alphabet = 'abcdefghij'


def my_printf(format_string, param):
    matcher = re.search("#b", format_string)
    if not matcher:
        print(format_string)
        return

    number = int(param)
    out_decimal_reversed = bin(number).replace('0b', '')[::-1]
    out_transformed = ''

    for i in range(len(out_decimal_reversed)):
        if out_decimal_reversed[i] == '0':
            out_transformed += '0'
        else:
            out_transformed += alphabet[i % len(alphabet)]

    out_param = out_transformed[::-1]
    out = format_string.replace(matcher.group(), out_param)

    print(out)


# data = sys.stdin.readlines()
data = ["abc #b",
        "123"]

for i in range(0, len(data), 2):
    my_printf(data[i].rstrip(), data[i + 1].rstrip())
