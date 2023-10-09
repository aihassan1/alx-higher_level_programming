#!/usr/bin/python3


def multiple_returns(sentence):

    str_len = len(sentence)
    first_char = sentence[0]

    if sentence[0] == []:
        sentence[0] = None

    tup = (str_len, first_char)
    return tup
