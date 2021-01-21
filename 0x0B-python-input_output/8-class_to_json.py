#!/usr/bin/python3
"""returns dict representation of class"""


def class_to_json(obj):
    """returns dict representation of class"""
    # cuando un objeto de clase o de definicion llama a __dict__
    # este mostrara el diccionario o la lista
    #  returns the dictionary description with simple data structure
    return (obj.__dict__)
