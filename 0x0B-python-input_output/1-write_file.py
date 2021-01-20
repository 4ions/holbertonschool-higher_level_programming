#!/usr/bin/python3
""" module of open files """


def write_file(filename="", text=""):
    """ write in to a file """
    chars = 0
    # "w" to write
    with open(filename, "w", encoding='utf-8') as writer:
        chars += writer.write(text)
    writer.closed
    return chars
