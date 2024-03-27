#!/usr/bin/python3
"""Finds a peak in a sequence of unsorted integers"""


def find_peak(sequence_of_integers):
    """Finds a peak within the given sequence of integers"""

    if sequence_of_integers is None or len(sequence_of_integers) == 0:
        return None

    if len(sequence_of_integers) == 1:
        return sequence_of_integers[0]

    mid_index = len(sequence_of_integers) // 2

    if mid_index != len(sequence_of_integers) - 1:
        if sequence_of_integers[mid_index - 1] < sequence_of_integers[mid_index] and \
           sequence_of_integers[mid_index + 1] < sequence_of_integers[mid_index]:
            return sequence_of_integers[mid_index]
    else:
        if sequence_of_integers[mid_index - 1] < sequence_of_integers[mid_index]:
            return sequence_of_integers[mid_index]
        else:
            return sequence_of_integers[mid_index - 1]

    if sequence_of_integers[mid_index - 1] > sequence_of_integers[mid_index]:
        subsequence = sequence_of_integers[:mid_index]
    else:
        subsequence = sequence_of_integers[mid_index + 1:]

    return find_peak(subsequence)
