#!/usr/bin/python3
"""
Contains a class MyList that inherits from list builtin
"""


class MyList(list):
    """Inherits from the list class"""

    def __init__(self):
        """Initializes the object
        """
        super().__init__()

    def print_sorted(self):
        """Prints the sorted list
        """
        print(sorted(self))

if __name__ == "__main__":
    my_list = MyList()
    my_list.append(1)
    my_list.append(4)
    my_list.append(2)
    my_list.append(3)
    my_list.append(5)
    print(my_list)
    my_list.print_sorted()
    print(my_list)
