#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys
if __name__ == "__main__":
    argv = sys.argv
    size = len(argv)
    if size - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <>")
        sys.exit(1)
    else:
        a = int(argv[1])
        b = int(argv[3])

    if argv[2] == "+":
        print("{} + {} = {}".format(a, b, add(a, b)))
    elif argv[2] == "-":
        print("{} - {} = {}".format(a, b, sub(a, b)))
    elif argv[2] == "*":
        print("{} * {} = {}".format(a, b, mul(a, b)))
    elif argv[2] == "/":
        print("{} / {} = {}".format(a, b, div(a, b)))
    else:
        print("Unknown operator. Avalible operators: +, -, * and /")
        sys.exit(1)
