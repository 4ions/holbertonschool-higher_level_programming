#!/usr/bin/python3
""" Module add attribute """


def add_attribute(obj, name, value):
    """ Function to add new attribute IF possible """

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")

    setattr(obj, name, value)
