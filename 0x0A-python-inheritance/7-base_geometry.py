#!/usr/bin/python3
""" Module of inheritance """


class BaseGeometry():
    """ class to Base Geometry """

    def area(self):
        """ area of geometry """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Integer Validator """
        if type(value) != int:
            raise TypeError("{:} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:} must be greater than 0".format(name))
