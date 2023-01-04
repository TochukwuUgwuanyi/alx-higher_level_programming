#!/usr/bin/python3
import string
c = string.ascii_lowercase[:4]
d = string.ascii_lowercase[5:16]
e = string.ascii_lowercase[17:]
i = c + d + e
print("{:s}".format(i), end='')
