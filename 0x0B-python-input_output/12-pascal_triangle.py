#!/usr/bin/python3
""" Create a pascal triangle """


def pascal_triangle(n):
    """ Create a pascal tringule and return in list """
    pascal_list = []
    if n <= 0:
        return (pascal_list)

    for i in range(0, n):
        pascal_list.append([])
        for j in range(0, i + 1):
            pascal_list[i].\
                append(binomialCoeff(i, j))

    return pascal_list


def binomialCoeff(n, k):
    """ calcule number """
    res = 1
    if (k > n - k):
        k = n - k
    for i in range(0, k):
        res = res * (n - i)
        res = res // (i + 1)
    return res
