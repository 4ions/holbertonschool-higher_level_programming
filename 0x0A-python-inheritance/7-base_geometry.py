#!/usr/bin/python3
""" Module of inheritance """


class BaseGeometry():
    """ class to Base Geometry """

    def __init__(self):
        """ Initializes new geometry """
        pass

    def area(self):
        """ area of geometry """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Integer Validator """
        self.name = name
        if type(value) != int:
            raise TypeError("{:} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{:} must be greater than 0".format(name))
        else:
            self.value = value
