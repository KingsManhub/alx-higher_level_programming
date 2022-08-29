#!/usr/bin/python3

def multiple_returns(sentence):
    if len(sentence) == 0:
        result = (0, None)
        return result
    else:
        length = len(sentence)
        fl = sentence[0]
        result = (length, fl)
        return result
