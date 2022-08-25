#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        num = abs(number) % 10
        num *= -1
    else:
        num = number % 10
    return num
