#!/usr/bin/python3


def roman_to_int(roman_string):

    if roman_string is None or not isinstance(roman_string, str):
        return 0

    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    roman_num_list = list(roman_string)
    total = 0

    for i in range(len(roman_num_list)):

        number = roman.get(roman_num_list[i])
        if number is None:
            return 0

        if i < len(roman_num_list) - 1:
            next_num = roman.get(roman_num_list[i + 1])
            if next_num > number:
                number = -number

        total += number

    return total
