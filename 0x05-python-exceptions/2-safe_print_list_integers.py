#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
     q, c = 0, 0
    while q < x:
        try:
            print("{:d}".format(my_list[q]), end='')
            c += 1
        except (TypeError, ValueError):
            pass
        q += 1
    print()
    return c
