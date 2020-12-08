#!/usr/bin/python3
def remove_char_at(str, n):
    for i in range(len(str)):
        if n > 0:
            if i != n:
                cpy = str[:n]
                cpy2 = str[n + 1:]
            return(cpy + cpy2)
        else:
            return(str)
