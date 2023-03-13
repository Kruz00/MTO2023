#!/usr/bin/env python3

import sys


def my_printf(format_string, param):
    param = str(param)
    shouldDo = True
    next_index = 0
    for idx in range(0, len(format_string)):
        is_printed = False
        if next_index > idx:
            continue
        if shouldDo:
            if format_string[idx] == '#' and format_string[idx + 1] == 'k':
                print(param.swapcase(), end="")
                shouldDo = False
                is_printed = True
            elif format_string[idx] == '#' and format_string[idx + 1] == '.' and format_string[idx + 2].isdigit():
                end_id = idx + 2
                while format_string[idx + 2: end_id + 1].isdigit():
                    end_id += 1
                    if end_id > len(format_string):
                        break
                end_id -= 1
                if format_string[end_id + 1] != 'k':
                    break
                str_len = int(format_string[idx + 2: end_id + 1])
                print(param[:str_len].swapcase(), end="")
                next_index = end_id + 1
                shouldDo = False
                is_printed = True
            if not is_printed:
                print(format_string[idx].swapcase(), end="")
                is_printed = True
        else:
            shouldDo = True
    print("")


data = sys.stdin.readlines()
# data = ["abc #.8k",
#         "TEST2"]

for i in range(0, len(data), 2):
    my_printf(data[i].rstrip(), data[i + 1].rstrip())
