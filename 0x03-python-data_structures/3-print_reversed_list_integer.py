#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    for(i = len(my_list) - 1; i >= 0; i -= 1):
        print('{:d}'.format(my_list[i]))
