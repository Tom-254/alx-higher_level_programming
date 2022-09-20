#!/usr/bin/python3
"""Module to find the max integer in a list
"""


def max_integer(list=[]):
    """Finds the max integer in a list of integers
       Args:
            list (list): list of integers
       Returns:
            int: maximum integer in the list
    """
    length = len(list)
    if length == 0:
        return None
    result = list[0]
    i = 1
    while i < length:
        if list[i] > result:
            result = list[i]
        i += 1
    return result
