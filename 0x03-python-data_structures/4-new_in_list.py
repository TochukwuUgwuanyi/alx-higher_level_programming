#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    i = len(my_list) - 1
    if ((idx < 0) or (idx > i)):
        return (my_list)
    new = [c for c in my_list]
    new[idx] = element
    return (new)
