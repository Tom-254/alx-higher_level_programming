#!/usr/bin/python3
"""Defines Square class"""


class Square:
    """Square representation"""

    def __init__(self, size):
        """Initializes the instance attributes
            Args:
                size: size of the square
        """
        self.__size = size


if __name__ == "__main__":
    my_square = Square(3)
    print(type(my_square))
    print(my_square.__dict__)

    try:
        print(my_square.size)
    except Exception as e:
        print(e)

    try:
        print(my_square.__size)
    except Exception as e:
        print(e)
