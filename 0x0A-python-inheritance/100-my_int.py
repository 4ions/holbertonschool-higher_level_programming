#!/usr/bin/python3
class MyInt(int):
    """class to override int comparrisons"""
    def __eq__(self, other):
        """ Reference Equal """
        return int(self) != int(other)

    def __ne__(self, other):
        """ Reference diference """
        return int(self) == int(other)
