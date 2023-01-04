#!/usr/bin/python3
for letter in range(97, 123):
    if chr(letter) != 101 and chr(letter) != 113:
        print("{}".format(chr(letter)), end="")
