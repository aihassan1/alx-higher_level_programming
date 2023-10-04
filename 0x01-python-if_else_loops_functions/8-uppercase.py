#!/usr/bin/python3


def uppercase(str):
    str_list = list(str)
    for i in range(len(str_list)):
        if ord(str_list[i]) >= 97 and ord(str_list[i]) <= 122:
            str_list[i] = chr(ord(str_list[i]) - 32)

    result_str = ''.join(str_list)

    print(result_str)
