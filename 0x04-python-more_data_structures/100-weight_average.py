#!/usr/bin/python3
def weight_average(my_list=[]):
    weighted_sum = 0
    total_weight = 0

    for item in my_list:
        if len(item) == 2 and isinstance(item[0], int) and isinstance(item[1], int):
            weighted_sum += item[0] * item[1]
            total_weight += item[1]

    if total_weight == 0:
        return 0

    return weighted_sum / total_weight
