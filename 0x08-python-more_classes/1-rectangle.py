#!/usr/bin/python3
""" Module of rectangle """


class Rectangle():
    """ Class of rectangle """

    def __init__(self, width=0, height=0):
        """ instantiation of rectangle """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """ Return the width """
        return(self.__width)

    @width.setter
    def width(self, value):
        """ Sets width on rectangle """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Return the height """
        return(self.__height)

    @height.setter
    def height(self, value):
        """ set the height on rectangle """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
