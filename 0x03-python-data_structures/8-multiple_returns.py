#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        first = None
    size = len(sentence)
    first = sentence[:1]
    return(size, first)
