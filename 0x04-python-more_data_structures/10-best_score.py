#!/usr/bin/python3


def best_score(a_dictionary):

    if a_dictionary is not None:
        if not a_dictionary:
            return None

        highest_key = max(a_dictionary, key=a_dictionary.get)
        return highest_key

    else:
        return None
