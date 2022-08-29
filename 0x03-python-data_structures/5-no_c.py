#!/usr/bin/python3

from hashlib import new


def no_c(my_string):
    new_string = ""
    for ch in my_string:
        if not (ch == "c" or ch == "C"):
            new_string += ch
    return new_string


if __name__ == "__main__":
    print(no_c("Best School"))
    print(no_c("Chicago"))
    print(no_c("C is fun!"))
