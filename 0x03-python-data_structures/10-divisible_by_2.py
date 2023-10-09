#!/usr/bin/python3


def divisible_by_2(my_list=[]):

    answer_list = []
    for value in my_list:
        if value % 2 == 0:
            answer_list.append(True)
        else:
            answer_list.append(False)

    return answer_list
