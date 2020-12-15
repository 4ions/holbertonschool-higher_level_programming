#!/usr/bin/python3
def new_in_list(my_list, idx, element):

    copy = my_list.copy()
    size = len(my_list)
    if idx < 0:
        return (copy)
    if idx > size:
        return (copy)

    for i in my_list:
        if i == idx:
            copy[i] = element
        
    return (copy)
