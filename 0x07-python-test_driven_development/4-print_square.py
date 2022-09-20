#!/usr/bin/python3
"""
Prints square representation
"""


def print_square(size):
    """Prints a square with "#"'s that has a length of size
    Args:
        size (int): The size of the square
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size > 0:
        print(("#" * size + "\n") * size, end="")
