#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    size = len(my_list) - 1
    if idx < 0:
        return (my_list)
    if idx > size:
        return (my_list)
    for i in my_list:
        if i == idx:
            my_list[i] = element
    return (my_list)
