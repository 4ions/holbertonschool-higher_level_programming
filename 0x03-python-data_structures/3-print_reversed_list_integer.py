def print_reversed_list_integer(my_list=[]):
    size = len(my_list)
    my_list.reverse()
    for i in range(0, size):
        print(my_list[i])
