#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    _number = number * -1
    tmp = (_number % 10) * -1
else:
    _number = number
    tmp = _number % 10
if tmp > 5:
    print("Last digit of {} is {} and is greater than 5".format(number, tmp))
elif tmp == 0:
    print("Last digit of {} is {} and is 0".format(number, tmp))
else:
    print("Last digit of {} is {} and \
is less than 6 and not 0".format(number, tmp))
