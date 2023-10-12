#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):
    output = sorted(a_dictionary.items(), key=lambda item: item[0].lower())
    for key, value in output:
        print(f"{key}: {value}")
