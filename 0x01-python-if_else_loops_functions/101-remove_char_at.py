#!/usr/bin/python3


def remove_char_at(str, n):
    copied_str = list(str)

    str_len = len(copied_str)
    if n > str_len or n < 0:
        return str

    copied_str.pop(n)
    modified_string = ''.join(copied_str)

    return modified_string
