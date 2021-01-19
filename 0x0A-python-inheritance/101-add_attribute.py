#!/usr/bin/python3


def add_attribute(obj, name, value):
    """ Function to add new attribute IF possible """

    if not hasattr(obj, "__dict__"):
        raise TypeError("Can't add new attribute")

    setattr(obj, name, value)
