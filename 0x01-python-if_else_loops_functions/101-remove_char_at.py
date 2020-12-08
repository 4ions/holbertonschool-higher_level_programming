#!/usr/bin/python3
def remove_char_at(str, n):
    if n > -1:
        cpy = str[:n]
        cpy2 = str[n + 1:]
        return(cpy + cpy2)
    else:
        return(str)
