#!/usr/bin/python3
import string
for i in (string.ascii_lowercase[:4]+string.ascii_lowercase[5:16]+string.ascii_lowercase[17:]):
    print("{:s}".format(i), end='')
