#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    if idx < 0 or idx > len(my_list):
        return my_list
    else:
        for i in range(len(my_list)):
            if i == idx:
                new_list[i] = element
            else:
                new_list[i] = my_list[i]
        my_list = new_list
        return new_list, my_list
