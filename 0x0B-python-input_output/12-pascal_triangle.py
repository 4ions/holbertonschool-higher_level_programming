#!/usr/bin/python3
""" Create a pascal triangle """


def pascal_triangle(n):
    """ Create a pascal tringule and return in list """
    pascal_list = []
    if n <= 0:
        return (pascal_list)

    for i in range(0, n):
        pascal_list.append([])
        pascal_list[i].append(1)
        for j in range(0, i):
            pascal_list[i].\
                append(pascal_list[i - 1][j - 1] + pascal_list[i - 1][j])

    return pascal_list
