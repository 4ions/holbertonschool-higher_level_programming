#!/usr/bin/python3
def no_c(my_string):

    copy = ""
    for i in my_string:
        # "not int"" check if in my_string have 'Cc' and
        if i not in 'Cc':
            # "copy + i" concatenate each letters in copy
            copy = copy + i

    return (copy)
