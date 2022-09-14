#!/usr/bin/python3

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

if __name__ == "__main__":

    my_square = Square(89)
    print("Area: {} for size: {}".format(my_square.area(), my_square.size))

    my_square.size = 3
    print("Area: {} for size: {}".format(my_square.area(), my_square.size))

    try:
        my_square.size = "5 feet"
        print("Area: {} for size: {}".format(my_square.area(), my_square.size))
    except Exception as e:
        print(e)
