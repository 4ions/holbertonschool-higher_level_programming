#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import exit, argv
if __name__ == "__main__":
    argv = argv
    size = len(argv)
    if size - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <>")
        exit(1)
    
    a = int(argv[1])
    b = int(argv[3])

    if argv[2] == "+":
        print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
    elif argv[2] == "-":
        print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
    elif argv[2] == "*":
        print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
    elif argv[2] == "/":
        print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
    else:
        print("Unknown operator. Avalible operators: +, -, * and /")
        exit(1)
