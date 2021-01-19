#!/usr/bin/python3
""" Module that inherits from list """


class MyList(list):
    """ Class of my list """
    def print_sorted(self):
        """ Print sorted list """
        print(sorted(self))
