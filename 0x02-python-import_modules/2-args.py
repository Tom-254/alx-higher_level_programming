#!/usr/bin/python3
from sys import argv

def main():
    ag_count = len(argv) - 1

    if ag_count == 0:
        print("0 arguments.")

    elif ag_count == 1:
        print("1 argument:")
        print("1: {}".format(argv[1]))
    else:
        print("{:d} arguments:".format(ag_count))
        for i in range(1, ag_count + 1):
            print("{}: {}".format(i, argv[i]))

if __name__ == "__main__":
    main()
