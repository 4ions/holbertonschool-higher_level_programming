#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        score = max(a_dictionary, key=a_dictionary.get)
        return(max(a_dictionary, key=a_dictionary.get))
    return None
