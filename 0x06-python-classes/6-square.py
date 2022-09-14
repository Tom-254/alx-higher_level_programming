#!/usr/bin/python3

from signal import raise_signal
from typing import Type


class Square:
    """Square representation"""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes the instance attributes
            Args:
                size: size of the square
                position: tuple containing coordinates (x, y)
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Gets the size of the square class instance
           Returns:
                int: size of the square class instance
        """
        return self.__size

    @property
    def position(self):
        """Gets the position the instance square is on a cartesian
            plane
           Returns:
                tuple: contains two values reprenting
                the cartasian coordinates of the square
        """
        return self.__position

    @size.setter
    def size(self, value):
        """Sets the size of the square instance
            Args:
                value (int): the size of square to be set
        """
        if isinstance(value, int):
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
        else:
            raise TypeError("size must be an integer")

    @position.setter
    def position(self, value):
        """Sets the position of the square
            Args:
                value (:obj: `list` of :obj: `str`): contains the
                integer position coordinates (x, y)
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
            any(not isinstance(item, int) for item in value) or
                any(num < 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """ Calculates area of square
            Returns:
                int: Square area calculated
        """
        return (self.__size ** 2)

    def my_print(self):
        """prints out the square representaion with the
            character "#" to the stdout
        """
        if self.__size == 0:
            print()
        else:
            if self.__position[1] > 0:
                print("\n" * self.position[1], end='')

            for i in range(self.__size):
                if self.__position[0] > 0:
                    print(" " * self.__position[0], end='')
                print("#" * self.__size, end='')
                print()
