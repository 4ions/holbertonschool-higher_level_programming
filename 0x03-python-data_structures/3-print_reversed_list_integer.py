def print_reversed_list_integer(my_list=[]):
    size = len(my_list)
    my_list.reverse()
    for i in my_list:
        print("{}".format(i))
