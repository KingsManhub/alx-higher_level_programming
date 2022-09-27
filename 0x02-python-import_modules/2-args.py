#!/usr/bin/python3


def print_arg(argv):
    size = len(argv) - 1
    if size == 0:
        print("{:d} arguments.".format(size))
    elif size == 1:
        print("{:d} argument:".format(size))
        print("{:d}: {:s}".format(size, argv[size]))
    elif size > 1:
        print("{:d} arguments:".format(size))
        for i in range(1, size+1):
            print("{:d}: {:s}".format(i, argv[i]))


if __name__ == '__main__':

    from sys import argv
    print_arg(argv)
