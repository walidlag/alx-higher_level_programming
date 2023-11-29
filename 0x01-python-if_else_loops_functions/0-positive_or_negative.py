#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if (number < 0):
    print(f"{number:d} is negative")
elif number > 0:
    print(f"{number} is positive")
else:
    print("{:d} is zero".format(number))
