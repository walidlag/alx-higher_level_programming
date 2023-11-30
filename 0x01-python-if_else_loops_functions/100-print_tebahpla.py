#!/usr/bin/python3
for  a in range(30, -1, -1):
    c = a + ord("A")
    if a % 2 == 1:
        c += 32
        print("{:c}".format(c), end='')
