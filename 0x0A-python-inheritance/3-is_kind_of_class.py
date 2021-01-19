#!/usr/bin/python3
""" Module of inherit """


def is_kind_of_class(obj, a_class):
    """ class that return true or false if a instance of a class """
    return(True if isinstance(obj, a_class) else False)
