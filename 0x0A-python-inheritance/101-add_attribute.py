#!/usr/bin/python3
"""Module contains a class that inherits from 'int'
"""


def add_attribute(cls, name, first):
    """Assigns new attributes if not already assigned
        Args:
            name (str): name of the attribute to insert
            first (any): value of the attribute to insert
    """
    if not hasattr(cls, name):
        raise TypeError("can't add new attribute")
    cls.name = first
