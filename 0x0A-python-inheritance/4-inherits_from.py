#!/usr/bin/python3
""" Module of inherit """


def inherits_from(obj, a_class):
    """ Return true or false if obj is sub class of a_class """
    return(isinstance(obj, a_class) and type(obj) != a_class)
