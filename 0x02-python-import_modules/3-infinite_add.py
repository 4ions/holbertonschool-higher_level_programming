#!/usr/bin/python3
import sys
if __name__ == "__main__":
    argv = sys.argv
    size = len(argv)
    sum = 0
    for i in range(1, size):
        sum += int(argv[i])
    print("{:d}".format(sum))
