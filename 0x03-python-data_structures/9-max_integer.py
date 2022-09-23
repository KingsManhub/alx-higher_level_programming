#!/usr/bin/python3


def max_integer(my_list=[]):
    Max = 0
    size = len(my_list)
    if size == 0:
        return None
    else:
        for i in my_list:
            if i > Max:
                Max = i
        return Max
