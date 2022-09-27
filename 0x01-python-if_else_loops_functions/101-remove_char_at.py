#!/usr/bin/python3


def remove_char_at(str, n):
    strlen = len(str)
    new_file = ""
    for i in range(strlen):
        if i == n:
            continue
        new_file = new_file + str[i]
    return new_file
