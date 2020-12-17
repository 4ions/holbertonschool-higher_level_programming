#!/usr/bin/python3
def weight_average(my_list=[]):

    sum = 0
    div = 0
    if my_list:
        for i, j in list(my_list):
            sum += i * j
            div += j
        return sum / div
    return(0)
