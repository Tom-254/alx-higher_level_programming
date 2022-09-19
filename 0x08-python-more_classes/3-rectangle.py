#!/usr/bin/python3
"""Defines a Rectangle class"""


class Rectangle:
    """Rectangle class"""

    def __init__(self, width=0, height=0):
        """Initializes the instance attributes to create a rectangle
            Args:
                width (int): size of the square
                height (int): height of rectangle
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
            value (int): value to set as width
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
            value (int): value to set as width
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Calculates area of rectangle area (h * w)
            Returns:
                int: Rectangle area calculated
        """
        return self.__height * self.__width

    def perimeter(self):
        """ Calculates perimeter of rectangle perimeter 2 * (h + w)
            Returns:
                int: Rectangle perimeter calculated
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def area(self):
        """ Calculates area of rectangle area (h * w)
            Returns:
                int: Rectangle area calculated
        """
        return self.__height * self.__width

    def perimeter(self):
        """ Calculates perimeter of rectangle perimeter 2 * (h + w)
            Returns:
                int: Rectangle perimeter calculated
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """Called to return a string represention of
           the rectangle when printed
           Returns:
                str: Representation of the rectangel using (#) symbol
        """
        return (("#" * self.__width + "\n") * self.__height)[:-1]


if __name__ == "__main__":
    my_rectangle = Rectangle(2, 4)
    print("Area: {} - Perimeter: {}".format(my_rectangle.area(),
          my_rectangle.perimeter()))

    print(str(my_rectangle))
    print(repr(my_rectangle))

    print("--")

    my_rectangle.width = 10
    my_rectangle.height = 3
    print(my_rectangle)
    print(repr(my_rectangle))
