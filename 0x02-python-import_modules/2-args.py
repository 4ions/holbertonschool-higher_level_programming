#!/usr/bin/python3
import sys
size = len(sys.argv)
if size - 1 == 0:
    print("{} arguments.".format(size - 1))
else:
    if size - 1 == 1:
        print("{} argument:".format(size - 1))
    else:
        print("{} arguments:".format(size - 1))
    for i in range(1, size):
        print("{}: {}".format(i, sys.argv[i]))
