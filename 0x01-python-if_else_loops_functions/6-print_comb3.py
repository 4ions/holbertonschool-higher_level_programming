#!/usr/bin/python3
for i in range(0, 99):
    if i < 10 and i != 0:
        print("0{:d}, ".format(i), end="")
    elif i//10 != i % 10 and i > 9 and i < 89 and i//10 < i % 10:
        print("{:d}, ".format(i), end="")
    elif i == 89:
        print("{:d}".format(i))
