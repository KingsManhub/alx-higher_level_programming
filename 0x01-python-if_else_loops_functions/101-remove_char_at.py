#!/usr/bin/python3


def remove_char_at(str, n):
    strlen = len(str)
    for i in range(strlen):
        if i == n:
            continue
        print("{}".format(str[i]), end="")
