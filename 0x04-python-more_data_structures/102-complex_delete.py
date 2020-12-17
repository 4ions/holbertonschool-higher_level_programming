#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    myDict = {key: val for key, val in a_dictionary.items() if val == value}
    for search in myDict:
        a_dictionary.pop(search)
    return a_dictionary
