#!/usr/bin/python3
""" asdsads """


def text_indentation(text):
    """ dsdsadsadas """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for c in ['.', '?', ':']:
        text = text.replace(c, c + '\n\n')
    new = [line.strip() for line in text.split('\n')]
    new = '\n'.join(new)
    print(new, end='')
