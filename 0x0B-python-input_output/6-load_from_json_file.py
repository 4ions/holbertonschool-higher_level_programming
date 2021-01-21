#!/usr/bin/python3
""" module of load from json """
import json


def load_from_json_file(filename):
    """
    create a object from a json

    se usa loads porque es el ideal para eliminar las llaves
    en los diccionarios puede manejar tambien listas
    "This simple serialization technique can handle lists and
    dictionaries"

    When a dictionary is converted into JSON, all the keys
    of the dictionary are coerced to strings. As a result
    of this, if a dictionary is converted into JSON and
    then back into a dictionary, the dictionary may not
    equal the original one. That is, loads(dumps(x)) != x
    if x has non-string keys.
    """

    with open(filename, "r", encoding="utf-8") as f:
        dicti = json.loads(f.read())
    return dicti
