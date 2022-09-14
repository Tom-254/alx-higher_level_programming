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

    def my_print(self):
        """prints out the square representaion with the
            character "#" to the stdout
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size, end='')
                print()

if __name__ == "__main__":

    my_square = Square(3)
    my_square.my_print()

    print("--")

    my_square.size = 10
    my_square.my_print()

    print("--")

    my_square.size = 0
    my_square.my_print()

    print("--")
