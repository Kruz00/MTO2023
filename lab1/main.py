#!/usr/bin/env python3

import sys

def my_printf(format_string,param):
    #print(format_string)
    shouldDo = True
    string_var = ""
    for idx in range(0,len(format_string)):
        if shouldDo:
            if format_string[idx] == '#' and format_string[idx+1] == 'k':
                string_var = string_var + str(param)
                # print(param, end="")
                shouldDo=False
            else:
                # print(format_string[idx],end="")
                string_var = string_var + str(format_string[idx])
        else:
            shouldDo=True
    print(string_var)

data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())
