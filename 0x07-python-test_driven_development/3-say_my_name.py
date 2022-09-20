#!/usr/bin/python3
"""Joins uses both arguments to print out a statement
"""


def say_my_name(first_name, last_name=""):
    """Joins uses both arguments to print out a statement
    Args:
        first_name (str): the first string
        last_name (str): the second string
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
