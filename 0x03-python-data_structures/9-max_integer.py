#!/usr/bin/python3


def max_integer(my_list=[]):

    biggest = my_list[0]

    for value in my_list:
        if biggest < value:
            biggest = value

    return biggest
