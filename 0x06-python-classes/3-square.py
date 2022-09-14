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

    def area(self):
        """ Calculates area of square
            Returns:
                int: Square area calculated
        """
        return (self.__size ** 2)


if __name__ == "__main__":
    my_square_1 = Square(3)
    print("Area: {}".format(my_square_1.area()))

    try:
        print(my_square_1.size)
    except Exception as e:
        print(e)

    try:
        print(my_square_1.__size)
    except Exception as e:
        print(e)

    my_square_2 = Square(5)
    print("Area: {}".format(my_square_2.area()))
