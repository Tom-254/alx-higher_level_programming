#!/usr/bin/python3
"""Contains  function that reads a text file (UTF8) and prints it to stdout"""


def read_file(filename=""):
    """Reads a text file (UTF8) and prints it to stdout
        Args:
            filename (str): name of the file
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read())


if __name__ == "__main__":
    read_file("my_file_0.txt")
