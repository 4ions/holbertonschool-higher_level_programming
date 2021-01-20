#!/usr/bin/python3
""" Module of inheritance """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Class that inheriting from a rectangle class """

    def __init__(self, size):
        """ Initializes Square """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """ Area """
        return self.size * self.size
