#!/usr/bin/python3
def uniq_add(my_list=[]):
    s = set(my_list)
    sum = 0
    for i in s:
        sum += int(i)
    return (sum)
