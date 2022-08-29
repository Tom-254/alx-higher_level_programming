#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    if not my_list:
        return
    for number in my_list[::-1]:
        print("{:d}".format(number))


if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    print_reversed_list_integer(my_list)
