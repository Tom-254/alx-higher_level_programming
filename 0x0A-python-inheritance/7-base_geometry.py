#!/usr/bin/python3
"""
Holds the class superclass BaseGeometry
"""


class BaseGeometry:
    """BaseGeometry class containing area and integer_validator
    """

    def __init__(self):
        """Initializes the class
        """
        pass

    def area(self):
        """Raises and exception when called
        """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates input passed to match conditions provided
        """

        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
