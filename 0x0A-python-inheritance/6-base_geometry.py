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
