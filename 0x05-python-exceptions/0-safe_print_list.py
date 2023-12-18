#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    q = 0
    try:
        while q != x:
            print(my_list[q], end='')
            q += 1
    except IndexError:
        None
    print()
    return q
