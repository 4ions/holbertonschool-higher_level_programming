#!/usr/bin/python3
""" Function that adds 2 integers"""


def add_integer(a, b=98):
    """ Adds two integers """
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return int(a) + int(b)
    else:
        if isinstance(a, (int, float)):
            c = 'b'
        else:
            c = 'a'
        raise TypeError("{} must be an integer".format(c))
