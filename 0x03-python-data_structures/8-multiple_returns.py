#!/usr/bin/python3


def multiple_returns(sentence):

    if len(sentence) == 0:
        sentence[0] = None

    str_len = len(sentence)
    first_char = sentence[0]

    tup = (str_len, first_char)

    return tup
