#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
a = number % 10
if (a > 5):
    print(f"Last digit of {number} is {a} and is greater than 5\n")
elif (a == 0):
    print(f"Last digit of {number} is {a} and is 0\n")
else:
    print(f"Last digit of {number} is {a} and is less than 6 and not 0\n")
