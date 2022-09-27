#!/usr/bin/python3
"""returns a list of lists of integers
    representing the Pascal’s triangle of n
"""


def pascal_triangle(n):
    """returns a list of lists of integers
    representing the Pascal’s triangle of n
    """
    if n <= 0:
        return []

    p_list = []
    for j in range(1, n + 1):
        C = 1
        row = []
        for i in range(1, j + 1):
            row.append(C)
            C = C * (i - j) // j
        p_list.append(row)
    return p_list
