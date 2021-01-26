#!/usr/bin/python3
""" Module of retangle """
from models.base import Base


class Rectangle(Base):
    """ Class of Rectangle """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initialize """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """getter od width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter of width"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ Getter of height """
        return self.__height

    @height.setter
    def height(self, value):
        """ setter of height """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ Getter of x """
        return self.__x

    @x.setter
    def x(self, value):
        """ setter if x """
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ Getter of y """
        return self.__y

    @y.setter
    def y(self, value):
        """ setter of y """
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ area of rectangle """
        return self.__width * self.__height

    def display(self):
        """ display rectangle """
        for i in range(self.y):
            print()
        for i in range(self.__height):
            size = self.__x - 1
            print(" " * size, "#" * self.width)

    def __str__(self):
        """ change the build-in str """
        return ("[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format
                (self.id, self.x, self.y, self.width, self.height))

    def update(self, *args, **kwargs):
        """ update the values """
        if len(args):
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.width = arg
                elif i == 2:
                    self.height = arg
                elif i == 3:
                    self.x = arg
                elif i == 4:
                    self.y = arg

        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """ Dictionary of rectangle """
        dic = {}
        dic["id"] = self.id
        dic["width"] = self.width
        dic["height"] = self.height
        dic["x"] = self.x
        dic["y"] = self.y
        return dic
