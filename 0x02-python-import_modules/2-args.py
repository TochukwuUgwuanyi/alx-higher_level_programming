#!/usr/bin/python3

if __name__ == "__main__":
    """Print number of and list of arguments"""
    import sys

    a = len(sys.argv) - 1

    if (len(sys.argv) == 1):
        print("{} arguments.".format(a))
    elif (len(sys.argv) > 1):
        print("{} arguments.".format(a))
    for i in range(a):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
