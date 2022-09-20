#!/usr/bin/python3
"""Contains a function that separates a string based on certain characters
"""


def text_indentation(text):
    """Adds a new line if a . or ? or : is detected
    Args:
        text (str): the string to look through
    """

    flag = 0
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for a in text:
        if flag == 0:
            if a == ' ':
                continue
            else:
                flag = 1
        if flag == 1:
            if a == '?' or a == '.' or a == ':':
                print(a)
                print()
                flag = 0
            else:
                print(a, end="")
