#!/usr/bin/python3
""" Square Module """


class Square:
        """ Class of Square """
        def __init__(self, size=0):
                """ check conditions of size """
                if isinstance(size, int):
                        if size >= 0:
                                self.__size = size
                        else:
                                raise ValueError("size must be >= 0")
                else:
                        raise TypeError("size must be an integer")
