#!/usr/bin/python3
"""Defines a Rectangle class"""


class Rectangle:
    """Rectangle class"""

    def __init__(self, width=0, height=0):
        """Initializes the instance attributes to create a rectangle
            Args:
                width: size of the square
                height: height of rectangle
        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """Gets the width of the rectangle
           Returns:
                int: width of the rectangle class instance
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle
        Args:
            int: value to set as width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Gets the height of the rectangle
           Returns:
                int: height of the rectangle class instance
        """

        return self.__height

    @height.setter
    def height(self, value):
        """Sets the width of the rectangle
        Args:
            int: value to set as width
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value


if __name__ == "__main__":
    my_rectangle = Rectangle(2, 4)
    print(my_rectangle.__dict__)

    my_rectangle.width = 10
    my_rectangle.height = 3
    print(my_rectangle.__dict__)
