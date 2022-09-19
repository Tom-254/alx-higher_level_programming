#!/usr/bin/python3
"""Defines a Rectangle class"""


class Rectangle:
    """Rectangle class"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializes the instance attributes to create a rectangle
            Args:
                width: size of the square
                height: height of rectangle
        """

        self.width = width
        self.height = height

        Rectangle.number_of_instances += 1

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
        return ((str(self.print_symbol)
                * self.__width + "\n") * self.__height)[:-1]

    def __repr__(self):
        """Called to return a string represention of
           the rectangle that could be called using eval
           Returns:
                str: Representation of the rectangle
        """

        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Called after all references to Rectangle class object are deleted
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")


if __name__ == "__main__":
    my_rectangle_1 = Rectangle(8, 4)
    print(my_rectangle_1)
    print("--")
    my_rectangle_1.print_symbol = "&"
    print(my_rectangle_1)
    print("--")

    my_rectangle_2 = Rectangle(2, 1)
    print(my_rectangle_2)
    print("--")
    Rectangle.print_symbol = "C"
    print(my_rectangle_2)
    print("--")

    my_rectangle_3 = Rectangle(7, 3)
    print(my_rectangle_3)

    print("--")

    my_rectangle_3.print_symbol = ["C", "is", "fun!"]
    print(my_rectangle_3)

    print("--")
