#!/usr/bin/python3
""" module of open files """


def append_write(filename="", text=""):
    """ write in to a file """

    chars = 0
    # "a" to append to end of file
    with open(filename, "a", encoding='utf-8') as writer:
        chars += writer.write(text)
    writer.closed
    return chars
