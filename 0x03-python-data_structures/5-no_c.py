#!/usr/bin/python3


def no_c(my_string):

    output = ''

    for char in my_string:
        if char != 'C' and char != 'c':
            output += char

    return output
