#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for q in range(x):
            if type(my_list[q]) is int:
                print("{:d}".format(my_list[q]), end="")
                count += 1
    except ValueError and TypeError:
        return
    else:
        print()
        return count
