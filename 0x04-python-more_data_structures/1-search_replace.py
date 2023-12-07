#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = list(map(lambda q: replace if q == search else q, my_list))
    return (new_list)
