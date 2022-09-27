#!/usr/bin/python3
""" adds all arguments to a Python
    list, and then save them to a file:
"""
import sys
import os
save_to_json = __import__("7-save_to_json_file").save_to_json_file
load_from_json = __import__("8-load_from_json_file").load_from_json_file


def add_item(args, filename):
    """ adds all arguments to a Python
        list, and then save them to a file:
    """
    try:
        content = load_from_json(filename)
    except:
        content = []
    for item in args:
        content.append(item)
    save_to_json(content, filename)


if __name__ == "__main__":
    args = sys.argv[1:]
    filename = "add_item.json"
    add_item(args, filename)
