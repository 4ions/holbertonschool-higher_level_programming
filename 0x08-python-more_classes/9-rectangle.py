#!/usr/bin/python3
""" Module of rectangle """


class Rectangle():
    """ Class of rectangle """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """ instantiation of rectangle """
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        """ Return the area of rectangle """
        return(self.__width * self.__height)

    def perimeter(self):
        """ return the perimeter of a rectangle """
        if self.__width == 0 or self.__height == 0:
            return(0)
        return((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """ return a rectangle with # """
        t = ''
        if self.__width != 0 and self.__height != 0:
            for i in range(self.__height):
                t += str((self.print_symbol * self.__width)) + '\n'
        return(t[:-1])

    def __repr__(self):
        """returns string of rectangle"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """ When deleting show message """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ Return the bigger rect or if are equal """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        return(rect_1 if rect_1.area() >= rect_2.area() else rect_2)

    @classmethod
    def square(cls, size=0):
        """ returns a new Rectangle instance """
        return cls(size, size)
