#!/usr/bin/python3
"""Defines Square class"""


class Square:
    """Square representation"""

    def __init__(self, size=0):
        """Initializes the instance attributes
            Args:
                size: size of the square
        """
        if isinstance(size, int):
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        else:
            raise TypeError("size must be an integer")

    @property
    def size(self):
        """Gets the size of the square class instance
           Returns:
                int: size of the square class instance
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square instance
            Args:
                value (int): the size of square to be set
        """
        self.__init__(value)

    def area(self):
        """ Calculates area of square
            Returns:
                int: Square area calculated
        """
        return (self.__size ** 2)

    def __lt__(self, other):
        """
            checks if less than another
            instance object <
        """
        return (self.area() < other.area())

    def __le__(self, other):
        """
            checks if less than or equal to another
            instance object <=
        """
        return (self.area() <= other.area())

    def __eq__(self, other):
        """
            checks if equal to another
            instance object ==
        """
        return (self.area() == other.area())

    def __ge__(self, other):
        """
            checks if greater than or equal to another
            instance object >=
        """
        return (self.area() >= other.area())

    def __gt__(self, other):
        """
            checks if greater than another
            instance object >
        """
        return (self.area() > other.area())

    def __ne__(self, other):
        """
            checks if not equal another
            instance object !=
        """
        return (self.area() != other.area())


if __name__ == "__main__":

    s_5 = Square(5)
    s_6 = Square(6)

    if s_5 < s_6:
        print("Square 5 < Square 6")
    if s_5 <= s_6:
        print("Square 5 <= Square 6")
    if s_5 == s_6:
        print("Square 5 == Square 6")
    if s_5 != s_6:
        print("Square 5 != Square 6")
    if s_5 > s_6:
        print("Square 5 > Square 6")
    if s_5 >= s_6:
        print("Square 5 >= Square 6")
