#!/usr/bin/python3
""" Module of Read files """


def read_file(filename=""):
    """ read a file """

    # "r" to read
    with open(filename, encoding='utf-8') as f:
        for line in f:
            print(line, end="")
        f.closed
    print()
