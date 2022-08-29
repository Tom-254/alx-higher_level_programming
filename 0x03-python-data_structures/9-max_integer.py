#!/usr/bin/python3

from distutils.archive_util import make_zipfile


def max_integer(my_list=[]):
    if not my_list:
        return None
    max_num = 0
    for num in my_list:
        if max_num <= num:
            max_num = num
    return max_num


if __name__ == "__main__":
    my_list = [1, 90, 2, 13, 34, 5, -13, 3]
    max_value = max_integer(my_list)
    print("Max: {}".format(max_value))