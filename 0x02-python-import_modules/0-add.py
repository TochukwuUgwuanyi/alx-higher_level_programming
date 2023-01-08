#!/usr/bin/python3

def sum():

    from add_0 import add 
    """Print the sum of 1 and 2"""

    a = 1
    b = 2
    print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
if __name__ == "__main__":
    sum()
