#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    if (idx < 0) or (idx > len(my_list)):
        new_list = my_list
        return new_list
    else:
        for i in range(len(my_list)):
            if i == idx:
                new_list[i] = element
            else:
                new_list[i] = i
        return new_list
