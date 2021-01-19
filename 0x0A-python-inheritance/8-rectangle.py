#!/usr/bin/python3
""" Module of inheritance """


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Class of Rectangle """

    def __init__(self, width, height):
        """ Initialize new object of rectangle class """

        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__height = height
        self.__width = width
