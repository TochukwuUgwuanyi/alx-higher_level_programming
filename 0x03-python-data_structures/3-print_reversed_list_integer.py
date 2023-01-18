#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    a = my_list[::-1]
    for i in range(len(a)):
        print("{:d}".format(a[i]))
