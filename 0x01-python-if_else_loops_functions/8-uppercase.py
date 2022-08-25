#!/usr/bin/python3

def uppercase(str):
    for i in str:
        if ord(i) >= 97 and ord(i) <= 122:
            i = chr(ord(i)-32)
        cap = ord(i) >= 65 and ord(i) <= 91
        space = ord(i) == ord(" ") or ord(i) == ord("")
        digit = ord(i) >= 48 and ord(i) <= 57
        if cap or space or digit:
            print("{}".format(i), end="")
        else:
            print("")
