#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    list_length = len(my_list) - 1

    if idx < 0 or idx > list_length:
        return my_list

    new_list = my_list[:]
    new_list[idx] = element
    return new_list
