#!/usr/bin/python3

def no_c(my_string):
    my_new = my_string.translate({ord(i): None for i in "cC"})
    return (my_new)
