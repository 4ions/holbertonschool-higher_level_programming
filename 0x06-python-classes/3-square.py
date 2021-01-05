#!/usr/bin/python3
""" Square Module """


class Square:
        """ Class of square """
        def __init__(self, size=0):
                """ Check conditions of size """
                if isinstance(size, int):
                        if size >= 0:
                                self.__size = size
                        else:
                                raise ValueError("size must be >= 0")
                else:
                        raise TypeError("size must be an integer")

        def area(self):
                """ Area if a square """
                area = self.__size * self.__size
                return(area)
