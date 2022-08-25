#!/usr/bin/python3

def uppercase(str):
    for i in str:
        if ord(i) >= 97 and ord(i) <= 122:
            i = chr(ord(i)-32)
        if ord(i) >= 65 and ord(i) <= 91 or ord(i) == ord(" "):
            print(f"{i}", end="")
        else:
            print("")
