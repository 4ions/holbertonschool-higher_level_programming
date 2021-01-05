#!/usr/bin/python
""" Square Module """


class Square:
        """ Class of square """
        def __init__(self, size=0):
                """ Check conditions of size """
                if isinstance(size, int):
                        if size >= 0:
                                self.__size = size
                        else:
                                raise ValueError("size must be >= 0")
                else:
                        raise TypeError("size must be an integer")

        def area(self):
                """ Area if a square """
                area = self.__size * self.__size
                return(area)

        @property
        def size(self):
            """ Return size """
            return self.__size

        @size.setter
        def size(self, value):
            """ setter """
            if isinstance(value, int):
                if value >= 0:
                    self.__size = value
                else:
                    raise ValueError("size must be >= 0")
            else:
                raise TypeError("size must be an integer")

        def my_print(self):
            """ prints a square of '#' """
            for i in range(self.__size):
                print('#' * self.__size)
            if self.__size == 0:
                print()
