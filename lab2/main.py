#!/usr/bin/env python3

import sys


def my_printf(format_string, param):
    param = str(param)
    shouldDo = True
    for idx in range(0, len(format_string)):
        is_printed = False
        if shouldDo:
            if format_string[idx] == '#' and format_string[idx + 1] == 'k':
                print(param.swapcase(), end="")
                shouldDo = False
                is_printed = True
            elif format_string[idx] == '#' and format_string[idx + 1] == '.' and format_string[idx + 2].isdigit():
                end_id = idx + 2
                while format_string[idx + 2: end_id].isdigit():
                    end_id += 1
                end_id -= 1
                if format_string[idx + end_id + 1] != 'k':
                    break
                str_len = int(format_string[idx + 2: end_id])
                print(param[:str_len].swapcase(), end="")
                shouldDo = False
                is_printed = True
            if not is_printed:
                print(format_string[idx].swapcase(), end="")
                is_printed = True
        else:
            shouldDo = True
    print("")


data = sys.stdin.readlines()

for i in range(0, len(data), 2):
    my_printf(data[i].rstrip(), data[i + 1].rstrip())
