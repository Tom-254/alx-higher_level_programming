#!/usr/bin/python3
from sys import argv
from calculator_1 import add, sub, mul, div

def calculator(arg1, operator, arg2):

    if operator == "+":
        print("{} + {} = {}".format(arg1, arg2, add(arg1, arg2)))
    elif operator == "-":
        print("{} - {} = {}".format(arg1, arg2, sub(arg1, arg2)))
    elif operator == "*":
        print("{} * {} = {}".format(arg1, arg2, mul(arg1, arg2)))
    elif operator == "/":
        print("{} / {} = {}".format(arg1, arg2, div(arg1, arg2)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

def main():
    arg_count = len(argv) - 1
    if arg_count != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    operator = argv[2]
    a = int(argv[1])
    b = int(argv[3])
    calculator(a, operator, b)

if __name__ == "__main__":
    main()
