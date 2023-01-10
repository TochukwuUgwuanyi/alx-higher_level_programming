#!/usr/bin/python3


if __name__ == "__main__":
    """Print the number of and list of arguments."""
    import sys

    a = len(sys.argv) - 1
    if (a == 0):
        print("0 arguments.")
    elif (a == 1):
        print("1 argument:")
    else:
        print("{} arguments:".format(a))
    for i in range(a):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
