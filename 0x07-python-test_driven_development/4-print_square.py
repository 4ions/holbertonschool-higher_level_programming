#!/usr/bin/python3
""" sdasd """


def print_square(size):
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    
    for i in range(0, size):
        for i in range(0, size):
            print("#", end="")
        print()
