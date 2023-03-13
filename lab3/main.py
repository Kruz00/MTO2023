#!/usr/bin/env python3

import sys
import re


def my_printf(format_string, param):
    m = ''
    strbefore = ""
    strafter = format_string
    while m is not None:
        m = re.search('#(.+?)k', strafter)
        if m is None:
            continue

        #
        strreplace = param
        max_len = len(strreplace)
        min_len = len(strreplace)
        m_temp = re.search(r'\.\d+', m.group(0))
        if m_temp is not None:
            max_len = int(m_temp.group(0)[1:])

        m_temp = re.search(r'\d+\.', m.group(0))
        if m_temp is not None:
            min_len = int(m_temp.group(0)[:-1])
        #

        strreplace = strreplace[:max_len]


        strbefore += strafter[:m.span()[0]]
        strbefore += strreplace
        strafter = strafter[m.span()[1]:]
        str_k = m.group(1)

    format_string = strbefore + strafter

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


# data = sys.stdin.readlines()
data = ["abc #7.3kjhdf#.10kkjdf df#7kdf",
        "TEST2"]

for i in range(0, len(data), 2):
    my_printf(data[i].rstrip(), data[i + 1].rstrip())
