#!/usr/bin/python3
""" module of json """
import json


def from_json_string(my_obj):
    """
    Decodes to string

    Keys in key/value pairs of JSON are always of the type str.
    When a dictionary is converted into JSON,
    all the keys of the dictionary are coerced to strings.
    As a result of this, if a dictionary is converted into
    JSON and then back into a dictionary, the dictionary may
    not equal the original one. That is, loads(dumps(x)) != x if x
    has non-string keys.
    """

    return(json.loads(my_obj))
