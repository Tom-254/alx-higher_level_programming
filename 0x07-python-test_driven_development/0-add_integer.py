#!/usr/bin/python3

"""add_integer adds integers
"""


def add_integer(a, b=98):
    """Calculates sum of two integers
    Args:
        a(int): the first integer
        b(int): the second integer
    Return:
        int: The sum of a and b
    """
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    if not isinstance(a, int):
        raise TypeError("a must be an integer")
    if not isinstance(b, int):
        raise TypeError("b must be an integer")
    return a + b
