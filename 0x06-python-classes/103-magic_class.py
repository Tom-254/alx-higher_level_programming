#!/usr/bin/python3
"""Defines a class MagicClass"""
import math


class MagicClass:
    """MagicClass Circle represention"""

    def __init__(self, radius=0):
        """Initilizes the MagicClass Instance
            Args:
                radius (int): the radius of a circle
        """
        if type(radius) is not int or type(radius) is not float:
            raise TypeError('radius must be a number')

        self.__radius = radius

    def area(self):
        """Calculates the area
            Returns:
                float: the area of the circle
        """
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        """Calculates the circumference
            Returns
                float: the circumference of the circle
        """
        return 2 * math.pi * self.__radius
