#!/usr/bin/python3
"""Module of addition function"""


def add_integer(a, b=98):

    """
    Add two integer values together.
    If a float is encountered, it converts to an integer first before adding.
    Args:
        a(int): 'a'parameter of add_integer which will take the first argument
        b=98(int): 'b'parameter takse the second argument with 98 as defualt
    TypeError:
        raises a TypeError when the args are not int or float
    """
    if (type(a) in [int, float] and not (type(b) in [int, float])):
        raise TypeError("b must be an integer")
    elif (not (type(a) in [int, float]) and type(b) in [int, float]):
        raise TypeError("a must be an integer")
    elif not ((type(a) in [int, float]) and type(b) in [int, float]):
        raise TypeError("a must be an integer")
    return int(a)+int(b)
