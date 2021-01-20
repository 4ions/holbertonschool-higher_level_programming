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

    def area(self):
        """ Area """
        return self.__height * self.__width

    def __str__(self):
        """ STR """
        return "[{}] {:d}/{:d}".format("Rectangle", self.__width,
                                       self.__height)


class Square(Rectangle):
    """ Class that inheriting from a rectangle class """
    def __init__(self, size):
        """ Initializes Square """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """ Area """
        return super().area()
